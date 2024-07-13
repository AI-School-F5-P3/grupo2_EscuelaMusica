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