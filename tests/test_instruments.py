import pytest
from app.models import Instrument, Level

def test_create_instrument(init_database):
    """
    Prueba la creación de un nuevo instrumento.
    """
    with init_database.app.app_context():
        # Crear un nuevo instrumento
        instrument = Instrument(instrument="Piano")
        init_database.session.add(instrument)
        init_database.session.commit()

        # Recuperar el instrumento de la base de datos
        retrieved_instrument = Instrument.query.filter_by(instrument="Piano").first()

        # Verificar que el instrumento se creó correctamente
        assert retrieved_instrument is not None
        assert retrieved_instrument.instrument == "Piano"

        # Limpiar: eliminar el instrumento creado
        init_database.session.delete(retrieved_instrument)
        init_database.session.commit()

def test_instrument_level_relationship(init_database):
    """
    Prueba la relación entre instrumentos y niveles.
    """
    with init_database.app.app_context():
        # Crear un nuevo instrumento y un nuevo nivel
        instrument = Instrument(instrument="Violin")
        level = Level(name_level="Beginner")
