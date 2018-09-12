import sys
import uuid
from textwrap import dedent
try:
    from .gmk_board import Board
except ModuleNotFoundError:
    from gmk_board import Board

# stone placement verification


# bd.stone = 1


# bd.place_piece(7, 7)
# bd.place_piece(6, 8)
# bd.place_piece(5, 9)
# bd.place_piece(4, 10)
# bd.place_piece(3, 11)

# bd.place_piece(7, 7)
# bd.place_piece(6, 8)
# bd.place_piece(5, 9)
# bd.place_piece(4, 10)
# bd.place_piece(3, 11)


# bd.place_piece(7, 7)
# bd.place_piece(7, 8)
# bd.place_piece(7, 9)
# bd.place_piece(7, 10)
# bd.place_piece(7, 11)


def make_move(bd, stone, y, x):
    """
        Make Move on a board
        Input is a gameboard(2D List), stone(a character), and y and x(integers)
        Output is a Boolean
    """
    bd.place_piece(stone, y, x)
    display_board(bd)
    # import pdb; pdb.set_trace()
    return bd._check_vertical_match(stone, y, x)


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


def display_board(bd):
    """
    board spaced for stone placement
    """
    print(f'''
             00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14  [X]
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

        [Y]
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
        bd = Board()
        display_board(bd)
        make_move(bd, 1, 1, 1)
        make_move(bd, 1, 2, 2)
        make_move(bd, 1, 5, 5)
        make_move(bd, 1, 4, 4)
        while not bd.done:
            xinput = int(input('X : '))
            yinput = int(input('Y: '))
            stone = int(input('stone: '))
            bd.done = make_move(bd, stone, yinput, xinput)

    except KeyboardInterrupt:
        exit()
