from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .config import config_dict
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import os
from app.utils.app_logging import setup_logger
import pymysql
pymysql.install_as_MySQLdb()


# Cargar variables de entorno
load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    setup_logger(app)

    from .routes import students_bp, teachers_bp, levels_bp, instruments_bp, enrollments_bp
    app.register_blueprint(students_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(levels_bp)
    app.register_blueprint(instruments_bp)
    app.register_blueprint(enrollments_bp)

    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    app.run()

