from pyramid_restful.routers import ViewSetRouter
from .views import BoardAPIView


def includeme(config):
    """ Setup Routes
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    router = ViewSetRouter(config, trailing_slash=False)
    router.register('api/v1/board', BoardAPIView, 'board')
