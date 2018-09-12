from .gmk_board import Board
import pytest


@pytest.fixture()
def fresh_game():
    g = Board()
    return g


def test_board_import():
    assert Board


def test_board_instance():
    assert fresh_game()


def test_board_moves_list(fresh_game):
    moves = fresh_game.moves
    assert moves == []


def test_place_piece(fresh_game):
    fresh_game.stone = 1
    fresh_game.place_piece(0, 0)
    assert fresh_game.board[0][0] == fresh_game.stone


def test_placeover_error(fresh_game):
    fresh_game.stone = 1
    fresh_game.place_piece(0, 0)
    assert fresh_game.place_piece(0, 0) == IndexError


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
