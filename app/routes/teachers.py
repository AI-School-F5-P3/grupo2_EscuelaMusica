from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud.teachers import add_teacher, get_all_teachers, get_teacher_by_id, update_teacher, delete_teacher
from app.utils.exceptions import ResourceNotFoundError

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('', methods=['GET'])
@jwt_required()
def get_teachers():
    teachers = get_all_teachers()
    return jsonify(teachers), 200

@teachers_bp.route('/<int:teacher_id>', methods=['GET'])
@jwt_required()
def get_single_teacher(teacher_id):
    try:
        teacher = get_teacher_by_id(teacher_id)
        return jsonify(teacher), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@teachers_bp.route('', methods=['POST'])
@jwt_required()
def create_teacher():
    teacher_data = request.get_json()
    try:
        new_teacher = add_teacher(teacher_data)
        return jsonify(new_teacher), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@teachers_bp.route('/<int:teacher_id>', methods=['PUT'])
@jwt_required()
def modify_teacher(teacher_id):
    teacher_data = request.get_json()
    try:
        updated_teacher = update_teacher(teacher_id, teacher_data)
        return jsonify(updated_teacher), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@teachers_bp.route('/<int:teacher_id>', methods=['DELETE'])
@jwt_required()
def remove_teacher(teacher_id):
    try:
        deleted_teacher = delete_teacher(teacher_id)
        return jsonify({"message": "Teacher deleted successfully", "teacher": deleted_teacher}), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404