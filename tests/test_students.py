import pytest
from models import Student
from app import db

class TestStudent(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_student(self):
        # Crear un nuevo estudiante
        student = Student(first_name='John', last_name='Doe', age=25, phone='1234567890', email='john.doe@example.com')
        db.session.add(student)
        db.session.commit()

        # Verificar que el estudiante se creó correctamente
        self.assertEqual(student.first_name, 'John')
        self.assertEqual(student.last_name, 'Doe')
        self.assertEqual(student.age, 25)
        self.assertEqual(student.phone, '1234567890')
        self.assertEqual(student.email, 'john.doe@example.com')

    def test_update_student(self):
        # Crear un nuevo estudiante
        student = Student(first_name='John', last_name='Doe', age=25, phone='1234567890', email='john.doe@example.com')
        db.session.add(student)
        db.session.commit()

        # Actualizar el estudiante
        student.first_name = 'Jane'
        student.last_name = 'Doe'
        student.age = 30
        student.phone = '0987654321'
        student.email = 'jane.doe@example.com'
        db.session.commit()

        # Verificar que el estudiante se actualizó correctamente
        self.assertEqual(student.first_name, 'Jane')
        self.assertEqual(student.last_name, 'Doe')
        self.assertEqual(student.age, 30)
        self.assertEqual(student.phone, '0987654321')
        self.assertEqual(student.email, 'jane.doe@example.com')

if __name__ == '__main__':
    pytest.main()