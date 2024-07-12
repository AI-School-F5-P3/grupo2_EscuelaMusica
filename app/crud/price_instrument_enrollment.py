# Funciones CRUD para `PriceInstrumentEnrollment`

from config import Session
from models import PriceInstrumentEnrollment

db_session = Session()

def create_price_instrument_enrollment(pack, base_price):
    new_price_instrument_enrollment = PriceInstrumentEnrollment(price_instrument_pack=pack, enrollments_base_price=base_price)
    db_session.add(new_price_instrument_enrollment)
    db_session.commit()
    return new_price_instrument_enrollment

def get_price_instrument_enrollment_by_pack(pack):
    return db_session.query(PriceInstrumentEnrollment).filter_by(price_instrument_pack=pack).first()

def delete_price_instrument_enrollment(pack):
    price_instrument_enrollment = db_session.query(PriceInstrumentEnrollment).filter_by(price_instrument_pack=pack).first()
    if price_instrument_enrollment:
        db_session.delete(price_instrument_enrollment)
        db_session.commit()
    return price_instrument_enrollment

def get_all_price_instrument_enrollments():
    return db_session.query(PriceInstrumentEnrollment).all()