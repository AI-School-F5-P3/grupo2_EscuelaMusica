import pytest
from app import create_app, db
from app.models import Instrument

@pytest.fixture(scope='module')
def app():
    app = create_app('testing')
    return app

@pytest.fixture(scope='module')
def test_client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def init_database(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

def test_create_instrument(init_database):
    with init_database.app.app_context():
        instrument = Instrument(instrument='Guitar')
        db.session.add(instrument)
        db.session.commit()

        assert instrument.id_instrument is not None
        assert instrument.instrument == 'Guitar'

def test_update_instrument(init_database):
    with init_database.app.app_context():
        instrument = Instrument(instrument='Piano')
        db.session.add(instrument)
        db.session.commit()

        instrument.instrument = 'Grand Piano'
        db.session.commit()

        updated_instrument = Instrument.query.get(instrument.id_instrument)
        assert updated_instrument.instrument == 'Grand Piano'

def test_delete_instrument(init_database):
    with init_database.app.app_context():
        instrument = Instrument(instrument='Drums')
        db.session.add(instrument)
        db.session.commit()

        db.session.delete(instrument)
        db.session.commit()

        deleted_instrument = Instrument.query.get(instrument.id_instrument)
        assert deleted_instrument is None
