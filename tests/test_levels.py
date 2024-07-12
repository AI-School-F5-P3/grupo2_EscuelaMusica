import pytest
from models import Level
from app import db

class TestLevel(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_level(self):
        # Crear un nuevo nivel
        level = Level(name_level='Iniciación')
        db.session.add(level)
        db.session.commit()

        # Verificar que el nivel se creó correctamente
        self.assertEqual(level.name_level, 'Iniciación')

    def test_update_level(self):
        # Crear un nuevo nivel
        level = Level(name_level='Iniciación')
        db.session.add(level)
        db.session.commit()

        # Actualizar el nivel
        level.name_level = 'Medio'
        db.session.commit()

        # Verificar que el nivel se actualizó correctamente
        self.assertEqual(level.name_level, 'Medio')

if __name__ == '__main__':
    pytest.main()