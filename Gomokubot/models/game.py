class Game:
    def __init__(self, board=[
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
        ]):
        """
        GMK board class.
        game id for each instance.
        moves in order by play
        """
        # self.game_id = str(uuid4())

        # remains False until the board is read with victory conditions,
        # is then turned True and turned into other player.
        self.done = False

        self.p1_stone = '1'
        self.p2_stone = '2'

        # Each move made is appended to list as made.
        self.moves = []

        # 2D array. self.board[0][0] to self.board[14][14]
        self.board = board

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

    def auto_move(self, stone):

        """
        IN: Board.board
        OUT: self.place_piece(x, y)
        """
        deciding = True
        while deciding:
            x = int(randrange(0, 15))
            y = int(randrange(0, 15))

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
