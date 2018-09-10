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

    def _check_vertical_win(self, x, y):
        """ Validates the upper and lower stones of given coordinate, validates if connected 5
        """
        counter = 0
        check_up = False
        check_down = False

        while check_up is False:
            for i in range(y, 0, -1):
                if self.board[x][i] is self.stone:
                    counter += 1
                else:
                    check_up = True

        while check_down is False:
            for e in range(y, 15):
                if self.board[x][e] is self.stone:
                    counter += 1
                else:
                    check_down is True

        if counter < 4:
            return False
        return True

    def _check_horizontal_win(self, x, y):
        """ Validates the left and right sides of stones of given coordinate, validates if connected 5
        """
        counter = 0
        check_left = False
        check_right = False

        while check_left is False:
            for i in range(x, 0, -1):
                if self.board[x][i] is self.stone:
                    counter += 1
                else:
                    check_left = True

        while check_right is False:
            for e in range(x, 15):
                if self.board[x][e] is self.stone:
                    counter += 1
                else:
                    check_right is True

        if counter < 4:
            return False
        return True

    def _check_dignal1_win(self, x, y):
        counter = 0
        check_upperleft = False
        check_lowerright = False

        while check_upperleft is False:
            for i in range(0, x):
                if i + y > 15:
                    check_upperleft = True
                if self.board[x - i][y + i] is self.stone:
                    counter += 1
                else:
                    check_upperleft = True

        while check_lowerright is False:
            for e in range(0, y):
                if e + x > 15:
                    check_lowerright = True
                if self.board[x + e][y - e] is self.stone:
                    counter += 1
                else:
                    check_lowerright is True
        if counter < 4:
            return False
        return True

    def _check_diagnal2_win(self, x, y):
        counter = 0
        check_lowerleft = False
        check_upperright = False

        while check_lowerleft is False:
            for i in range(0, x):
                if i > y:
                    check_lowerleft = True
                if self.board[x - i][y + i] is self.stone:
                    counter += 1
                else:
                    check_lowerleft = True

        while check_upperright is False:
            for e in range(0, x):
                if e > y:
                    check_upperright = True
                if self.board[x + e][y - e] is self.stone:
                    counter += 1
                else:
                    check_lowerleft is True
        if counter < 4:
            return False
        return True

    def _board_check(self, x, y):
        import pdb; pdb.set_trace()
        win = False
        while win is False:
            win = self._check_vertical_win(x, y)
            win = self._check_horizontal_win(x, y)
            win = self._check_dignal1_win(x, y)
            win = self._check_dignal2_win(x, y)
            print(win)
            return win
        print(win)
        return win
