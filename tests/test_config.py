import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    # Create a test client using the Flask application configured for testing
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table(s)
    db.create_all()

    # Insert user data
    # user1 = User(username='testuser', email='testuser@example.com')  # Example of adding data
    # db.session.add(user1)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
