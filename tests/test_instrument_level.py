import pytest
from app import db, create_app
from app.models import Instrument, Level, InstrumentLevel

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

def test_instrument_level_association(db_session):
    instrument = Instrument(instrument="Saxophone")
    level = Level(name_level="Advanced")
    db_session.add(instrument)
    db_session.add(level)
    db_session.commit()

    instrument_level = InstrumentLevel(id_instrument=instrument.id_instrument, id_level=level.id_level)
    db_session.add(instrument_level)
    db_session.commit()

    retrieved_instrument_level = InstrumentLevel.query.filter_by(id_instrument=instrument.id_instrument, id_level=level.id_level).first()
    assert retrieved_instrument_level is not None
    assert retrieved_instrument_level.id_instrument == instrument.id_instrument
    assert retrieved_instrument_level.id_level == level.id_level