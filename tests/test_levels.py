import pytest
from app import create_app, db
from app.models import Level

<<<<<<< HEAD
class TestLevel(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///:armonia1:'
=======
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
>>>>>>> Jaanh
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

def test_create_level(init_database):
    with init_database.app.app_context():
        level = Level(name_level='Beginner')
        db.session.add(level)
        db.session.commit()

        assert level.id_level is not None
        assert level.name_level == 'Beginner'

def test_update_level(init_database):
    with init_database.app.app_context():
        level = Level(name_level='Intermediate')
        db.session.add(level)
        db.session.commit()

        level.name_level = 'Advanced Intermediate'
        db.session.commit()

        updated_level = Level.query.get(level.id_level)
        assert updated_level.name_level == 'Advanced Intermediate'

def test_delete_level(init_database):
    with init_database.app.app_context():
        level = Level(name_level='Advanced')
        db.session.add(level)
        db.session.commit()

        db.session.delete(level)
        db.session.commit()

        deleted_level = Level.query.get(level.id_level)
        assert deleted_level is None
