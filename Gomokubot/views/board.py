from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from sqlalchemy.exc import DataError, IntegrityError
from json.decoder import JSONDecodeError
from sqlalchemy.exc import DBAPIError
import requests
import json
from ..models.gmk_board import DBBoard, Board
from ..models.schemas import DBBoardSchema
from uuid import uuid4


class BoardAPIView(APIViewSet):
    """ Create, view, update, list all
    """
    def create(self, request):
        """ Create a new Gomoku Game
            POST api/v1/board
        """
        kwargs = {}
        try:
            kwargs['uuid'] = str(uuid4())
            board = DBBoard.new(request, **kwargs)
        except IntegrityError:
            return Response(json='failed to create new game', status=400)

        schema = DBBoardSchema()
        data = schema.dump(board).data
        return Response(json=data, status=201)

    def update(self, request, id=None):
        """ Send a new move on a given game, validates the win status, updates to db
            PUT api/v1/board/#
        """
        try:
            kwargs = json.loads(request.body)
            xaxis = int(kwargs['X'])
            yaxis = int(kwargs['Y'])
        except JSONDecodeError as e:
            return Response(json=e.msg, status=400)
        try:
            currentgame = DBBoard.retrieve(request=request, **kwargs)
        except (DataError, AttributeError):
            return Response(json='Invalid Information', status=400)

        if currentgame.gameboard[yaxis][xaxis] != 0:
            return Response(json='Coordinate already selected', status=400)
        player_stone = int(kwargs['stone'])
        currentgame.gameboard[yaxis][xaxis] = player_stone

        basegame = Board()
        basegame.board = currentgame.gameboard

        currentgame.finished = basegame.check_vertical_match(player_stone, yaxis, xaxis)
        # import pdb; pdb.set_trace()
        # Opponent winning condition
        if currentgame.finished:
            update_db = {'uuid': currentgame.uuid, 'gameboard': currentgame.gameboard, 'finished': currentgame.finished}

        # Computer move
        else:
            computer_player = Board()
            computer_player.board = currentgame.gameboard
            if kwargs['stone'] == '1':
                ymove, xmove = computer_player.auto_move(2)
                computer_player.board[ymove][xmove] = 2
                currentgame.finished = computer_player.check_vertical_match(2, ymove, xmove)
            else:
                ymove, xmove = computer_player.auto_move(1)
                computer_player.board[ymove][xmove] = 1
                currentgame.finished = computer_player.check_vertical_match(1, ymove, xmove)

            update_db = {'uuid': currentgame.uuid, 'gameboard': computer_player.board, 'finished': computer_player.finished}

        try:
            board = DBBoard.update(update_db, request)
        except (DataError, AttributeError):
            return Response(json='Failed to update database', status=400)

        if currentgame.finished:
            transfer_data = {'finished': currentgame.finished, 'uuid': currentgame.uuid, 'gametype': board.gametype}
        else:
            transfer_data = {'finished': computer_player.finished, 'uuid': currentgame.uuid, 'gametype': board.gametype, 'X': xmove, 'Y': ymove}

        schema = DBBoardSchema()
        data = schema.dump(transfer_data).data
        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """ Get one Gomoku Game with given id
            GET api/v1/board/#
        """
        try:
            kwargs = json.loads(request.body)
        except JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        try:
            board = DBBoard.retrieve(request=request, **kwargs)
        except (DataError, AttributeError):
            return Response(json='sent information is invalid', status=400)

        schema = DBBoardSchema()
        data = schema.dump(board).data
        return Response(json=data, status=200)

    def list(self, request):
        """ List all current running games
            GET api/v1/board
        """
        if request is None:
            return Response(json='Not Found', status=400)

        all_records = DBBoard.all(request)
        schema = DBBoardSchema()
        data = [schema.dump(record).data for record in all_records]
        return Response(json=data, status=200)
