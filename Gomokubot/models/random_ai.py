from random import randrange
class RandomAI():

    def __init__(self, stone=2):
        self.stone = stone
        pass

    def make_move(self, board: list):
        """
            Takes in a 2D list representation of a gomoku board and returns that same board with a legal move made
        """
        while True:
            x: int = int(randrange(0, len(board)))
            y: int = int(randrange(0, len(board[0])))
            if board[x][y] != 0:
                board[x][y] = self.stone
                return board
