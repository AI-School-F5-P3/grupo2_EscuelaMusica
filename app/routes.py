from flask import Blueprint, jsonify, request
from .models import db, Student, MusicClass

main = Blueprint('main', __name__)

@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@main.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

@main.route('/student', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

@main.route('/music_class', methods=['POST'])
def create_music_class():
    data = request.get_json()
    new_class = MusicClass(name=data['name'], price=data['price'], student_id=data['student_id'])
    db.session.add(new_class)
    db.session.commit()
    return jsonify(new_class.to_dict()), 201
