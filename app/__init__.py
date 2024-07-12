from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

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
