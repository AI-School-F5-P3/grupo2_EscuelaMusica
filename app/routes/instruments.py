from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.instruments import add_instrument, get_all_instruments, get_instrument_by_id, update_instrument, delete_instrument
from app.utils.logging import log_request

instruments_bp = Blueprint('instruments', __name__)

@instruments_bp.route('/instruments', methods=['POST'])
@jwt_required()
@log_request
def create_instrument():
    data = request.json
    return add_instrument(data)

@instruments_bp.route('/instruments', methods=['GET'])
@jwt_required()
@log_request
def list_instruments():
    return jsonify(get_all_instruments())

@instruments_bp.route('/instruments/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def retrieve_instrument(id):
    return get_instrument_by_id(id)

@instruments_bp.route('/instruments/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def edit_instrument(id):
    data = request.json
    return update_instrument(id, data)

@instruments_bp.route('/instruments/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def remove_instrument(id):
    return delete_instrument(id)
