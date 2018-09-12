from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home', renderer='json', request_method='GET')
def my_view(request):
    """ This is a home page holding spot
    """
    message = ''' Gomokubot Home Page '''
    return Response(json=message, content_type="text/plain")
