from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.students import add_student, get_all_students, get_student_by_id, update_student, delete_student
from app.utils.logging import log_request

students_bp = Blueprint('students', __name__)

@students_bp.route('', methods=['GET'])
def get_students():
    students = get_all_students()
    return jsonify(students), 200

@students_bp.route('/<int:student_id>', methods=['GET'])
def get_single_student(student_id):
    student = get_student_by_id(student_id)
    return student, 200

@students_bp.route('', methods=['POST'])
def create_student():
    student_data = request.get_json()
    new_student = add_student(student_data)
    return new_student, 201

@students_bp.route('/<int:student_id>', methods=['PUT'])
def modify_student(student_id):
    student_data = request.get_json()
    updated_student = update_student(student_id, student_data)
    return updated_student, 200

@students_bp.route('/<int:student_id>', methods=['DELETE'])
def remove_student(student_id):
    deleted_student = delete_student(student_id)
    return deleted_student, 200