from app.models import Instrument
from app.schemas import instrument_schema, instruments_schema
from app import db

def add_instrument(data):
    new_instrument = Instrument(**data)
    db.session.add(new_instrument)
    db.session.commit()
    return instrument_schema.jsonify(new_instrument)

def get_all_instruments():
    instruments = Instrument.query.all()
    return instruments_schema.dump(instruments)

def get_instrument_by_id(instrument_id):
    instrument = Instrument.query.get_or_404(instrument_id)
    return instrument_schema.jsonify(instrument)

def update_instrument(instrument_id, data):
    instrument = Instrument.query.get_or_404(instrument_id)
    for key, value in data.items():
        setattr(instrument, key, value)
    db.session.commit()
    return instrument_schema.jsonify(instrument)

def delete_instrument(instrument_id):
    instrument = Instrument.query.get_or_404(instrument_id)
    db.session.delete(instrument)
    db.session.commit()
    return instrument_schema.jsonify(instrument)
