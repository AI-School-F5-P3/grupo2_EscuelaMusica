from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.teachers import add_teacher, get_all_teachers, get_teacher_by_id, update_teacher, delete_teacher
from app.utils.logging import log_request

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers', methods=['POST'])
@jwt_required()
@log_request
def create_teacher():
    data = request.json
    return add_teacher(data)

@teachers_bp.route('/teachers', methods=['GET'])
@jwt_required()
@log_request
def list_teachers():
    return jsonify(get_all_teachers())

@teachers_bp.route('/teachers/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def retrieve_teacher(id):
    return get_teacher_by_id(id)

@teachers_bp.route('/teachers/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def edit_teacher(id):
    data = request.json
    return update_teacher(id, data)

@teachers_bp.route('/teachers/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def remove_teacher(id):
    return delete_teacher(id)
