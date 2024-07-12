from config import Session
from models import Student

db_session = Session()

def create_student(first_name, last_name, age, phone, email):
    new_student = Student(first_name=first_name, last_name=last_name, age=age, phone=phone, email=email)
    db_session.add(new_student)
    db_session.commit()
    return new_student

def get_student_by_id(student_id):
    return db_session.query(Student).filter_by(id_student=student_id).first()

def update_student(student_id, new_data):
    student = db_session.query(Student).filter_by(id_student=student_id).first()
    if student:
        for key, value in new_data.items():
            setattr(student, key, value)
        db_session.commit()
    return student

def delete_student(student_id):
    student = db_session.query(Student).filter_by(id_student=student_id).first()
    if student:
        db_session.delete(student)
        db_session.commit()
    return student

def get_all_students():
    return db_session.query(Student).all()