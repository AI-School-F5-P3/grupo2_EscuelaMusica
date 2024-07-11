from config import Session
from models import Enrollment

db_session = Session()

def create_enrollment(student_id, level_id, instrument_id, teacher_id, base_price, final_price, family_discount):
    new_enrollment = Enrollment(
        id_student=student_id,
        id_level=level_id,
        id_instrument=instrument_id,
        id_teacher=teacher_id,
        base_price=base_price,
        final_price=final_price,
        family_discount=family_discount
    )
    db_session.add(new_enrollment)
    db_session.commit()
    return new_enrollment

def get_enrollment_by_id(enrollment_id):
    return db_session.query(Enrollment).filter_by(id=enrollment_id).first()

def update_enrollment(enrollment_id, new_data):
    enrollment = db_session.query(Enrollment).filter_by(id=enrollment_id).first()
    if enrollment:
        for key, value in new_data.items():
            setattr(enrollment, key, value)
        db_session.commit()
    return enrollment

def delete_enrollment(enrollment_id):
    enrollment = db_session.query(Enrollment).filter_by(id=enrollment_id).first()
    if enrollment:
        db_session.delete(enrollment)
        db_session.commit()
    return enrollment

def get_all_enrollments():
    return db_session.query(Enrollment).all()
