from config import Session
from models import Instrument

db_session = Session()

def create_instrument(instrument_name):
    new_instrument = Instrument(instrument=instrument_name)
    db_session.add(new_instrument)
    db_session.commit()
    return new_instrument

def get_instrument_by_id(instrument_id):
    return db_session.query(Instrument).filter_by(id_instrument=instrument_id).first()

def update_instrument(instrument_id, new_data):
    instrument = db_session.query(Instrument).filter_by(id_instrument=instrument_id).first()
    if instrument:
        setattr(instrument, 'instrument', new_data['instrument'])
        db_session.commit()
    return instrument

def delete_instrument(instrument_id):
    instrument = db_session.query(Instrument).filter_by(id_instrument=instrument_id).first()
    if instrument:
        db_session.delete(instrument)
        db_session.commit()
    return instrument

def get_all_instruments():
    return db_session.query(Instrument).all()