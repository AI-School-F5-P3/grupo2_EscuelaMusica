from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.enrollments import add_enrollment, get_all_enrollments, get_enrollment_by_id, update_enrollment, delete_enrollment
from app.utils.logging import log_request

enrollments_bp = Blueprint('enrollments', __name__)

@enrollments_bp.route('/enrollments', methods=['POST'])
@jwt_required()
@log_request
def create_enrollment():
    data = request.json
    return add_enrollment(data)

@enrollments_bp.route('/enrollments', methods=['GET'])
@jwt_required()
@log_request
def list_enrollments():
    return jsonify(get_all_enrollments())

@enrollments_bp.route('/enrollments/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def retrieve_enrollment(id):
    return get_enrollment_by_id(id)

@enrollments_bp.route('/enrollments/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def edit_enrollment(id):
    data = request.json
    return update_enrollment(id, data)

@enrollments_bp.route('/enrollments/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def remove_enrollment(id):
    return delete_enrollment(id)
