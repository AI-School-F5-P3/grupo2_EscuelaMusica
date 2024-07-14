import  pytest
from models import Instrument
from app import db

class TestInstrument(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///:armonia1:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_instrument(self):
        # Crear un nuevo instrumento
        instrument = Instrument(instrument='Piano')
        db.session.add(instrument)
        db.session.commit()

        # Verificar que el instrumento se creó correctamente
        self.assertEqual(instrument.instrument, 'Piano')

    def test_update_instrument(self):
        # Crear un nuevo instrumento
        instrument = Instrument(instrument='Piano')
        db.session.add(instrument)
        db.session.commit()

        # Actualizar el instrumento
        instrument.instrument = 'Guitarra'
        db.session.commit()

        # Verificar que el instrumento se actualizó correctamente
        self.assertEqual(instrument.instrument, 'Guitarra')

if __name__ == '__main__':
    pytest.main()