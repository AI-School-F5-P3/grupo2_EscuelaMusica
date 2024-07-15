<<<<<<< HEAD
import os
import logging
from logging.handlers import RotatingFileHandler
from functools import wraps
from flask import request, g, current_app
import time

def setup_logger(app):
    """Configura el logger global y de la aplicación."""
    if not app.debug or app.testing:
        log_dir = os.path.join(app.root_path, 'logs')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_file = os.path.join(log_dir, 'app.log')
        
        file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=10)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        
        # Evitar agregar múltiples veces el manejador
        if not app.logger.handlers:
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('Inicialización del logger')

def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()

        current_app.logger.info(f"Solicitud recibida: {request.method} {request.url}")
        current_app.logger.info(f"Headers: {dict(request.headers)}")
        current_app.logger.info(f"Datos: {request.get_data()}")

        response = f(*args, **kwargs)

        duration = time.time() - start_time

        current_app.logger.info(f"Respuesta enviada: {response.status_code}")
        current_app.logger.info(f"Tiempo de respuesta: {duration:.2f} segundos")

        return response
    return decorated_function

def log_error(error):
    """Función para loguear errores."""
    current_app.logger.error(f"Error: {str(error)}", exc_info=True)

def log_info(message):
    """Función para loguear información general."""
    current_app.logger.info(message)

def log_warning(message):
    """Función para loguear advertencias."""
    current_app.logger.warning(message)

def log_debug(message):
    """Función para loguear mensajes de debug."""
    current_app.logger.debug(message)
def log_debug(message):
    """Función para loguear mensajes de debug."""
    logger.debug(message)
=======
import logging
from logging.handlers import RotatingFileHandler
from flask import request
from flask_jwt_extended import get_jwt_identity

class JWTRequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.method = request.method
        record.remote_addr = request.remote_addr
        record.user_id = get_jwt_identity() or 'Anonymous'
        return super().format(record)

def setup_logging(app):
    """
    Configura el logging para la aplicación.
    
    :param app: La instancia de la aplicación Flask
    """
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = JWTRequestFormatter('%(asctime)s - %(name)s - %(levelname)s - %(method)s %(url)s (%(remote_addr)s) - User: %(user_id)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
>>>>>>> Jaanh
