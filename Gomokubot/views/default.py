from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home_view(request):

    return Response(body="Hello World", content_type='text/html', status=200)
