# import uuid


# class Board():
#     def __init__(self):
#         """
#         GMK board class.
#         game id for each instance.
#         moves in order by play
#         """
#         self.game_id = uuid.uuid4().hex

#         # match is CC, CP, or PP
#         self.match = []

#         # Black goes first.
#         # Black 1, white 2.
#         self.stone = 0
#         # remains False until the board is read with victory conditions,
#         # is then turned True and turned into other player.
#         self.done = False

#         # Each move made is appended to list as made.
#         self.moves = []

#         # 2D array. self.board[0][0] to self.board[14][14]
#         self.board = [
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         ]

#     def __str__(self):
#         return(
#             f'game_id: {self.game_id} | '
#             f'done: {self.done} | moves: {self.moves}'
#             )

#     def __repr__(self):
#         return(
#             f'<BOARD | game_id: {self.game_id} | '
#             f'done: {self.done} | moves: {self.moves}'
#             )

#     def place_piece(self, x=0, y=0):
#         # move argument is derived from JSON response in the form of
#         # (X,Y) X: OVER | Y: DOWN
#         if self.board[x][y] == 0:
#             self.board[x][y] = self.stone
#             # after placement, call the Fx that initiates the
#             # sending of me move made to the waiting player.

#         else:
#             print('coordinate marked; illegal move')
#             return IndexError

#     def board_check(self):
#         pass
