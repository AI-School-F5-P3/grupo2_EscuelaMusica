import pytest
from app import db, create_app
from app.models import Instrument, Level

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

def test_instrument_model(db_session):
    instrument = Instrument(instrument="Guitar")
    db_session.add(instrument)
    db_session.commit()

    retrieved_instrument = Instrument.query.filter_by(instrument="Guitar").first()
    assert retrieved_instrument is not None
    assert retrieved_instrument.instrument == "Guitar"

def test_instrument_level_relationship(db_session):
    instrument = Instrument(instrument="Piano")
    level = Level(name_level="Intermediate")
    instrument.rel_levels.append(level)
    db_session.add(instrument)
    db_session.add(level)
    db_session.commit()

    retrieved_instrument = Instrument.query.filter_by(instrument="Piano").first()
    assert retrieved_instrument is not None
    assert len(retrieved_instrument.rel_levels) == 1
    assert retrieved_instrument.rel_levels[0].name_level == "Intermediate"