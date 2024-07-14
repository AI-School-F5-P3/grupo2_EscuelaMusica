import  pytest
from models import Instrument
from app import db

class TestInstrument(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
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
