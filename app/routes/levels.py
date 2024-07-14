import logging
from flask import Blueprint, request, jsonify
<<<<<<< Updated upstream
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.CRUD.instruments import add_instrument, get_all_instruments, get_instrument_by_id, update_instrument, delete_instrument
from app.utils.app_logging import log_request
=======
from flask_jwt_extended import jwt_required
from app.crud.levels import add_level, get_all_levels, get_level_by_id, update_level, delete_level
from app.utils.logging import log_request
>>>>>>> Stashed changes

# Configuración del logger
logger = logging.getLogger(__name__)

instruments_bp = Blueprint('instruments', __name__)

@instruments_bp.route('/instruments', methods=['POST'])
@jwt_required()
@log_request
<<<<<<< Updated upstream
def create_instrument():
    current_user = get_jwt_identity()
    data = request.json
    logger.info(f"Usuario {current_user} creando nuevo instrumento: {data}")
    result = add_instrument(data)
    if isinstance(result, tuple) and result[1] != 201:
        logger.error(f"Error al crear instrumento: {result[0]}")
    else:
        logger.info(f"Instrumento creado exitosamente: {result}")
    return result
=======
def create_level():
    data = request.json
    return add_level(data)
>>>>>>> Stashed changes

@instruments_bp.route('/instruments', methods=['GET'])
@jwt_required()
@log_request
<<<<<<< Updated upstream
def list_instruments():
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} solicitando lista de todos los instrumentos")
    instruments = get_all_instruments()
    logger.info(f"Se recuperaron {len(instruments)} instrumentos")
    return jsonify(instruments)
=======
def list_levels():
    return jsonify(get_all_levels())
>>>>>>> Stashed changes

@instruments_bp.route('/instruments/<int:id>', methods=['GET'])
@jwt_required()
@log_request
<<<<<<< Updated upstream
def retrieve_instrument(id):
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} solicitando detalles del instrumento con ID: {id}")
    result = get_instrument_by_id(id)
    if isinstance(result, tuple) and result[1] != 200:
        logger.error(f"Error al recuperar instrumento con ID {id}: {result[0]}")
    else:
        logger.info(f"Instrumento con ID {id} recuperado exitosamente")
    return result
=======
def retrieve_level(id):
    return get_level_by_id(id)
>>>>>>> Stashed changes

@instruments_bp.route('/instruments/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
<<<<<<< Updated upstream
def edit_instrument(id):
    current_user = get_jwt_identity()
    data = request.json
    logger.info(f"Usuario {current_user} intentando actualizar instrumento con ID {id}: {data}")
    result = update_instrument(id, data)
    if isinstance(result, tuple) and result[1] != 200:
        logger.error(f"Error al actualizar instrumento con ID {id}: {result[0]}")
    else:
        logger.info(f"Instrumento con ID {id} actualizado exitosamente")
    return result
=======
def edit_level(id):
    data = request.json
    return update_level(id, data)
>>>>>>> Stashed changes

@instruments_bp.route('/instruments/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
<<<<<<< Updated upstream
def remove_instrument(id):
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} intentando eliminar instrumento con ID {id}")
    result = delete_instrument(id)
    if isinstance(result, tuple) and result[1] != 200:
        logger.error(f"Error al eliminar instrumento con ID {id}: {result[0]}")
    else:
        logger.info(f"Instrumento con ID {id} eliminado exitosamente")
    return result
=======
def remove_level(id):
    return delete_level(id)
>>>>>>> Stashed changes
