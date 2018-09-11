from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class BoardAPIView(APIViewSet):
    """ Create, view, update, list all
    """
    def create(self, request):
        """ Create a new Gomoku Game
        """
        return Response(json='Fake Create', status=201)

    def update(self, request, id=None):
        """ Send a new move on a given game
        """
        if not id:
            return Response(json='Update Game Not Found', status=404)
        mssg = f'Fake sent a move to game {id}'
        return Response(json=mssg, status=200)

    def retrieve(self, request, id=None):
        """ Get one Gomoku Game with given id
        """
        if not id:
            return Response(json='Not Found', status=404)
        mssg = f'Looking at game {id}'
        # if move:
        #     mssg += f' on move {move}'

        return Response(json=mssg, status=200)

    def list(self, request):
        """ List all current running games
        """
        return Response(json='Fake list active games', status=200)
