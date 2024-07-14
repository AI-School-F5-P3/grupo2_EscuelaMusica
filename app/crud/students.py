<<<<<<< HEAD
import logging
from app.models import Student
from app.schemas import student_schema, students_schema
from app import db

# Configura el nivel de registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_student(data):
    try:
        new_student = Student(**data)
        db.session.add(new_student)
        db.session.commit()
        logging.info(f"Estudiante agregado: {new_student}")
        return student_schema.jsonify(new_student)
    except Exception as e:
        logging.error(f"Error al agregar estudiante: {e}")
        return "Error adding student", 500

def get_all_students():
    try:
        students = Student.query.all()
        logging.info(f"Se obtuvieron {len(students)} estudiantes")
        return students_schema.dump(students)
    except Exception as e:
        logging.error(f"Error al obtener estudiantes: {e}")
        return "Error fetching students", 500

def get_student_by_id(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        logging.info(f"Se obtuvo el estudiante: {student}")
        return student_schema.jsonify(student)
    except Exception as e:
        logging.error(f"Error al obtener el estudiante por ID: {e}")
        return "Error fetching student", 404

def update_student(student_id, data):
    try:
        student = Student.query.get_or_404(student_id)
        for key, value in data.items():
            setattr(student, key, value)
        db.session.commit()
        logging.info(f"Estudiante actualizado: {student}")
        return student_schema.jsonify(student)
    except Exception as e:
        logging.error(f"Error al actualizar el estudiante: {e}")
        return "Error updating student", 500

def delete_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        logging.info(f"Estudiante eliminado: {student}")
        return student_schema.jsonify(student)
    except Exception as e:
        logging.error(f"Error al eliminar el estudiante: {e}")
        return "Error deleting student", 500
=======
import logging
from app.models import Level
from app.schemas import level_schema, levels_schema
from app import db

# Configura el nivel de registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_level(data):
    try:
        new_level = Level(**data)
        db.session.add(new_level)
        db.session.commit()
        logging.info(f"Nivel agregado: {new_level}")
        return level_schema.jsonify(new_level)
    except Exception as e:
        logging.error(f"Error al agregar nivel: {e}")
        return "Error adding level", 500

def get_all_levels():
    try:
        levels = Level.query.all()
        logging.info(f"Se obtuvieron {len(levels)} niveles")
        return levels_schema.dump(levels)
    except Exception as e:
        logging.error(f"Error al obtener niveles: {e}")
        return "Error fetching levels", 500

def get_level_by_id(level_id):
    try:
        level = Level.query.get_or_404(level_id)
        logging.info(f"Se obtuvo el nivel: {level}")
        return level_schema.jsonify(level)
    except Exception as e:
        logging.error(f"Error al obtener el nivel por ID: {e}")
        return "Error fetching level", 404

def update_level(level_id, data):
    try:
        level = Level.query.get_or_404(level_id)
        for key, value in data.items():
            setattr(level, key, value)
        db.session.commit()
        logging.info(f"Nivel actualizado: {level}")
        return level_schema.jsonify(level)
    except Exception as e:
        logging.error(f"Error al actualizar el nivel: {e}")
        return "Error updating level", 500

def delete_level(level_id):
    try:
        level = Level.query.get_or_404(level_id)
        db.session.delete(level)
        db.session.commit()
        logging.info(f"Nivel eliminado: {level}")
        return level_schema.jsonify(level)
    except Exception as e:
        logging.error(f"Error al eliminar el nivel: {e}")
        return "Error deleting level", 500
>>>>>>> Jaanh
