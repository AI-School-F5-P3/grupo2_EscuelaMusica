import pytest
from app import db, create_app
from app.models import Teacher, Instrument, TeacherInstrument

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

def test_teacher_instrument_association(db_session):
    teacher = Teacher(name_teacher="Alice", last_name="Johnson")
    instrument = Instrument(instrument="Violin")
    db_session.add(teacher)
    db_session.add(instrument)
    db_session.commit()

    teacher_instrument = TeacherInstrument(id_teacher=teacher.id_teacher, id_instrument=instrument.id_instrument)
    db_session.add(teacher_instrument)
    db_session.commit()

    retrieved_teacher_instrument = TeacherInstrument.query.filter_by(id_teacher=teacher.id_teacher, id_instrument=instrument.id_instrument).first()
    assert retrieved_teacher_instrument is not None
    assert retrieved_teacher_instrument.id_teacher == teacher.id_teacher
    assert retrieved_teacher_instrument.id_instrument == instrument.id_instrument