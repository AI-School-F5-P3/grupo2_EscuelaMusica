import logging
from db import Session
from models import Student

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_student(first_name, last_name, age, phone, email):
    logging.info(f'Creando estudiante: {first_name} {last_name}')
    new_student = Student(first_name=first_name, last_name=last_name, age=age, phone=phone, email=email)
    db_session.add(new_student)
    db_session.commit()
    logging.info(f'Estudiante creado exitosamente: {first_name} {last_name}')
    return new_student

def get_student_by_id(student_id):
    logging.info(f'Recuperando estudiante con ID: {student_id}')
    student = db_session.query(Student).filter_by(id_student=student_id).first()
    if student:
        logging.info(f'Estudiante recuperado: {student.first_name} {student.last_name}')
    else:
        logging.warning(f'Estudiante con ID {student_id} no encontrado')
    return student

def update_student(student_id, new_data):
    logging.info(f'Actualizando estudiante con ID: {student_id}')
    student = db_session.query(Student).filter_by(id_student=student_id).first()
    if student:
        logging.debug(f'Actualizando detalles del estudiante: {student.first_name} {student.last_name} -> {new_data}')
        for key, value in new_data.items():
            setattr(student, key, value)
        db_session.commit()
        logging.info(f'Estudiante actualizado exitosamente: {student.first_name} {student.last_name}')
    else:
        logging.warning(f'Estudiante con ID {student_id} no encontrado')
    return student

def delete_student(student_id):
    logging.info(f'Borrando estudiante con ID: {student_id}')
    student = db_session.query(Student).filter_by(id_student=student_id).first()
    if student:
        logging.info(f'Borrando estudiante: {student.first_name} {student.last_name}')
        db_session.delete(student)
        db_session.commit()
        logging.info(f'Estudiante borrado exitosamente: {student.first_name} {student.last_name}')
    else:
        logging.warning(f'Estudiante con ID {student_id} no encontrado')
    return student

def get_all_students():
    logging.info('Recuperando todos los estudiantes')
    students = db_session.query(Student).all()
    logging.info(f'Se han recuperado {len(students)} estudiantes')
    return students
