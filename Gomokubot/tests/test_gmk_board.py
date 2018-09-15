from ..models.gmk_board import Board
import pytest


@pytest.fixture()
def fresh_game():
    g = Board()
    return g


def test_board_import():
    """ tests for Board class
    """
    assert Board()


def test_board_instance(fresh_game):
    """ test for Board instance
    """
    assert isinstance(fresh_game, Board)


def test_board_done(fresh_game):
    """ test for Board properties done
    """
    done = fresh_game.done
    assert done == False


def test_board_finished(fresh_game):
    """ test for Board properties finished
    """
    finished = fresh_game.finished
    assert finished == False


def test_board_board(fresh_game):
    """ test for Board properties board
    """
    done = [
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
    assert fresh_game.board == done


def test_for_automove(fresh_game):
    """ tests for return of random two digits
    """
    y, x = fresh_game.auto_move(1)
    assert x
    assert y


def test_place_piece(fresh_game):
    """ test for board update
    """
    assert fresh_game.place_piece(1, 0, 0) == True


def test_win_validation(fresh_game):
    """ test for win validation, expect no win
    """
    expect = False
    assert fresh_game.check_vertical_match(1, 1, 5) == expect


def test_vertical_win(fresh_game):
    """ test for return True when vertical win
    """
    fresh_game.board[0][0] = 1
    fresh_game.board[1][0] = 1
    fresh_game.board[2][0] = 1
    fresh_game.board[4][0] = 1
    fresh_game.board[5][0] = 1
    actual = fresh_game.check_vertical_match(1, 3, 0)
    assert actual is True


def test_horizontal_win(fresh_game):
    """ test for return True when horizontal win
    """
    fresh_game.board[0][4] = 1
    fresh_game.board[0][3] = 1
    fresh_game.board[0][2] = 1
    fresh_game.board[0][1] = 1
    assert fresh_game.check_vertical_match(1, 0, 5) == True


def test_diagnal_win_1(fresh_game):
    """ test for return True when diagnal win 1
    """
    fresh_game.board[0][0] = 1
    fresh_game.board[1][1] = 1
    fresh_game.board[2][2] = 1
    fresh_game.board[3][3] = 1
    assert fresh_game.check_vertical_match(1, 4, 4) == True


def test_diagnal_win_2(fresh_game):
    """ test for return True when diagnal win 2
    """
    fresh_game.board[5][5] = 1
    fresh_game.board[4][6] = 1
    fresh_game.board[3][7] = 1
    fresh_game.board[2][8] = 1
    assert fresh_game.check_vertical_match(1, 1, 9) == True

