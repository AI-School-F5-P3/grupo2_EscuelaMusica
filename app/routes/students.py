from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud.students import add_student, get_all_students, get_student_by_id, update_student, delete_student
from app.utils.exceptions import ResourceNotFoundError

students_bp = Blueprint('students', __name__)

@students_bp.route('', methods=['GET'])
@jwt_required()
def get_students():
    students = get_all_students()
    return jsonify(students), 200

@students_bp.route('/<int:student_id>', methods=['GET'])
@jwt_required()
def get_single_student(student_id):
    try:
        student = get_student_by_id(student_id)
        return jsonify(student), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@students_bp.route('', methods=['POST'])
@jwt_required()
def create_student():
    student_data = request.get_json()
    try:
        new_student = add_student(student_data)
        return jsonify(new_student), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@students_bp.route('/<int:student_id>', methods=['PUT'])
@jwt_required()
def modify_student(student_id):
    student_data = request.get_json()
    try:
        updated_student = update_student(student_id, student_data)
        return jsonify(updated_student), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@students_bp.route('/<int:student_id>', methods=['DELETE'])
@jwt_required()
def remove_student(student_id):
    try:
        deleted_student = delete_student(student_id)
        return jsonify({"message": "Student deleted successfully", "student": deleted_student}), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404