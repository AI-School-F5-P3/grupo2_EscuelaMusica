import os
import pytest
from app import create_app, db
from app.models import Student, Teacher, Instrument, Level, Enrollment

@pytest.fixture(scope='session')
def app():
    """Create and configure a new app instance for each test session."""
    # Configurar la aplicación para pruebas
    app = create_app('testing')
    
    # Asegurarse de que estamos usando la base de datos de prueba
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    
    # Crear un contexto de aplicación
    with app.app_context():
        # Crear todas las tablas en la base de datos
        db.create_all()
        
        yield app
        
        # Limpiar la base de datos después de todas las pruebas
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture(scope='function')
def init_database(app):
    """Initialize database for each test function."""
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def sample_data(init_database):
    """Create sample data for tests."""
    student = Student(first_name="Test", last_name="Student", age=20, phone="1234567890", email="test@example.com")
    teacher = Teacher(name_teacher="Test Teacher")
    instrument = Instrument(instrument="Test Instrument")
    level = Level(name_level="Test Level")
    enrollment = Enrollment(
        id_student=1,
        id_level=1,
        id_instrument=1,
        id_teacher=1,
        base_price=100.0,
        final_price=100.0,
        family_discount=False
    )
    
    init_database.session.add_all([student, teacher, instrument, level, enrollment])
    init_database.session.commit()
    
    yield {
        'student': student,
        'teacher': teacher,
        'instrument': instrument,
        'level': level,
        'enrollment': enrollment
    }
    
    # Limpiar los datos después de cada prueba
    init_database.session.rollback()
