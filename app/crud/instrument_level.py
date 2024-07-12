import logging
from db import Session
from models import InstrumentLevel

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_instrument_level(instrument_id, level_id):
    logging.info(f'Creando nivel de instrumento - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    new_instrument_level = InstrumentLevel(instruments_id_instrument=instrument_id, levels_id_level=level_id)
    db_session.add(new_instrument_level)
    db_session.commit()
    logging.info(f'Nivel de instrumento creado exitosamente - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    return new_instrument_level

def get_instrument_level(instrument_id, level_id):
    logging.info(f'Recuperando nivel de instrumento - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    instrument_level = db_session.query(InstrumentLevel).filter_by(instruments_id_instrument=instrument_id, levels_id_level=level_id).first()
    if instrument_level:
        logging.info(f'Nivel de instrumento recuperado - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    else:
        logging.warning(f'Nivel de instrumento no encontrado - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    return instrument_level

def delete_instrument_level(instrument_id, level_id):
    logging.info(f'Borrando nivel de instrumento - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    instrument_level = db_session.query(InstrumentLevel).filter_by(instruments_id_instrument=instrument_id, levels_id_level=level_id).first()
    if instrument_level:
        db_session.delete(instrument_level)
        db_session.commit()
        logging.info(f'Nivel de instrumento borrado exitosamente - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    else:
        logging.warning(f'Nivel de instrumento no encontrado - Instrumento ID: {instrument_id}, Nivel ID: {level_id}')
    return instrument_level

def get_all_instrument_levels():
    logging.info('Recuperando todos los niveles de instrumento')
    instrument_levels = db_session.query(InstrumentLevel).all()
    logging.info(f'Se han recuperado {len(instrument_levels)} niveles de instrumento')
    return instrument_levels

