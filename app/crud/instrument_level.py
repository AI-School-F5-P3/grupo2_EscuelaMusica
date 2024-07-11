# Funciones CRUD para `InstrumentLevel`

from config import Session
from models import InstrumentLevel

db_session = Session()

def create_instrument_level(instrument_id, level_id):
    new_instrument_level = InstrumentLevel(instruments_id_instrument=instrument_id, levels_id_level=level_id)
    db_session.add(new_instrument_level)
    db_session.commit()
    return new_instrument_level

def get_instrument_level(instrument_id, level_id):
    return db_session.query(InstrumentLevel).filter_by(instruments_id_instrument=instrument_id, levels_id_level=level_id).first()

def delete_instrument_level(instrument_id, level_id):
    instrument_level = db_session.query(InstrumentLevel).filter_by(instruments_id_instrument=instrument_id, levels_id_level=level_id).first()
    if instrument_level:
        db_session.delete(instrument_level)
        db_session.commit()
    return instrument_level

def get_all_instrument_levels():
    return db_session.query(InstrumentLevel).all()
