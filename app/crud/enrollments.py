import logging
from db import Session
from models import Enrollment

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_enrollment(student_id, level_id, instrument_id, teacher_id, base_price, final_price, family_discount):
    logging.info(f'Creando matrícula para el estudiante ID {student_id} en el nivel ID {level_id}, instrumento ID {instrument_id}, profesor ID {teacher_id}')
    new_enrollment = Enrollment(
        id_student=student_id,
        id_level=level_id,
        id_instrument=instrument_id,
        id_teacher=teacher_id,
        base_price=base_price,
        final_price=final_price,
        family_discount=family_discount
    )
    db_session.add(new_enrollment)
    db_session.commit()
    logging.info(f'Matrícula creada exitosamente con ID: {new_enrollment.id}')
    return new_enrollment

def get_enrollment_by_id(enrollment_id):
    logging.info(f'Recuperando matrícula con ID: {enrollment_id}')
    enrollment = db_session.query(Enrollment).filter_by(id=enrollment_id).first()
    if enrollment:
        logging.info(f'Matrícula recuperada: ID {enrollment.id}, ID del estudiante {enrollment.id_student}, ID del nivel {enrollment.id_level}, ID del instrumento {enrollment.id_instrument}, ID del profesor {enrollment.id_teacher}')
    else:
        logging.warning(f'Matrícula con ID {enrollment_id} no encontrada')
    return enrollment

def update_enrollment(enrollment_id, new_data):
    logging.info(f'Actualizando matrícula con ID: {enrollment_id}')
    enrollment = db_session.query(Enrollment).filter_by(id=enrollment_id).first()
    if enrollment:
        logging.debug(f'Actualizando detalles de la matrícula: {enrollment.id}, {new_data}')
        for key, value in new_data.items():
            setattr(enrollment, key, value)
        db_session.commit()
        logging.info(f'Matrícula actualizada exitosamente: ID {enrollment.id}')
    else:
        logging.warning(f'Matrícula con ID {enrollment_id} no encontrada')
    return enrollment

def delete_enrollment(enrollment_id):
    logging.info(f'Borrando matrícula con ID: {enrollment_id}')
    enrollment = db_session.query(Enrollment).filter_by(id=enrollment_id).first()
    if enrollment:
        logging.info(f'Borrando matrícula: ID {enrollment.id}, ID del estudiante {enrollment.id_student}, ID del nivel {enrollment.id_level}, ID del instrumento {enrollment.id_instrument}, ID del profesor {enrollment.id_teacher}')
        db_session.delete(enrollment)
        db_session.commit()
        logging.info(f'Matrícula borrada exitosamente: ID {enrollment.id}')
    else:
        logging.warning(f'Matrícula con ID {enrollment_id} no encontrada')
    return enrollment

def get_all_enrollments():
    logging.info('Recuperando todas las matrículas')
    enrollments = db_session.query(Enrollment).all()
    logging.info(f'Se han recuperado {len(enrollments)} matrículas')
    return enrollments
