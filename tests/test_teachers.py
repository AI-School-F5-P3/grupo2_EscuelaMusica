import pytest
from app.models import Teacher

def test_create_teacher(init_database):
    """
    Prueba la creación de un nuevo profesor.
    """
    with init_database.app.app_context():
        # Crear un nuevo profesor
        teacher = Teacher(name_teacher="Maria Garcia")
        init_database.session.add(teacher)
        init_database.session.commit()

        # Recuperar el profesor de la base de datos
        retrieved_teacher = Teacher.query.filter_by(name_teacher="Maria Garcia").first()

        # Verificar que el profesor se creó correctamente
        assert retrieved_teacher is not None
        assert retrieved_teacher.name_teacher == "Maria Garcia"

        # Limpiar: eliminar el profesor creado
        init_database.session.delete(retrieved_teacher)
        init_database.session.commit()

def test_update_teacher(init_database):
    """
    Prueba la actualización de un profesor existente.
    """
    with init_database.app.app_context():
        # Crear un nuevo profesor
        teacher = Teacher(name_teacher="John Smith")
        init_database.session.add(teacher)
        init_database.session.commit()

        # Actualizar el nombre del profesor
        teacher.name_teacher = "John A. Smith"
        init_database.session.commit()

        # Recuperar el profesor actualizado
        updated_teacher = Teacher.query.filter_by(name_teacher="John A. Smith").first()

        # Verificar que el profesor se actualizó correctamente
        assert updated_teacher is not None
        assert updated_teacher.name_teacher == "John A. Smith"

        # Limpiar: eliminar el profesor creado
        init_database.session.delete(updated_teacher)
        init_database.session.commit()

def test_delete_teacher(init_database):
    """
    Prueba la eliminación de un profesor.
    """
    with init_database.app.app_context():
        # Crear un nuevo profesor
        teacher = Teacher(name_teacher="Alice Johnson")
        init_database.session.add(teacher)
        init_database.session.commit()

        # Guardar el ID del profesor
        teacher_id = teacher.id_teacher

        # Eliminar el profesor
        init_database.session.delete(teacher)
        init_database.session.commit()

        # Intentar recuperar el profesor eliminado
        deleted_teacher = Teacher.query.get(teacher_id)

        # Verificar que el profesor se eliminó correctamente
        assert deleted_teacher is None

def test_teacher_unique_name(init_database):
    """
    Prueba que no se pueden crear dos profesores con el mismo nombre.
    """
    with init_database.app.app_context():
        # Crear un profesor
        teacher1 = Teacher(name_teacher="Robert Brown")
        init_database.session.add(teacher1)
        init_database.session.commit()

        # Intentar crear otro profesor con el mismo nombre
        teacher2 = Teacher(name_teacher="Robert Brown")
        init_database.session.add(teacher2)

        # Verificar que se lanza una excepción al intentar commitear
        with pytest.raises(Exception):  # Ajusta el tipo de excepción según tu configuración de BD
            init_database.session.commit()

        # Limpiar: eliminar el profesor creado
        init_database.session.rollback()
        init_database.session.delete(teacher1)
        init_database.session.commit()

def test_teacher_with_empty_name(init_database):
    """
    Prueba que no se puede crear un profesor con nombre vacío.
    """
    with init_database.app.app_context():
        # Intentar crear un profesor con nombre vacío
        teacher = Teacher(name_teacher="")
        init_database.session.add(teacher)

        # Verificar que se lanza una excepción al intentar commitear
        with pytest.raises(Exception):  # Ajusta el tipo de excepción según tu validación
            init_database.session.commit()

        # Limpiar
        init_database.session.rollback()
