import pytest
from models import Teacher
from app import db

class TestTeacher(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///:armonia1:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_teacher(self):
        # Crear un nuevo profesor
        teacher = Teacher(name_teacher='Maria Gomez')
        db.session.add(teacher)
        db.session.commit()

        # Verificar que el profesor se creó correctamente
        self.assertEqual(teacher.name_teacher, 'Maria Gomez')

    def test_update_teacher(self):
        # Crear un nuevo profesor
        teacher = Teacher(name_teacher='Maria Gomez')
        db.session.add(teacher)
        db.session.commit()

        # Actualizar el profesor
        teacher.name_teacher = 'Juan Perez'
        db.session.commit()

        # Verificar que el profesor se actualizó correctamente
        self.assertEqual(teacher.name_teacher, 'Juan Perez')

if __name__ == '__main__':
    pytest.main()