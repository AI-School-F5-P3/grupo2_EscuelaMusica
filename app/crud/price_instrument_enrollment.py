import logging
from db import Session
from models import PriceInstrumentEnrollment

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_price_instrument_enrollment(pack, base_price):
    logging.info(f'Creando inscripción de instrumento con precio - Paquete: {pack}, Precio base: {base_price}')
    new_price_instrument_enrollment = PriceInstrumentEnrollment(price_instrument_pack=pack, enrollments_base_price=base_price)
    db_session.add(new_price_instrument_enrollment)
    db_session.commit()
    logging.info(f'Inscripción de instrumento con precio creada exitosamente - Paquete: {pack}, Precio base: {base_price}')
    return new_price_instrument_enrollment

def get_price_instrument_enrollment_by_pack(pack):
    logging.info(f'Recuperando inscripción de instrumento con precio por paquete: {pack}')
    price_instrument_enrollment = db_session.query(PriceInstrumentEnrollment).filter_by(price_instrument_pack=pack).first()
    if price_instrument_enrollment:
        logging.info(f'Inscripción de instrumento con precio recuperada - Paquete: {pack}')
    else:
        logging.warning(f'Inscripción de instrumento con precio no encontrada - Paquete: {pack}')
    return price_instrument_enrollment

def delete_price_instrument_enrollment(pack):
    logging.info(f'Borrando inscripción de instrumento con precio por paquete: {pack}')
    price_instrument_enrollment = db_session.query(PriceInstrumentEnrollment).filter_by(price_instrument_pack=pack).first()
    if price_instrument_enrollment:
        db_session.delete(price_instrument_enrollment)
        db_session.commit()
        logging.info(f'Inscripción de instrumento con precio borrada exitosamente - Paquete: {pack}')
    else:
        logging.warning(f'Inscripción de instrumento con precio no encontrada - Paquete: {pack}')
    return price_instrument_enrollment

def get_all_price_instrument_enrollments():
    logging.info('Recuperando todas las inscripciones de instrumento con precio')
    price_instrument_enrollments = db_session.query(PriceInstrumentEnrollment).all()
    logging.info(f'Se han recuperado {len(price_instrument_enrollments)} inscripciones de instrumento con precio')
    return price_instrument_enrollments

