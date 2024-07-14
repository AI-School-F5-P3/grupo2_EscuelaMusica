from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar extensiones
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
migrate = Migrate()

password = quote_plus("rocio99")
engine = create_engine(f'mysql+pymysql://root:{password}@localhost:3306/armonia_utopia', pool_pre_ping=True)
Session = sessionmaker(bind=engine)

# Crea las tablas en la base de datos si no existen
db.metadata.create_all(engine)




def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicializar extensiones con la aplicación
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

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
