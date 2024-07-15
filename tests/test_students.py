import pytest
from app import db, create_app
from app.models import Student

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

def test_student_model(db_session):
    student = Student(first_name="John", last_name="Doe", age=20, phone="123-456-7890", email="john@example.com")
    db_session.add(student)
    db_session.commit()

    retrieved_student = Student.query.filter_by(first_name="John").first()
    assert retrieved_student is not None
    assert retrieved_student.last_name == "Doe"
    assert retrieved_student.age == 20
    assert retrieved_student.phone == "123-456-7890"
    assert retrieved_student.email == "john@example.com"