from app.models import Student
from app.schemas import student_schema, students_schema
from app import db

def add_student(data):
    new_student = Student(**data)
    db.session.add(new_student)
    db.session.commit()
    return student_schema.jsonify(new_student)

def get_all_students():
    students = Student.query.all()
    return students_schema.dump(students)

def get_student_by_id(student_id):
    student = Student.query.get_or_404(student_id)
    return student_schema.jsonify(student)

def update_student(student_id, data):
    student = Student.query.get_or_404(student_id)
    for key, value in data.items():
        setattr(student, key, value)
    db.session.commit()
    return student_schema.jsonify(student)

def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)
