import os
import sys
import json
from textwrap import dedent
import requests
from random import randrange


class Game:
    def __init__(self):
        """ state of a game being persistantly updated
        """
        self.uuid = ''
        self.board = []

    def place_piece(self, stone, x=0, y=0):
        """ updates a board
        """
        if self.board[x][y] == 0:
            self.board[x][y] = stone  # being 1 or 2
            return True
        else:
            return False

    def check_vertical_match(self, stone, y, x):
        """
        Validates the upper and lower stones of given coordinate,
        validates if connected 5
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
            return self._check_dignal_LR_match(stone, y, x)
        print('_check_horizontal_match')
        return True

    def _check_dignal_LR_match(self, stone, y, x):
        """ Validates a diagnal
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
        """ validates a win of diagal
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


def play_again():
    """ asks to play a new game
    """
    print('Would you like to play again? y/n')
    userinput = input()
    if userinput is 'y':
        return False
    else:
        return True


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
    [Y]     ----------------------------------------------------------
        00 | {draw_board_row(bd['gameboard'][0])}

        01 | {draw_board_row(bd['gameboard'][1])}

        02 | {draw_board_row(bd['gameboard'][2])}

        03 | {draw_board_row(bd['gameboard'][3])}

        04 | {draw_board_row(bd['gameboard'][4])}

        05 | {draw_board_row(bd['gameboard'][5])}

        06 | {draw_board_row(bd['gameboard'][6])}

        07 | {draw_board_row(bd['gameboard'][7])}

        08 | {draw_board_row(bd['gameboard'][8])}

        09 | {draw_board_row(bd['gameboard'][9])}

        10 | {draw_board_row(bd['gameboard'][10])}

        11 | {draw_board_row(bd['gameboard'][11])}

        12 | {draw_board_row(bd['gameboard'][12])}

        13 | {draw_board_row(bd['gameboard'][13])}

        14 | {draw_board_row(bd['gameboard'][14])}

              00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14  [X]
             ----------------------------------------------------------
    ''')


def exit():
    '''
    exits the app
    '''
    print(dedent('''
        EXIT PHRASE
    '''))
    sys.exit()


def flip():
    """ Decides if user goes first/second
    """
    num = randrange(0, 10)
    if num % 2 == 0:
        return 1
    else:
        return 2


def validate_opponent(bd, response):
    """ validates a opponents coordinates
    """
    # import pdb; pdb.set_trace()
    data = json.loads(response)
    # import pdb; pdb.set_trace()
    if data['finished']:
        print('Computer WIN, you loose')
        return True
    yaxis = data['Y']
    xaxis = data['X']
    if bd['stone'] == 1:
        bd['gameboard'][yaxis][xaxis] = 2
    else:
        bd['gameboard'][yaxis][xaxis] = 1
    return False


def send_json(bd, xaxis, yaxis):
    """ Sends json to server PUT
    """
    # Deployed AWS (Production)
    url = 'http://ec2-18-218-190-194.us-east-2.compute.amazonaws.com/api/v1/board/1'

    # Local (Development)
    # url = 'http://localhost:6543/api/v1/board/1'
    update = {'uuid': bd['uuid'], 'X': str(xaxis), 'Y': str(yaxis), 'stone': str(bd['stone'])}
    send_info = json.dumps(update)
    return requests.put(url, data=send_info)


def validate_usermove(bd, xaxis, yaxis):
    """ validates a move for a coordinate
    """
    current_game = Game()
    current_game.board = bd['gameboard']
    return current_game.check_vertical_match(bd['stone'], yaxis, xaxis)


def userplay(bd):
    """ Submit user coordinate and validates it
    """
    while True:
        print('Your move!')
        xinput = int(input('X : '))
        yinput = int(input('Y: '))
        current_game = Game()
        current_game.board = bd['gameboard']
        legal_move = current_game.place_piece(bd['stone'], yinput, xinput)
        cls()
        if legal_move:
            return (xinput, yinput)
        display_board(bd)
        print('coordinate marked; illegal move')


def new_game():
    """ Initiates a new game and sends POST request to DB to create a new data set
    """
    # Deployed AWS (Production)
    url = 'http://ec2-18-218-190-194.us-east-2.compute.amazonaws.com/api/v1/board'

    # Local (Development)
    # url = 'http://localhost:6543/api/v1/board'

    response = requests.post(url)
    if response.status_code == 201:
        bd = json.loads(response.text)
        return bd
    else:
        print(response.json)


def cls():
    """ clears Console during gameplay
    """
    os.system('cls' if os.name=='nt' else 'clear')


def play_game():
    """ entire process of playing game
    """
    session = True
    while session:
        bd = new_game()
        bd['stone'] = flip()
        single_game = True

        while single_game:
            display_board(bd)
            xaxis, yaxis = userplay(bd)
            if validate_usermove(bd, xaxis, yaxis):
                display_board(bd)
                print('You WIN!!!!')
                single_game = False
            else:
                response = send_json(bd, xaxis, yaxis)
                # import pdb; pdb.set_trace()
                if response.status_code != 200:
                    print('API update error')
                else:
                    if validate_opponent(bd, response.text):
                        single_game = False

        exit_session = play_again()
        if exit_session:
            session = False


if __name__ == '__main__':
    '''
    run : core
    key exit : polite
    '''
    try:
        play_game()

    except KeyboardInterrupt:
        exit()
