from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.teachers import add_teacher, get_all_teachers, get_teacher_by_id, update_teacher, delete_teacher
from app.utils.logging import log_request

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('', methods=['GET'])
def get_teachers():
    teachers = get_all_teachers()
    return jsonify(teachers), 200

@teachers_bp.route('/<int:teacher_id>', methods=['GET'])
def get_single_teacher(teacher_id):
    teacher = get_teacher_by_id(teacher_id)
    return teacher, 200

@teachers_bp.route('', methods=['POST'])
def create_teacher():
    teacher_data = request.get_json()
    new_teacher = add_teacher(teacher_data)
    return new_teacher, 201

@teachers_bp.route('/<int:teacher_id>', methods=['PUT'])
def modify_teacher(teacher_id):
    teacher_data = request.get_json()
    updated_teacher = update_teacher(teacher_id, teacher_data)
    return updated_teacher, 200

@teachers_bp.route('/<int:teacher_id>', methods=['DELETE'])
def remove_teacher(teacher_id):
    deleted_teacher = delete_teacher(teacher_id)
    return deleted_teacher, 200