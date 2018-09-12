import sys
import uuid
import json
from textwrap import dedent

try:
    from .gmk_board import Board
except ModuleNotFoundError:
    from gmk_board import Board

from random import randrange

# call the api with a post, api instantiates game with uuid
# url = 'localhost:6543/api/v1/board'
import pdb; pdb.set_trace()
url = 'http://ec2-18-223-100-124.us-east-2.compute.amazonaws.com/api/v1/board'
response = request.post(url)
bd = json.loads(response.body)


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


# DEPRIC
# def turn_cycle():
#     global bd
#     while not bd.done:
#         xinput = int(input('X : '))
#         yinput = int(input('Y: '))
#         bd.done = make_move(bd, stone, yinput, xinput)


#     # if bd._check_vertical_match(stone, y, x):

#     return bd._check_vertical_match(stone, y, x)
#     # TODO: this check needs to be tied to the game cycle on the ''front end''

coin = True


def flip():
    global coin
    num = randrange(0, 10)
    if num % 2 == 0:
        coin = True
    else:
        coin = False


def turn_cycle():
    global bd
    global coin

    # decide stone

    if coin:
        # X/black chosen, CLI goes first
        CLI_stone = bd.p1_stone
        # cpu gets O
        CPU_stone = bd.p2_stone
        print('Your move!')

        while not bd.done:
            xinput = int(input('X : '))
            yinput = int(input('Y: '))

            legal_move = bd.place_piece(bd, CLI_stone, yinput, xinput)
            if legal_move:
                display_board(bd)
                bd.check_vertical_match(CLI_stone, yinput, xinput)
                # send api w. put move made

            else:
                print('coordinate marked; illegal move')
                pass

    if not coin:
        pass
        # # O/white chosen, CLI goes second
        # CLI_stone = bd.p2_stone
        # # cpu gets X
        # CPU_stone = bd.p1_stone
        # print('Opponent move!')

        # while not bd.done:

        #     bd.auto_move(CPU_stone)
        #     display_board(bd)
        #     bd.check_vertical_match()

        #     xinput = int(input('X : '))
        #     yinput = int(input('Y: '))
        #     legal_move = bd.place_piece(bd, CLI_stone, yinput, xinput)
        #     if legal_move:
        #         display_board(bd)
        #         bd.check_vertical_match(CLI_stone, yinput, xinput)


        #     else:
        #         print('coordinate marked; illegal move')
        #         pass

def core():

    display_board(bd)
    flip()
    turn_cycle()


if __name__ == '__main__':
    '''
    run : core
    key exit : polite
    '''
    try:
        core()

    except KeyboardInterrupt:
        exit()
