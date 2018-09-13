from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
import transaction
from random import randrange
from sqlalchemy import (
    Boolean,
    String,
    Column,
    Text,
    Integer,
    JSON,
)
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import zope.sqlalchemy
from pyramid.paster import (
    get_appsettings,
    setup_logging,
)
from pyramid.scripts.common import parse_vars
from .meta import Base
import json
from uuid import uuid4


class Board:
    def __init__(self, board=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]):
        """
        GMK board class.
        game id for each instance.
        moves in order by play
        """
        self.done = False
        self.p1_stone = '1'
        self.p2_stone = '2'
        self.finished = False
        self.board = board

    def auto_move(self, stone):
        """
        IN: Board.board
        OUT: self.place_piece(x, y)
        """
        deciding = True
        while deciding:
            x = int(randrange(0, 5))
            y = int(randrange(0, 5))

            if self.board[y][x] == 0:
                self.board[y][x] = stone
                deciding = False
                return(y, x)

    def place_piece(self, stone, x=0, y=0):
        if self.board[x][y] == 0:
            self.board[x][y] = stone  # being 1 or 2
            return True
        else:
            return False

    def check_vertical_match(self, stone, y, x):
        """
        Validates the upper and lower stones of given coordinate,
        validates if connected 3
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
            for e in range(x + 1, 5):
                if self.board[y][e] is stone:
                    counter += 1
                else:
                    check_down = True
                    break
            check_down = True
            break

        if counter <= 2:
            return self._check_horizontal_match(stone, y, x)
        print('_check_vertical_match')
        return True

    def _check_horizontal_match(self, stone, y, x):
        """ Validates the left and right sides of stones of given coordinate, validates if connected 3
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
            for e in range(y + 1, 5):
                if self.board[e][x] is stone:
                    counter += 1
                else:
                    check_right = True
                    break
            check_right = True
            break

        if counter <= 2:
            return self._check_dignal_LR_match(stone, y, x)
        print('_check_horizontal_match')
        return True

    def _check_dignal_LR_match(self, stone, y, x):
        """
        """
        counter = 0
        check_lowerleft = False
        check_upperright = False

        while check_lowerleft is False:
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
            for e in range(1, 4):
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
        if counter < 3:
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
                for i in range(4):
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
            for e in range(1, 3):
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
        if counter < 3:
            return False
        print('_check_diagnal_RL_match')
        return True


class DBBoard(Base):
    __tablename__ = 'gameboards'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255), nullable=False)
    X = Column(Integer)
    Y = Column(Integer)
    gameboard = Column(JSON, default=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],

        ])
    finished = Column(Boolean, nullable=False, default=False)
    gametype = Column(String(31))

    @classmethod
    def new(cls, request=None, **kwargs):
        """
            Creates a new entry in our DB for this new game and board
        """
        if request is None:
            raise DBAPIError
        board = cls(**kwargs)
        request.dbsession.add(board)
        request.dbsession

        return request.dbsession.query(cls).filter(
            cls.uuid == kwargs['uuid']).one_or_none()

    @classmethod
    def update(cls, newupdate, request=None):
        """
            Update a gameboard with new data. Note the incoming kwargs will need a JSON object called gameboard assigned to it.
        """
        if request is None:
            raise DBAPIError
        gb = newupdate['gameboard']
        done = newupdate['finished']
        data = {'gameboard': gb, 'finished': done}

        # Due to commit failed to work, following code were copied and pasted to load transaction manager
        config_uri = 'production.ini'
        options = parse_vars([])
        setup_logging(config_uri)
        settings = get_appsettings(config_uri, options=options)

        engine = engine_from_config(settings, 'sqlalchemy.')

        Base.metadata.create_all(engine)

        factory = sessionmaker(expire_on_commit=True)
        factory.configure(bind=engine)
        session_factory = factory

        with transaction.manager:
            dbsession = session_factory()
            zope.sqlalchemy.register(dbsession, transaction_manager=transaction.manager)
            game = dbsession.query(cls).filter(cls.uuid == newupdate['uuid']).first()
            game.gameboard = newupdate['gameboard']
            dbsession.flush()

        dbsession.close()
        engine.dispose()

        return request.dbsession.query(cls).filter(cls.uuid == newupdate['uuid']).one_or_none()

    @classmethod
    def retrieve(cls, request=None, **kwargs):
        """
            Get a specific gameboard
        """
        if request is None:
            raise DBAPIError
        return request.dbsession.query(cls).filter(cls.uuid == kwargs['uuid']).one_or_none()

    @classmethod
    def all(cls, request):
        """ return all of gameboard data
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()
