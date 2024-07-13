import logging
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    """
    Configura el logging para la aplicación.
    
    :param app: La instancia de la aplicación Flask
    """
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)