from .gmk_board import Board
from .gmk_board import DBBoard
import pytest


@pytest.fixture()
def fresh_game():
    """New board instance, no stones.
    """
    g = Board()
    return g


@pytest.fixture()
def one_board():
    """Board of stones.
    """
    g = Board()
    g.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
    return g


@pytest.fixture()
def win_board():
    """Board of stones in winning combinations
    in all directions from each corner.
    """
    g = Board()
    g.board = [
            [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        ]
    return g


@pytest.fixture()
def DBB():
    """Instantiation of the DBBoard class for DB storage.
    """
    DBB = DBBoard()
    return DBB


def test_board_import():
    """Board constructor class import.
    """
    assert Board


def test_board_instance():
    """Board instantiation.
    """
    assert fresh_game()


def test_auto_move_1(fresh_game):
    """Board class method for random black stone placement.
    """
    assert fresh_game.auto_move(fresh_game.p1_stone)


def test_auto_move_2(fresh_game):
    """Board class method for random white stone placement.
    """
    assert fresh_game.auto_move(fresh_game.p2_stone)


def test_place_piece_1(fresh_game):
    """Board class method for selective black stone placement.
    """
    fresh_game.place_piece(fresh_game.p1_stone, 0, 0)
    assert fresh_game.place_piece(
        fresh_game.p1_stone, 0, 0) is False


def test_place_piece_2(fresh_game):
    """Board class method for selective white stone placement.
    """
    fresh_game.place_piece(fresh_game.p2_stone, 0, 0)
    assert fresh_game.place_piece(
        fresh_game.p2_stone, 0, 0) is False


def test_win_board_assignment(one_board):
    """Verification of the board set.
    """
    assert one_board.board == [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]


def test_one_board_is_board_instance(one_board):
    """Verificaion that the board instance is an instance of Board.
    """
    assert isinstance(one_board, Board)


def test_matching_method_presence(one_board):
    """Check method access.
    """
    assert one_board.check_vertical_match


def test_vertical_1(one_board):
    """Check cascade checks with vertical combo.
    """
    assert one_board.check_vertical_match(1, 7, 7)


def test_horizontal_2(win_board):
    """Check cascare checks with horizontal combo.
    """
    assert win_board.check_vertical_match(2, 0, 0)


def test_vertical_2(win_board):
    """Check cascade checks with vertical combo.
    """
    assert win_board.check_vertical_match(2, 0, 14)


def test_diagonal_A_2(win_board):
    """Check cascade checks with diagonal combo.
    """
    assert win_board.check_vertical_match(2, 14, 14)


def test_diagonal_B_2(win_board):
    """Check cascade checks with diagonal combo.
    """
    assert win_board.check_vertical_match(2, 14, 0)


def test_verifor_center_complete(win_board):
    """Verify position for center combo completion.
    """
    assert win_board.board[11][0] == 2
    assert win_board.board[12][0] == 2
    assert win_board.board[13][0] == 2


def test_center_complete_vert(win_board):
    """Center combo completion testing.
    """
    assert win_board.check_vertical_match(2, 12, 0)


def test_center_complete_horizontal(win_board):
    """Center combo completion testing.
    """
    assert win_board._check_horizontal_match


def test_center_complete_diagonal_LR(win_board):
    """Center combo completion testing.
    """
    assert win_board._check_horizontal_match(2, 13, 13)


def test_center_complete_diagonal_RL(win_board):
    """Center combo completion testing.
    """
    assert win_board._check_horizontal_match(2, 1, 13)


def test_import_DBBoard():
    """Import of the DBBoard class for DB translation.
    """
    assert DBBoard
