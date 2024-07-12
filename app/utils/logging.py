import logging
from functools import wraps
from flask import request, g
import time

# Configuración del logger
logger = logging.getLogger(__name__)

def setup_logger():
    """Configura el logger global."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Registrar el tiempo de inicio
        start_time = time.time()

        # Loguear detalles de la solicitud
        logger.info(f"Solicitud recibida: {request.method} {request.url}")
        logger.info(f"Headers: {dict(request.headers)}")
        logger.info(f"Datos: {request.get_data()}")

        # Ejecutar la función
        response = f(*args, **kwargs)

        # Calcular el tiempo de respuesta
        duration = time.time() - start_time

        # Loguear detalles de la respuesta
        logger.info(f"Respuesta enviada: {response.status_code}")
        logger.info(f"Tiempo de respuesta: {duration:.2f} segundos")

        return response
    return decorated_function

def log_error(error):
    """Función para loguear errores."""
    logger.error(f"Error: {str(error)}", exc_info=True)

def log_info(message):
    """Función para loguear información general."""
    logger.info(message)

def log_warning(message):
    """Función para loguear advertencias."""
    logger.warning(message)

def log_debug(message):
    """Función para loguear mensajes de debug."""
    logger.debug(message)