from config import Session
from models import Teacher

db_session = Session()

def create_teacher(name_teacher):
    new_teacher = Teacher(name_teacher=name_teacher)
    db_session.add(new_teacher)
    db_session.commit()
    return new_teacher

def get_teacher_by_id(teacher_id):
    return db_session.query(Teacher).filter_by(id_teacher=teacher_id).first()

def update_teacher(teacher_id, new_data):
    teacher = db_session.query(Teacher).filter_by(id_teacher=teacher_id).first()
    if teacher:
        setattr(teacher, 'name_teacher', new_data['name_teacher'])
        db_session.commit()
    return teacher

def delete_teacher(teacher_id):
    teacher = db_session.query(Teacher).filter_by(id_teacher=teacher_id).first()
    if teacher:
        db_session.delete(teacher)
        db_session.commit()
    return teacher

def get_all_teachers():
    return db_session.query(Teacher).all()