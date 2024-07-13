from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.enrollments import add_enrollment, get_all_enrollments, get_enrollment_by_id, update_enrollment, delete_enrollment
from app.utils.logging import log_request

enrollments_bp = Blueprint('enrollments', __name__)

@enrollments_bp.route('', methods=['GET'])
def get_enrollments():
    enrollments = get_all_enrollments()
    return jsonify(enrollments), 200

@enrollments_bp.route('/<int:enrollment_id>', methods=['GET'])
def get_single_enrollment(enrollment_id):
    enrollment = get_enrollment_by_id(enrollment_id)
    return enrollment, 200

@enrollments_bp.route('', methods=['POST'])
def create_enrollment():
    enrollment_data = request.get_json()
    new_enrollment = add_enrollment(enrollment_data)
    return new_enrollment, 201

@enrollments_bp.route('/<int:enrollment_id>', methods=['PUT'])
def modify_enrollment(enrollment_id):
    enrollment_data = request.get_json()
    updated_enrollment = update_enrollment(enrollment_id, enrollment_data)
    return updated_enrollment, 200

@enrollments_bp.route('/<int:enrollment_id>', methods=['DELETE'])
def remove_enrollment(enrollment_id):
    deleted_enrollment = delete_enrollment(enrollment_id)
    return deleted_enrollment, 200