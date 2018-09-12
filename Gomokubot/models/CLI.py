import sys
import uuid
from textwrap import dedent
from random import randrange
from gmk_board import Board


bd = Board()


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
    global bd
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


def make_move(bd, stone, y, x):
    global bd
    bd.place_piece(stone, y, x)
    display_board(bd)
    # import pdb; pdb.set_trace()
    return bd._check_vertical_match(stone, y, x)


def turn_cycle():
    global bd
    while not bd.done:
        xinput = int(input('X : '))
        yinput = int(input('Y: '))
        bd.done = make_move(bd, stone, yinput, xinput)


def turn_flip_and_cycle():
    global bd

    # decide stone
    num = randrange(0, 10)
    if num % 2 == 0:
        # X/black chosen, CLI goes first
        CLI_stone = bd.p1_stone
        # cpu gets O
        CPU_stone = bd.p2_stone
        print('You move first!')

        while not bd.done:
            xinput = int(input('X : '))
            yinput = int(input('Y: '))
            bd.done = make_move(bd, stone, yinput, xinput)

    else:
        # O/white chosen, CLI goes second
        CLI_stone = bd.p2_stone
        # cpu gets X
        CPU_stone = bd.p1_stone
        print('Opponent moves first!')

        while not bd.done:
            xinput = int(input('X : '))
            yinput = int(input('Y: '))
            bd.done = make_move(bd, stone, yinput, xinput)


def core():
    display_board(bd)
    turn_flip_and_cycle()


if __name__ == '__main__':
    '''
    run : core
    key exit : polite
    '''
    try:
        core()

    except KeyboardInterrupt:
        exit()
