from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.students import add_student, get_all_students, get_student_by_id, update_student, delete_student
from app.utils.logging import log_request

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
@jwt_required()
@log_request
def create_student():
    data = request.json
    return add_student(data)

@students_bp.route('/students', methods=['GET'])
@jwt_required()
@log_request
def list_students():
    return jsonify(get_all_students())

@students_bp.route('/students/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def retrieve_student(id):
    return get_student_by_id(id)

@students_bp.route('/students/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def edit_student(id):
    data = request.json
    return update_student(id, data)

@students_bp.route('/students/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def remove_student(id):
    return delete_student(id)
