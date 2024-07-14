import pytest
from app import create_app, db
from app.models import Teacher

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

def test_create_teacher(init_database):
    with init_database.app.app_context():
        teacher = Teacher(name_teacher='Maria Garcia')
        db.session.add(teacher)
        db.session.commit()

        assert teacher.id_teacher is not None
        assert teacher.name_teacher == 'Maria Garcia'

def test_update_teacher(init_database):
    with init_database.app.app_context():
        teacher = Teacher(name_teacher='John Smith')
        db.session.add(teacher)
        db.session.commit()

        teacher.name_teacher = 'John A. Smith'
        db.session.commit()

        updated_teacher = Teacher.query.get(teacher.id_teacher)
        assert updated_teacher.name_teacher == 'John A. Smith'

def test_delete_teacher(init_database):
    with init_database.app.app_context():
        teacher = Teacher(name_teacher='Emily Brown')
        db.session.add(teacher)
        db.session.commit()

        db.session.delete(teacher)
        db.session.commit()

        deleted_teacher = Teacher.query.get(teacher.id_teacher)
        assert deleted_teacher is None
