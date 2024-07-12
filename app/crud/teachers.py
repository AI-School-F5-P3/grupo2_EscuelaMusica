import logging
from db import Session
from models import Teacher

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_teacher(name_teacher):
    logging.info(f'Creando profesor: {name_teacher}')
    new_teacher = Teacher(name_teacher=name_teacher)
    db_session.add(new_teacher)
    db_session.commit()
    logging.info(f'Profesor creado exitosamente: {name_teacher}')
    return new_teacher

def get_teacher_by_id(teacher_id):
    logging.info(f'Recuperando profesor con ID: {teacher_id}')
    teacher = db_session.query(Teacher).filter_by(id_teacher=teacher_id).first()
    if teacher:
        logging.info(f'Profesor recuperado: {teacher.name_teacher}')
    else:
        logging.warning(f'Profesor con ID {teacher_id} no encontrado')
    return teacher

def update_teacher(teacher_id, new_data):
    logging.info(f'Actualizando profesor con ID: {teacher_id}')
    teacher = db_session.query(Teacher).filter_by(id_teacher=teacher_id).first()
    if teacher:
        logging.debug(f'Actualizando detalles del profesor: {teacher.name_teacher} -> {new_data["name_teacher"]}')
        setattr(teacher, 'name_teacher', new_data['name_teacher'])
        db_session.commit()
        logging.info(f'Profesor actualizado exitosamente: {teacher.name_teacher}')
    else:
        logging.warning(f'Profesor con ID {teacher_id} no encontrado')
    return teacher

def delete_teacher(teacher_id):
    logging.info(f'Borrando profesor con ID: {teacher_id}')
    teacher = db_session.query(Teacher).filter_by(id_teacher=teacher_id).first()
    if teacher:
        logging.info(f'Borrando profesor: {teacher.name_teacher}')
        db_session.delete(teacher)
        db_session.commit()
        logging.info(f'Profesor borrado exitosamente: {teacher.name_teacher}')
    else:
        logging.warning(f'Profesor con ID {teacher_id} no encontrado')
    return teacher


def get_all_teachers():
    logging.info('Retrieving all teachers')
    teachers = db_session.query(Teacher).all()
    logging.info(f'Retrieved {len(teachers)} teachers')
    return teachers
