from flask import app
import pytest
from app.models import Enrollment, Student, Level, Instrument, Teacher
from app import db

class TestEnrollment(pytest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos para las pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_enrollment(self):
        # Crear un estudiante, nivel, instrumento y profesor
        student = Student(first_name='John', last_name='Doe', age=25, phone='1234567890', email='john.doe@example.com')
        level = Level(name_level='Iniciación')
        instrument = Instrument(instrument='Piano')
        teacher = Teacher(name_teacher='Maria Gomez')
        db.session.add_all([student, level, instrument, teacher])
        db.session.commit()

        # Crear una nueva inscripción
        enrollment = Enrollment(
            id_student=student.id_student,
            id_level=level.id_level,
            id_instrument=instrument.id_instrument,
            id_teacher=teacher.id_teacher,
            base_price=35.0,
            final_price=35.0,
            family_discount=False
        )
        db.session.add(enrollment)
        db.session.commit()

        # Verificar que la inscripción se creó correctamente
        self.assertEqual(enrollment.id_student, student.id_student)
        self.assertEqual(enrollment.id_level, level.id_level)
        self.assertEqual(enrollment.id_instrument, instrument.id_instrument)
        self.assertEqual(enrollment.id_teacher, teacher.id_teacher)
        self.assertEqual(enrollment.base_price, 35.0)
        self.assertEqual(enrollment.final_price, 35.0)
        self.assertFalse(enrollment.family_discount)

    def test_update_enrollment(self):
        # Crear una nueva inscripción
        enrollment = Enrollment(
            id_student=1,
            id_level=1,
            id_instrument=1,
            id_teacher=1,
            base_price=35.0,
            final_price=35.0,
            family_discount=False
        )
        db.session.add(enrollment)
        db.session.commit()

        # Actualizar la inscripción
        enrollment.final_price = 30.0
        enrollment.family_discount = True
        db.session.commit()

        # Verificar que la inscripción se actualizó correctamente
        self.assertEqual(enrollment.final_price, 30.0)
        self.assertTrue(enrollment.family_discount)

if __name__ == '__main__':
    pytest.main()