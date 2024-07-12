from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.levels import add_level, get_all_levels, get_level_by_id, update_level, delete_level
from app.utils.logging import log_request

levels_bp = Blueprint('levels', __name__)

@levels_bp.route('/levels', methods=['POST'])
@jwt_required()
@log_request
def create_level():
    data = request.json
    return add_level(data)

@levels_bp.route('/levels', methods=['GET'])
@jwt_required()
@log_request
def list_levels():
    return jsonify(get_all_levels())

@levels_bp.route('/levels/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def retrieve_level(id):
    return get_level_by_id(id)

@levels_bp.route('/levels/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def edit_level(id):
    data = request.json
    return update_level(id, data)

@levels_bp.route('/levels/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def remove_level(id):
    return delete_level(id)
