from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from sqlalchemy.exc import DataError, IntegrityError
from json.decoder import JSONDecodeError
from sqlalchemy.exc import DBAPIError
import requests
import json
from ..models.gmk_board import DBBoard
from ..models.schemas import DBBoardSchema
from uuid import uuid4


class BoardAPIView(APIViewSet):
    """ Create, view, update, list all
    """
    def create(self, request):
        """ Create a new Gomoku Game
            POST api/v1/board/newgame
        """
        import pdb; pdb.set_trace()
        try:
            kwargs = json.loads(request.body)
        except JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        try:
            kwargs['uuid'] = uuid4.uuid()
            board = DBBoard.new(request, **kwargs)
        except IntegrityError:
            return Response(json='uuid does not exist', status=400)

        schema = DBBoardSchema()
        data = schema.dump(board).data
        return Response(json=data, status=201)

    def update(self, request, id=None):
        """ Send a new move on a given game
            PUT api/v1/board/**kwargs
        """
        import pdb; pdb.set_trace()
        try:
            kwargs = json.loads(request.body)
        except JSONDecodeError as e:
            return Response(json=e.msg, status=400)
        try:
            board = DBBoard.update(request=request, **kwargs)
        except (DataError, AttributeError):
            return Response(json='sent information is invalid', status=400)

        schema = DBBoardSchema()
        data = schema.dump(board).data
        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """ Get one Gomoku Game with given id
            GET api/v1/board/**kwargs
        """
        import pdb; pdb.set_trace()
        try:
            kwargs = json.loads(request.body)
        except JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        try:
            board = DBBoard.one(request=request, **kwargs)
        except (DataError, AttributeError):
            return Response(json='sent information is invalid', status=400)

        schema = DBBoardSchema()
        data = schema.dump(board).data
        return Response(json=data, status=200)

    def list(self, request):
        """ List all current running games
            GET api/v1/board
        """
        import pdb; pdb.set_trace()
        if request is None:
            return Response(json='Not Found', status=400)

        all_records = DBBoard.all(request)
        schema = DBBoardSchema()
        data = [schema.dump(record).data for record in all_records]
        return Response(json=data, status=200)
