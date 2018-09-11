# from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Boolean,
    String,
    Column,
    Text,
    # DateTime,
    Integer,
    # Index,
    # ForeignKey,
)
from .meta import Base


import uuid


class Board():
    def __init__(self):
        """
        GMK board class.
        game id for each instance.
        moves in order by play
        """
        self.game_id = uuid.uuid4().hex

        # match is CC, CP, or PP
        self.match = []

        # remains False until the board is read with victory conditions,
        # is then turned True and turned into other player.
        self.done = False

        # Each move made is appended to list as made.
        self.moves = []

        # 2D array. self.board[0][0] to self.board[14][14]
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def __str__(self):
        return(
            f'game_id: {self.game_id} | '
            f'done: {self.done} | moves: {self.moves}'
            )

    def __repr__(self):
        return(
            f'<BOARD | game_id: {self.game_id} | '
            f'done: {self.done} | moves: {self.moves}'
            )

    def place_piece(self, stone, x=0, y=0):
        # move argument is derived from JSON response in the form of
        # (X,Y) X: OVER | Y: DOWN
        if self.board[x][y] == 0:
            self.board[x][y] = stone
            # after placement, call the Fx that initiates the
            # sending of me move made to the waiting player.

        else:
            print('coordinate marked; illegal move')
            return IndexError

    def _check_vertical_match(self, stone, y, x):
        """ Validates the upper and lower stones of given coordinate, validates if connected 5
        """
        counter = 0
        check_up = False
        check_down = False

        while check_up is False:
            for i in range(x, 0, -1):
                if self.board[y][i] is stone:
                    counter += 1
                else:
                    check_up = True
                    break
            check_up = True
            break

        while check_down is False:
            for e in range(x + 1, 15):
                if self.board[y][e] is stone:
                    counter += 1
                else:
                    check_down = True
                    break
            check_down = True
            break

        if counter <= 4:
            return self._check_horizontal_match(stone, y, x)
        print('_check_vertical_match')
        return True

    def _check_horizontal_match(self, stone, y, x):
        """ Validates the left and right sides of stones of given coordinate, validates if connected 5
        """
        counter = 0
        check_left = False
        check_right = False

        while check_left is False:
            for i in range(y, 0, -1):
                if self.board[i][x] is stone:
                    counter += 1
                else:
                    check_left = True
                    break
            check_left = True
            break

        while check_right is False:
            for e in range(y + 1, 15):
                if self.board[e][x] is stone:
                    counter += 1
                else:
                    check_right = True
                    break
            check_right = True
            break

        if counter <= 4:
            # import pdb; pdb.set_trace()
            return self._check_dignal_LR_match(stone, y, x)
        print('_check_horizontal_match')
        return True

    def _check_dignal_LR_match(self, stone, y, x):
        """
        """
        # import pdb; pdb.set_trace()
        counter = 0
        check_lowerleft = False
        check_upperright = False

        while check_lowerleft is False:
            # import pdb; pdb.set_trace()
            for i in range(6):
                try:
                    if self.board[y - i][x - i] is stone:
                        counter += 1
                    else:
                        check_lowerleft = True
                        break
                except IndexError:
                    pass
            check_lowerleft = True
            break

        while check_upperright is False:
            for e in range(1, 5):
                try:
                    if self.board[y + e][x + e] is stone:
                        counter += 1
                    else:
                        check_upperright = True
                        break
                except IndexError:
                    pass
            check_upperright = True
            break
        if counter < 5:
            return self._check_diagnal_RL_match(stone, y, x)
        print('_check_dignal_LR_match')
        return True

    def _check_diagnal_RL_match(self, stone, y, x):
        """
        """
        counter = 0
        check_lowerleft = False
        check_upperright = False

        while check_lowerleft is False:
            try:
                for i in range(6):
                    if i > x:
                        check_lowerleft = True
                    if self.board[y - i][x + i] is stone:
                        counter += 1
                    else:
                        check_lowerleft = True
                        break
            except IndexError:
                pass
            check_lowerleft = True
            break

        while check_upperright is False:
            for e in range(1, 5):
                # import pdb; pdb.set_trace()
                try:
                    if e > x:
                        check_upperright = True
                    if self.board[y + e][x - e] is stone:
                        counter += 1
                    else:
                        check_upperright = True
                        break
                except IndexError:
                    pass
            check_upperright = True
            break
        if counter < 5:
            return False
        print('_check_diagnal_RL_match')
        return True


class DBBoard(Base):
    __tablename__ = 'gameboards'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255), nullable=False)
    gameboard = Column(Text)
    finished = Column(Boolean)
    gametype = Column(String(31))

    @classmethod
    def new(cls, request=None, **kwargs):
        if request is None:
            raise DBAPIError
        board = cls(**kwargs)
        request.dbsession.add(board)
        # request.dbsession.u

        return request.dbsession.query(cls).filter(
            cls.uuid == kwargs['uuid']).one_or_none()

    def update(stuff):
        # takes in same param as new one,
        # qrs the db, puts new stone,
        # returns updated board
