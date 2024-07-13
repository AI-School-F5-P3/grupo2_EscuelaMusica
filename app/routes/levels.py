from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.levels import add_level, get_all_levels, get_level_by_id, update_level, delete_level
from app.utils.logging import log_request

levels_bp = Blueprint('levels', __name__)

@levels_bp.route('', methods=['GET'])
def get_levels():
    levels = get_all_levels()
    return jsonify(levels), 200

@levels_bp.route('/<int:level_id>', methods=['GET'])
def get_single_level(level_id):
    level = get_level_by_id(level_id)
    return level, 200

@levels_bp.route('', methods=['POST'])
def create_level():
    level_data = request.get_json()
    new_level = add_level(level_data)
    return new_level, 201

@levels_bp.route('/<int:level_id>', methods=['PUT'])
def modify_level(level_id):
    level_data = request.get_json()
    updated_level = update_level(level_id, level_data)
    return updated_level, 200

@levels_bp.route('/<int:level_id>', methods=['DELETE'])
def remove_level(level_id):
    deleted_level = delete_level(level_id)
    return deleted_level, 200
