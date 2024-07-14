import pytest
from app import create_app, db
from app.models import Student

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

def test_create_student(init_database):
    with init_database.app.app_context():
        student = Student(
            first_name='John',
            last_name='Doe',
            age=20,
            phone='1234567890',
            email='john.doe@example.com'
        )
        db.session.add(student)
        db.session.commit()

        assert student.id_student is not None
        assert student.first_name == 'John'
        assert student.last_name == 'Doe'
        assert student.age == 20
        assert student.phone == '1234567890'
        assert student.email == 'john.doe@example.com'

def test_update_student(init_database):
    with init_database.app.app_context():
        student = Student(
            first_name='Jane',
            last_name='Smith',
            age=25,
            phone='9876543210',
            email='jane.smith@example.com'
        )
        db.session.add(student)
        db.session.commit()

        student.age = 26
        student.phone = '1122334455'
        db.session.commit()

        updated_student = Student.query.get(student.id_student)
        assert updated_student.age == 26
        assert updated_student.phone == '1122334455'

def test_delete_student(init_database):
    with init_database.app.app_context():
        student = Student(
            first_name='Alice',
            last_name='Johnson',
            age=30,
            phone='5556667777',
            email='alice.johnson@example.com'
        )
        db.session.add(student)
        db.session.commit()

        db.session.delete(student)
        db.session.commit()

        deleted_student = Student.query.get(student.id_student)
        assert deleted_student is None
