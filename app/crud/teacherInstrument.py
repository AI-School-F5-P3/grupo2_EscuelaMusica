from config import Session
from models import TeacherInstrument

db_session = Session()

def create_teacher_instrument(id_teacher, id_instrument, id_level):
    new_teacher_instrument = TeacherInstrument(id_teacher=id_teacher, id_instrument=id_instrument, id_level=id_level)
    db_session.add(new_teacher_instrument)
    db_session.commit()
    return new_teacher_instrument

def get_teacher_instrument_by_id(instrument_id):
    return db_session.query(TeacherInstrument).filter_by(id=instrument_id).first()

def update_teacher_instrument(instrument_id, new_data):
    teacher_instrument = db_session.query(TeacherInstrument).filter_by(id=instrument_id).first()
    if teacher_instrument:
        for key, value in new_data.items():
            setattr(teacher_instrument, key, value)
        db_session.commit()
    return teacher_instrument

def delete_teacher_instrument(instrument_id):
    teacher_instrument = db_session.query(TeacherInstrument).filter_by(id=instrument_id).first()
    if teacher_instrument:
        db_session.delete(teacher_instrument)
        db_session.commit()
    return teacher_instrument

def get_all_teacher_instruments():
    return db_session.query(TeacherInstrument).all()
