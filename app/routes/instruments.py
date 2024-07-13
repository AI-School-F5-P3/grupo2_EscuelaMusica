from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.crud.instruments import add_instrument, get_all_instruments, get_instrument_by_id, update_instrument, delete_instrument
from app.utils.logging import log_request

instruments_bp = Blueprint('instruments', __name__)

@instruments_bp.route('', methods=['GET'])
def get_instruments():
    instruments = get_all_instruments()
    return jsonify(instruments), 200

@instruments_bp.route('/<int:instrument_id>', methods=['GET'])
def get_single_instrument(instrument_id):
    instrument = get_instrument_by_id(instrument_id)
    return instrument, 200

@instruments_bp.route('', methods=['POST'])
def create_instrument():
    instrument_data = request.get_json()
    new_instrument = add_instrument(instrument_data)
    return new_instrument, 201

@instruments_bp.route('/<int:instrument_id>', methods=['PUT'])
def modify_instrument(instrument_id):
    instrument_data = request.get_json()
    updated_instrument = update_instrument(instrument_id, instrument_data)
    return updated_instrument, 200

@instruments_bp.route('/<int:instrument_id>', methods=['DELETE'])
def remove_instrument(instrument_id):
    deleted_instrument = delete_instrument(instrument_id)
    return deleted_instrument, 200
