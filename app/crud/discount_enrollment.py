import logging
from db import Session
from models import DiscountEnrollment

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_discount_enrollment(discount_percentage, final_price):
    logging.info(f'Creando inscripción con descuento: Porcentaje {discount_percentage}, Precio final {final_price}')
    new_discount_enrollment = DiscountEnrollment(discount_discount_percentage=discount_percentage, enrollments_final_price=final_price)
    db_session.add(new_discount_enrollment)
    db_session.commit()
    logging.info(f'Inscripción con descuento creada exitosamente: Porcentaje {discount_percentage}, Precio final {final_price}')
    return new_discount_enrollment

def get_discount_enrollment_by_percentage(discount_percentage):
    logging.info(f'Recuperando inscripción con descuento por porcentaje: {discount_percentage}')
    discount_enrollment = db_session.query(DiscountEnrollment).filter_by(discount_discount_percentage=discount_percentage).first()
    if discount_enrollment:
        logging.info(f'Inscripción con descuento recuperada: Porcentaje {discount_percentage}, Precio final {discount_enrollment.enrollments_final_price}')
    else:
        logging.warning(f'Inscripción con descuento para porcentaje {discount_percentage} no encontrada')
    return discount_enrollment

def delete_discount_enrollment(discount_percentage):
    logging.info(f'Borrando inscripción con descuento por porcentaje: {discount_percentage}')
    discount_enrollment = db_session.query(DiscountEnrollment).filter_by(discount_discount_percentage=discount_percentage).first()
    if discount_enrollment:
        db_session.delete(discount_enrollment)
        db_session.commit()
        logging.info(f'Inscripción con descuento borrada exitosamente: Porcentaje {discount_percentage}, Precio final {discount_enrollment.enrollments_final_price}')
    else:
        logging.warning(f'Inscripción con descuento para porcentaje {discount_percentage} no encontrada')
    return discount_enrollment

def get_all_discount_enrollments():
    logging.info('Recuperando todas las inscripciones con descuento')
    discount_enrollments = db_session.query(DiscountEnrollment).all()
    logging.info(f'Se han recuperado {len(discount_enrollments)} inscripciones con descuento')
    return discount_enrollments
