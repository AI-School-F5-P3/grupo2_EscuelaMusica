from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud.levels import add_level, get_all_levels, get_level_by_id, update_level, delete_level
from app.utils.exceptions import ResourceNotFoundError

levels_bp = Blueprint('levels', __name__)

@levels_bp.route('', methods=['GET'])
@jwt_required()
def get_levels():
    levels = get_all_levels()
    return jsonify(levels), 200

@levels_bp.route('/<int:level_id>', methods=['GET'])
@jwt_required()
def get_single_level(level_id):
    try:
        level = get_level_by_id(level_id)
        return jsonify(level), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@levels_bp.route('', methods=['POST'])
@jwt_required()
def create_level():
    level_data = request.get_json()
    try:
        new_level = add_level(level_data)
        return jsonify(new_level), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@levels_bp.route('/<int:level_id>', methods=['PUT'])
@jwt_required()
def modify_level(level_id):
    level_data = request.get_json()
    try:
        updated_level = update_level(level_id, level_data)
        return jsonify(updated_level), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@levels_bp.route('/<int:level_id>', methods=['DELETE'])
@jwt_required()
def remove_level(level_id):
    try:
        deleted_level = delete_level(level_id)
        return jsonify({"message": "Level deleted successfully", "level": deleted_level}), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404