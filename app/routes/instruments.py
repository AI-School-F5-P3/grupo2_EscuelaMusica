from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud.instruments import add_instrument, get_all_instruments, get_instrument_by_id, update_instrument, delete_instrument
from app.utils.exceptions import ResourceNotFoundError

instruments_bp = Blueprint('instruments', __name__)

@instruments_bp.route('', methods=['GET'])
@jwt_required()
def get_instruments():
    instruments = get_all_instruments()
    return jsonify(instruments), 200

@instruments_bp.route('/<int:instrument_id>', methods=['GET'])
@jwt_required()
def get_single_instrument(instrument_id):
    try:
        instrument = get_instrument_by_id(instrument_id)
        return jsonify(instrument), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@instruments_bp.route('', methods=['POST'])
@jwt_required()
def create_instrument():
    instrument_data = request.get_json()
    try:
        new_instrument = add_instrument(instrument_data)
        return jsonify(new_instrument), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@instruments_bp.route('/<int:instrument_id>', methods=['PUT'])
@jwt_required()
def modify_instrument(instrument_id):
    instrument_data = request.get_json()
    try:
        updated_instrument = update_instrument(instrument_id, instrument_data)
        return jsonify(updated_instrument), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@instruments_bp.route('/<int:instrument_id>', methods=['DELETE'])
@jwt_required()
def remove_instrument(instrument_id):
    try:
        deleted_instrument = delete_instrument(instrument_id)
        return jsonify({"message": "Instrument deleted successfully", "instrument": deleted_instrument}), 200
    except ResourceNotFoundError as e:
        return jsonify({"error": str(e)}), 404