import json
from uuid import uuid4
uuid = uuid4()


def test_home_route(testapp):
    """
        Ensure the home route returns the right status code
    """
    response = testapp.get('/')
    assert response.status_code == 200


def test_bad_route(testapp):
    """
        Ensure that a 404 is returned when hitting a nonexistant route
    """
    response = testapp.get('/home/etc/v1/api/keys/id')
    assert response.status_code == 404


def test_create_board(testapp):
    """
        Ensure that a board is created when hitting the board route
    """
    response = testapp.post(f'api/v1/board/{uuid}')
    assert response.status_code == 201


def test_get_specific_boards(testapp):
    """
        Ensure that a board can be retreived after hitting the board route
    """
    response = testapp.get(f'api/v1/board/{uuid}')
    assert response.status_code == 200


def test_get_all_boards(testapp):
    response = testapp.get(f'api/v1/board')
    assert response.status_code == 200


def test_update_board(testapp):
    response = testapp.put(f'api/v1/board/{uuid}?x=3&y=3&stone=1')
    assert response.status_code == 200
