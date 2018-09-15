import pytest
import transaction
from ..models.meta import Base
import zope.sqlalchemy
from ..models import get_tm_session


@pytest.fixture(scope='session')
def testapp(request):
    """ Function for setting up a test server/app
    """
    from webtest import TestApp
    from pyramid.config import Configurator

    def add_role_principles(userid, request):
        return request.jwt_claims.get('roles', [])

    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        settings = {
            'sqlalchemy.url': 'postgresql://localhost:5432/Gomoku'
        }
        config = Configurator(settings=settings)
        # config.include('pyramid_jwt')
        config.include('pyramid_restful')
        config.include('..models')
        config.include('Gomokubot.routes')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(bind=engine)

    def tear_down():
        """
            Destroys the server after the test is done
        """
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tear_down)

    return TestApp(app)
