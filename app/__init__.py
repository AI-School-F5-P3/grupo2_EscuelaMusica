from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

#importar librerías para el Log:
import logging
from logging.handlers import RotatingFileHandler

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Configurar logging
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/escuela_de_musica.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('EscuelaDeMusica startup')


# Registrar rutas
from app.routes.students import students_bp
from app.routes.teachers import teachers_bp
from app.routes.levels import levels_bp
from app.routes.instruments import instruments_bp
from app.routes.enrollments import enrollments_bp

app.register_blueprint(students_bp)
app.register_blueprint(teachers_bp)
app.register_blueprint(levels_bp)
app.register_blueprint(instruments_bp)
app.register_blueprint(enrollments_bp)

from app.utils.logging import setup_logging
setup_logging()
