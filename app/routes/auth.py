import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User
from app.utils.app_logging import log_request

# Configuración del logger
logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
@log_request
def register_user():
    data = request.json
    logger.info(f"Creando nuevo usuario: {data}")
    
    # Verificar si el usuario ya existe
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"msg": "Username already exists"}), 400
    
    # Crear un nuevo usuario
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    
    try:
        new_user.save()
        logger.info(f"Usuario creado exitosamente: {new_user}")
        return jsonify({"msg": "User created successfully"}), 201
    except Exception as e:
        logger.error(f"Error al crear usuario: {str(e)}")
        return jsonify({"msg": "Failed to create user"}), 500

@auth_bp.route('/users', methods=['GET'])
@jwt_required()
@log_request
def list_users():
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} solicitando lista de usuarios")
    
    users = User.query.all()
    user_list = [{"username": user.username, "id": user.id} for user in users]
    
    logger.info(f"Retornando {len(user_list)} usuarios")
    return jsonify(user_list), 200

@auth_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def retrieve_user(id):
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} solicitando información del usuario con ID: {id}")
    
    user = User.query.get(id)
    if user:
        user_data = {"username": user.username, "id": user.id}
        logger.info(f"Retornando información del usuario: {user_data}")
        return jsonify(user_data), 200
    else:
        logger.warning(f"No se encontró el usuario con ID: {id}")
        return jsonify({"msg": "User not found"}), 404

@auth_bp.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def edit_user(id):
    current_user = get_jwt_identity()
    data = request.json
    logger.info(f"Usuario {current_user} actualizando información del usuario con ID: {id} - Datos: {data}")
    
    user = User.query.get(id)
    if user:
        try:
            user.username = data.get('username', user.username)
            if 'password' in data:
                user.set_password(data['password'])
            user.save()
            logger.info(f"Usuario actualizado correctamente: {user}")
            return jsonify({"msg": "User updated successfully"}), 200
        except Exception as e:
            logger.error(f"Error al actualizar usuario: {str(e)}")
            return jsonify({"msg": "Failed to update user"}), 500
    else:
        logger.warning(f"No se encontró el usuario con ID: {id}")
        return jsonify({"msg": "User not found"}), 404

@auth_bp.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def delete_user(id):
    current_user = get_jwt_identity()
    logger.info(f"Usuario {current_user} eliminando usuario con ID: {id}")
    
    user = User.query.get(id)
    if user:
        try:
            user.delete()
            logger.info(f"Usuario eliminado correctamente: {user}")
            return jsonify({"msg": "User deleted successfully"}), 200
        except Exception as e:
            logger.error(f"Error al eliminar usuario: {str(e)}")
            return jsonify({"msg": "Failed to delete user"}), 500
    else:
        logger.warning(f"No se encontró el usuario con ID: {id}")
        return jsonify({"msg": "User not found"}), 404
