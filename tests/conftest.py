import pytest
from app import create_app, db
from flask_jwt_extended import create_access_token
import os

@pytest.fixture(scope='module')
def app():
    os.environ['TEST_DATABASE_URL'] = 'sqlite:///test_armonia_utopia.db'
    app = create_app('config.TestingConfig')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope='module')
def init_database(app):
    return db

@pytest.fixture(scope='module')
def auth_header(app):
    with app.app_context():
        # Create a user and generate a token
        token = create_access_token(identity='test_user')
        return {
            'Authorization': f'Bearer {token}'
        }

