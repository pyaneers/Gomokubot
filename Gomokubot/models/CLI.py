import sys
import uuid
from textwrap import dedent
<<<<<<< HEAD
from gmk_board import Board
=======
# from .gmk_board import Board as bd

# this class should be removed, and imported instead.
# need to learn how to handle the imports in conjuction w/ __main__


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

        # Black goes first.
        # Black 1, white 2.
        self.stone = 0
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

    def place_piece(self, x=0, y=0):
        # move argument is derived from JSON response in the form of
        # (X,Y) X: OVER | Y: DOWN
        if self.board[x][y] == 0:
            self.board[x][y] = self.stone
            # after placement, call the Fx that initiates the
            # sending of me move made to the waiting player.

        else:
            print('coordinate marked; illegal move')
            return IndexError
>>>>>>> fe967c531b8b2d163514d2a1b5ffd965ee998c2a


# stone placement verification


bd = Board()


bd.stone = 1


bd.place_piece(7, 7)


bd.place_piece(7, 9)


bd.place_piece(8, 7)


bd.stone = 2


bd.place_piece(7, 8)


bd.place_piece(8, 8)


bd.place_piece(9, 7)


def draw_board_row(line):
    """
    evaluates the board class and draws stone locations
    (<four monospace>)
    """
    row = ''
    for place in line:
        if place == 0:
            row += (' .  ')
        if place == 1:
            row += (' X  ')
        if place == 2:
            row += (' O  ')
    return row


def display_board():
    """
    board spaced for stone placement
    """
    print(f'''
             00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14
             ----------------------------------------------------------
        00 | {draw_board_row(bd.board[0])}

        01 | {draw_board_row(bd.board[1])}

        02 | {draw_board_row(bd.board[2])}

        03 | {draw_board_row(bd.board[3])}

        04 | {draw_board_row(bd.board[4])}

        05 | {draw_board_row(bd.board[5])}

        06 | {draw_board_row(bd.board[6])}

        07 | {draw_board_row(bd.board[7])}

        08 | {draw_board_row(bd.board[8])}

        09 | {draw_board_row(bd.board[9])}

        10 | {draw_board_row(bd.board[10])}

        11 | {draw_board_row(bd.board[11])}

        12 | {draw_board_row(bd.board[12])}

        13 | {draw_board_row(bd.board[13])}

        14 | {draw_board_row(bd.board[14])}
    ''')


def exit():
    '''
    exits the app
    '''
    print(dedent('''
        EXIT PHRASE
    '''))
    sys.exit()


if __name__ == '__main__':
    '''
    run : core
    key exit : polite
    '''
    try:
        display_board()
    except KeyboardInterrupt:
        exit()
