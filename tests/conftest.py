import pytest
from app import create_app, db
from app.models import Student, Teacher, Instrument, Level, PriceInstrument, Enrollment
import os

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    
    # Asegúrate de que estamos usando SQLite para las pruebas
    assert 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def session(app):
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        options = dict(bind=connection, binds={})
        sess = db.create_scoped_session(options=options)
        db.session = sess
        yield sess
        transaction.rollback()
        connection.close()
        sess.remove()

@pytest.fixture(scope='function')
def init_database(session):
    # Crear datos iniciales para las pruebas
    price_pack = PriceInstrument(pack="Test_Pack", pack_price=50.0)
    session.add(price_pack)
    session.commit()

    instrument = Instrument(instrument="Guitar", pack_id=price_pack.id_pack)
    session.add(instrument)

    level = Level(name_level="Beginner")
    session.add(level)

    teacher = Teacher(name_teacher="John", last_name="Doe", telphone="123-456-7890", email="john.doe@example.com")
    session.add(teacher)

    student = Student(first_name="Jane", last_name="Smith", age=20, phone="987-654-3210", email="jane.smith@example.com")
    session.add(student)

    enrollment = Enrollment(id_student=1, id_instrument=1, enrollment_date="2023-01-01", name_student="Jane", lastname_student="Smith", family=False)
    session.add(enrollment)

    session.commit()

    yield session

@pytest.fixture(scope='function')
def test_client(app, init_database):
    return app.test_client()
