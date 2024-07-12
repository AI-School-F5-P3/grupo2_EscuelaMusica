from app.models import Teacher
from app.schemas import teacher_schema, teachers_schema
from app import db

def add_teacher(data):
    new_teacher = Teacher(**data)
    db.session.add(new_teacher)
    db.session.commit()
    return teacher_schema.jsonify(new_teacher)

def get_all_teachers():
    teachers = Teacher.query.all()
    return teachers_schema.dump(teachers)

def get_teacher_by_id(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return teacher_schema.jsonify(teacher)

def update_teacher(teacher_id, data):
    teacher = Teacher.query.get_or_404(teacher_id)
    for key, value in data.items():
        setattr(teacher, key, value)
    db.session.commit()
    return teacher_schema.jsonify(teacher)

def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    return teacher_schema.jsonify(teacher)
