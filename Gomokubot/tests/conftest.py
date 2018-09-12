import pytest
import transaction
from ..models.meta import Base
from ..models import get_tm_session

@pytest.fixture(scope='session')
def testapp(request):
    """
        Sets up test server for testing purposes so that we can test
    """

    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        """
            This function returns a Pyramid WSGI Appliaction
        """
        settings = {
            'sqlalchemy.url': pass#PUT test_DB URL HERE
        }

        config = Configurator(settings=setting)
        config.include('pyramid_jwt')
        config.include('pyramid_restful')

        config.include('Gomokubot.models')
        config.include('Gomokubot.routes')
        config.scan()

        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadta.create_all(bing=engine)

    with transaction.manager:
        db_session = get_tm_session(SessionFactory, transaction.manager)

    def tear_down():
        """
            Destroys the server after the test is done
        """
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tear_down)

    return TestApp(app)
