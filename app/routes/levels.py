import logging
from flask import Blueprint, request, jsonify
<<<<<<< Updated upstream
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud.levels import add_level, get_all_levels, get_level_by_id, update_level, delete_level
from app.utils.app_logging import log_request
=======
from flask_jwt_extended import jwt_required
from app.crud.levels import add_level, get_all_levels, get_level_by_id, update_level, delete_level
from app.utils.logging import log_request
>>>>>>> Stashed changes

# Configuración del logger
logger = logging.getLogger(__name__)

levels_bp = Blueprint('levels', __name__)

@levels_bp.route('/levels', methods=['POST'])
@jwt_required()
@log_request
<<<<<<< HEAD
<<<<<<< Updated upstream
def create_instrument():
=======
def create_level():
>>>>>>> f5c9393db2d7f571e4c27886ffb4a84871eae107
    current_user = get_jwt_identity()
    data = request.json
    logger.info(f"Usuario {current_user} creando nuevo nivel: {data}")
    result = add_level(data)
    if isinstance(result, tuple) and result[1] != 201:
        logger.error(f"Error al crear nivel: {result[0]}")
    else:
        logger.info(f"Nivel creado exitosamente: {result}")
    return result
=======
def create_level():
    data = request.json
    return add_level(data)
>>>>>>> Stashed changes

@levels_bp.route('/levels', methods=['GET'])
@jwt_required()
@log_request
<<<<<<< HEAD
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
=======
def list_levels():
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} solicitando lista de todos los niveles")
    levels = get_all_levels()
    logger.info(f"Se recuperaron {len(levels)} niveles")
    return jsonify(levels)
>>>>>>> f5c9393db2d7f571e4c27886ffb4a84871eae107

@levels_bp.route('/levels/<int:id>', methods=['GET'])
@jwt_required()
@log_request
<<<<<<< HEAD
<<<<<<< Updated upstream
def retrieve_instrument(id):
=======
def retrieve_level(id):
>>>>>>> f5c9393db2d7f571e4c27886ffb4a84871eae107
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} solicitando detalles del nivel con ID: {id}")
    result = get_level_by_id(id)
    if isinstance(result, tuple) and result[1] != 200:
        logger.error(f"Error al recuperar nivel con ID {id}: {result[0]}")
    else:
        logger.info(f"Nivel con ID {id} recuperado exitosamente")
    return result
=======
def retrieve_level(id):
    return get_level_by_id(id)
>>>>>>> Stashed changes

@levels_bp.route('/levels/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
<<<<<<< HEAD
<<<<<<< Updated upstream
def edit_instrument(id):
=======
def edit_level(id):
>>>>>>> f5c9393db2d7f571e4c27886ffb4a84871eae107
    current_user = get_jwt_identity()
    data = request.json
    logger.info(f"Usuario {current_user} intentando actualizar nivel con ID {id}: {data}")
    result = update_level(id, data)
    if isinstance(result, tuple) and result[1] != 200:
        logger.error(f"Error al actualizar nivel con ID {id}: {result[0]}")
    else:
        logger.info(f"Nivel con ID {id} actualizado exitosamente")
    return result
=======
def edit_level(id):
    data = request.json
    return update_level(id, data)
>>>>>>> Stashed changes

@levels_bp.route('/levels/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
<<<<<<< HEAD
<<<<<<< Updated upstream
def remove_instrument(id):
=======
def remove_level(id):
>>>>>>> f5c9393db2d7f571e4c27886ffb4a84871eae107
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} intentando eliminar nivel con ID {id}")
    result = delete_level(id)
    if isinstance(result, tuple) and result[1] != 200:
        logger.error(f"Error al eliminar nivel con ID {id}: {result[0]}")
    else:
        logger.info(f"Nivel con ID {id} eliminado exitosamente")
    return result
=======
def remove_level(id):
    return delete_level(id)
>>>>>>> Stashed changes
