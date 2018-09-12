from pyramid.view import notfound_view_config
# from pyramid.response import Response


@notfound_view_config(renderer='json')
def notfound_view(request):
    request.response.status = 404
    # mssg = 'Not Found'
    # mssg += request.json
    # request.response.json = 'Not Found'
    # return Response(json=mssg, content_type="text/plain", status=404)
    return {}
