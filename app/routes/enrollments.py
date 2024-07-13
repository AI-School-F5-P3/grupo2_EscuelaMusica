from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud.enrollments import add_enrollment, get_all_enrollments, get_enrollment_by_id, update_enrollment, delete_enrollment
from app.utils.exceptions import ResourceNotFoundError

enrollments_bp = Blueprint('enrollments', __name__)

@enrollments_bp.route('', methods=['GET'])
@jwt_required()
def get_enrollments():
    enrollments = get_all_enrollments()
    return jsonify(enrollments), 200

@enrollments_bp.route('/<int:enrollment_id>', methods=['GET'])
@jwt_required()
def get_single_enrollment(enrollment_id):
    try:
        enrollment = get_enrollment_by_id(enrollment_id)
        return jsonify(enrollment), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@enrollments_bp.route('', methods=['POST'])
@jwt_required()
def create_enrollment():
    enrollment_data = request.get_json()
    try:
        new_enrollment = add_enrollment(enrollment_data)
        return jsonify(new_enrollment), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@enrollments_bp.route('/<int:enrollment_id>', methods=['PUT'])
@jwt_required()
def modify_enrollment(enrollment_id):
    enrollment_data = request.get_json()
    try:
        updated_enrollment = update_enrollment(enrollment_id, enrollment_data)
        return jsonify(updated_enrollment), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@enrollments_bp.route('/<int:enrollment_id>', methods=['DELETE'])
@jwt_required()
def remove_enrollment(enrollment_id):
    try:
        deleted_enrollment = delete_enrollment(enrollment_id)
        return jsonify({"message": "Enrollment deleted successfully", "enrollment": deleted_enrollment}), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404