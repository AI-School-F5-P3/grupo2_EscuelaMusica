import pytest
from app.models import Level, Instrument

def test_create_level(init_database):
    """
    Prueba la creación de un nuevo nivel.
    """
    with init_database.app.app_context():
        # Crear un nuevo nivel
        level = Level(name_level="Intermediate")
        init_database.session.add(level)
        init_database.session.commit()

        # Recuperar el nivel de la base de datos
        retrieved_level = Level.query.filter_by(name_level="Intermediate").first()

        # Verificar que el nivel se creó correctamente
        assert retrieved_level is not None
        assert retrieved_level.name_level == "Intermediate"

        # Limpiar: eliminar el nivel creado
        init_database.session.delete(retrieved_level)
        init_database.session.commit()

def test_level_instrument_relationship(init_database):
    """
    Prueba la relación entre niveles e instrumentos.
    """
    with init_database.app.app_context():
        # Crear un nuevo nivel y un nuevo instrumento
        level = Level(name_level="Advanced")
        instrument = Instrument(instrument="Saxophone")

        # Establecer la relación entre el nivel y el instrumento
        level.back_levels.append(instrument)

        # Agregar y guardar en la base de datos
        init_database.session.add(level)
        init_database.session.add(instrument)
        init_database.session.commit()

        # Recuperar el nivel de la base de datos
        retrieved_level = Level.query.filter_by(name_level="Advanced").first()

        # Verificar la relación entre el nivel y el instrumento
        assert retrieved_level is not None
        assert len(retrieved_level.back_levels) == 1
        assert retrieved_level.back_levels[0].instrument == "Saxophone"

        # Limpiar: eliminar el nivel y el instrumento creados
        init_database.session.delete(level)
        init_database.session.delete(instrument)
        init_database.session.commit()

def test_update_level(init_database):
    """
    Prueba la actualización de un nivel existente.
    """
    with init_database.app.app_context():
        # Crear un nuevo nivel
        level = Level(name_level="Beginner")
        init_database.session.add(level)
        init_database.session.commit()

        # Actualizar el nombre del nivel
        level.name_level = "Novice"
        init_database.session.commit()

        # Recuperar el nivel actualizado
        updated_level = Level.query.filter_by(name_level="Novice").first()

        # Verificar que el nivel se actualizó correctamente
        assert updated_level is not None
        assert updated_level.name_level == "Novice"

        # Limpiar: eliminar el nivel creado
        init_database.session.delete(updated_level)
        init_database.session.commit()

def test_delete_level(init_database):
    """
    Prueba la eliminación de un nivel.
    """
    with init_database.app.app_context():
        # Crear un nuevo nivel
        level = Level(name_level="Expert")
        init_database.session.add(level)
        init_database.session.commit()

        # Guardar el ID del nivel
        level_id = level.id_level

        # Eliminar el nivel
        init_database.session.delete(level)
        init_database.session.commit()

        # Intentar recuperar el nivel eliminado
        deleted_level = Level.query.get(level_id)

        # Verificar que el nivel se eliminó correctamente
        assert deleted_level is None
