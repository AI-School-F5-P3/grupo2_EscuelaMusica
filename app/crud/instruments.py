import logging
from db import Session
from models import Instrument

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_instrument(instrument_name):
    logging.info(f'Creando instrumento: {instrument_name}')
    new_instrument = Instrument(instrument=instrument_name)
    db_session.add(new_instrument)
    db_session.commit()
    logging.info(f'Instrumento creado exitosamente: {instrument_name}')
    return new_instrument

def get_instrument_by_id(instrument_id):
    logging.info(f'Recuperando instrumento con ID: {instrument_id}')
    instrument = db_session.query(Instrument).filter_by(id_instrument=instrument_id).first()
    if instrument:
        logging.info(f'Instrumento recuperado: {instrument.instrument}')
    else:
        logging.warning(f'Instrumento con ID {instrument_id} no encontrado')
    return instrument

def update_instrument(instrument_id, new_data):
    logging.info(f'Actualizando instrumento con ID: {instrument_id}')
    instrument = db_session.query(Instrument).filter_by(id_instrument=instrument_id).first()
    if instrument:
        logging.debug(f'Actualizando detalles del instrumento: {instrument.instrument} -> {new_data["instrument"]}')
        setattr(instrument, 'instrument', new_data['instrument'])
        db_session.commit()
        logging.info(f'Instrumento actualizado exitosamente: {instrument.instrument}')
    else:
        logging.warning(f'Instrumento con ID {instrument_id} no encontrado')
    return instrument

def delete_instrument(instrument_id):
    logging.info(f'Borrando instrumento con ID: {instrument_id}')
    instrument = db_session.query(Instrument).filter_by(id_instrument=instrument_id).first()
    if instrument:
        logging.info(f'Borrando instrumento: {instrument.instrument}')
        db_session.delete(instrument)
        db_session.commit()
        logging.info(f'Instrumento borrado exitosamente: {instrument.instrument}')
    else:
        logging.warning(f'Instrumento con ID {instrument_id} no encontrado')
    return instrument

def get_all_instruments():
    logging.info('Recuperando todos los instrumentos')
    instruments = db_session.query(Instrument).all()
    logging.info(f'Se han recuperado {len(instruments)} instrumentos')
    return instruments
