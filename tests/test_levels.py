import pytest
from app import db, create_app
from app.models import Level

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db_session(app):
    with app.app_context():
        db.create_all()
        yield db.session
        db.session.remove()
        db.drop_all()

def test_level_model(db_session):
    level = Level(name_level="Intermediate")
    db_session.add(level)
    db_session.commit()

    retrieved_level = Level.query.filter_by(name_level="Intermediate").first()
    assert retrieved_level is not None
    assert retrieved_level.name_level == "Intermediate"