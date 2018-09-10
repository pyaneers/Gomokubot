from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home_view(request):
    message = 'hello world'
    return Response(body=message, content_type='application/json', status=200)
