from db import Session
from models import PriceInstrument

db_session = Session()

def create_price_instrument(pack, pack_price):
    new_price_instrument = PriceInstrument(pack=pack, pack_price=pack_price)
    db_session.add(new_price_instrument)
    db_session.commit()
    return new_price_instrument

def get_price_instrument_by_id(price_id):
    return db_session.query(PriceInstrument).filter_by(id_price=price_id).first()

def update_price_instrument(price_id, new_data):
    price_instrument = db_session.query(PriceInstrument).filter_by(id_price=price_id).first()
    if price_instrument:
        setattr(price_instrument, 'pack', new_data['pack'])
        setattr(price_instrument, 'pack_price', new_data['pack_price'])
        db_session.commit()
    return price_instrument

def delete_price_instrument(price_id):
    price_instrument = db_session.query(PriceInstrument).filter_by(id_price=price_id).first()
    if price_instrument:
        db_session.delete(price_instrument)
        db_session.commit()
    return price_instrument

def get_all_price_instruments():
    return db_session.query(PriceInstrument).all()
