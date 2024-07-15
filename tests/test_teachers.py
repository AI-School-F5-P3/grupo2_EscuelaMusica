import pytest
from app import db, create_app
from app.models import Teacher, Instrument


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

def test_teacher_model(db_session):
    teacher = Teacher(name_teacher="Jane", last_name="Smith", telphone="987-654-3210", email="jane@example.com")
    db_session.add(teacher)
    db_session.commit()

    retrieved_teacher = Teacher.query.filter_by(name_teacher="Jane").first()
    assert retrieved_teacher is not None
    assert retrieved_teacher.last_name == "Smith"
    assert retrieved_teacher.telphone == "987-654-3210"
    assert retrieved_teacher.email == "jane@example.com"

def test_teacher_instrument_relationship(db_session):
    teacher = Teacher(name_teacher="Bob", last_name="Johnson")
    instrument = Instrument(instrument="Piano")
    teacher.rel_instrument.append(instrument)
    db_session.add(teacher)
    db_session.add(instrument)
    db_session.commit()

    retrieved_teacher = Teacher.query.filter_by(name_teacher="Bob").first()
    assert retrieved_teacher is not None
    assert len(retrieved_teacher.rel_instrument) == 1
    assert retrieved_teacher.rel_instrument[0].instrument == "Piano"