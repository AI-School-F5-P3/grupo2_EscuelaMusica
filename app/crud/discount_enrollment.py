from config import Session
from models import DiscountEnrollment

db_session = Session()

def create_discount_enrollment(discount_percentage, final_price):
    new_discount_enrollment = DiscountEnrollment(discount_discount_percentage=discount_percentage, enrollments_final_price=final_price)
    db_session.add(new_discount_enrollment)
    db_session.commit()
    return new_discount_enrollment

def get_discount_enrollment_by_percentage(discount_percentage):
    return db_session.query(DiscountEnrollment).filter_by(discount_discount_percentage=discount_percentage).first()

def delete_discount_enrollment(discount_percentage):
    discount_enrollment = db_session.query(DiscountEnrollment).filter_by(discount_discount_percentage=discount_percentage).first()
    if discount_enrollment:
        db_session.delete(discount_enrollment)
        db_session.commit()
    return discount_enrollment

def get_all_discount_enrollments():
    return db_session.query(DiscountEnrollment).all()
