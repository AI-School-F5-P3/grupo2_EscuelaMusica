import pytest
from app.models import Student

def test_create_student(init_database):
    """
    Prueba la creación de un nuevo estudiante.
    """
    with init_database.app.app_context():
        # Crear un nuevo estudiante
        student = Student(
            first_name="John",
            last_name="Doe",
            age=20,
            phone="1234567890",
            email="john.doe@example.com"
        )
        init_database.session.add(student)
        init_database.session.commit()

        # Recuperar el estudiante de la base de datos
        retrieved_student = Student.query.filter_by(email="john.doe@example.com").first()

        # Verificar que el estudiante se creó correctamente
        assert retrieved_student is not None
        assert retrieved_student.first_name == "John"
        assert retrieved_student.last_name == "Doe"
        assert retrieved_student.age == 20
        assert retrieved_student.phone == "1234567890"
        assert retrieved_student.email == "john.doe@example.com"

        # Limpiar: eliminar el estudiante creado
        init_database.session.delete(retrieved_student)
        init_database.session.commit()

def test_update_student(init_database):
    """
    Prueba la actualización de un estudiante existente.
    """
    with init_database.app.app_context():
        # Crear un nuevo estudiante
        student = Student(
            first_name="Jane",
            last_name="Smith",
            age=25,
            phone="9876543210",
            email="jane.smith@example.com"
        )
        init_database.session.add(student)
        init_database.session.commit()

        # Actualizar los datos del estudiante
        student.age = 26
        student.phone = "1122334455"
        init_database.session.commit()

        # Recuperar el estudiante actualizado
        updated_student = Student.query.filter_by(email="jane.smith@example.com").first()

        # Verificar que el estudiante se actualizó correctamente
        assert updated_student is not None
        assert updated_student.age == 26
        assert updated_student.phone == "1122334455"

        # Limpiar: eliminar el estudiante creado
        init_database.session.delete(updated_student)
        init_database.session.commit()

def test_delete_student(init_database):
    """
    Prueba la eliminación de un estudiante.
    """
    with init_database.app.app_context():
        # Crear un nuevo estudiante
        student = Student(
            first_name="Alice",
            last_name="Johnson",
            age=22,
            phone="5555555555",
            email="alice.johnson@example.com"
        )
        init_database.session.add(student)
        init_database.session.commit()

        # Guardar el ID del estudiante
        student_id = student.id_student

        # Eliminar el estudiante
        init_database.session.delete(student)
        init_database.session.commit()

        # Intentar recuperar el estudiante eliminado
        deleted_student = Student.query.get(student_id)

        # Verificar que el estudiante se eliminó correctamente
        assert deleted_student is None

def test_student_unique_email(init_database):
    """
    Prueba que no se pueden crear dos estudiantes con el mismo email.
    """
    with init_database.app.app_context():
        # Crear un estudiante
        student1 = Student(
            first_name="Bob",
            last_name="Brown",
            age=30,
            phone="1231231234",
            email="bob.brown@example.com"
        )
        init_database.session.add(student1)
        init_database.session.commit()

        # Intentar crear otro estudiante con el mismo email
        student2 = Student(
            first_name="Robert",
            last_name="Brown",
            age=31,
            phone="4564564567",
            email="bob.brown@example.com"
        )
        init_database.session.add(student2)

        # Verificar que se lanza una excepción al intentar commitear
        with pytest.raises(Exception):  # Ajusta el tipo de excepción según tu configuración de BD
            init_database.session.commit()

        # Limpiar: eliminar el estudiante creado
        init_database.session.rollback()
        init_database.session.delete(student1)
        init_database.session.commit()

    retrieved_student = Student.query.filter_by(first_name="Test").first()
    assert retrieved_student is not None
    assert retrieved_student.last_name == "Student"
    assert retrieved_student.age == 20
    assert retrieved_student.phone == "1234567890"
    assert retrieved_student.email == "test@test.com"

    db.session.delete(retrieved_student)
    db.session.commit()
