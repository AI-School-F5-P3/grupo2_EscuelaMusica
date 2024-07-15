from flask import Flask
from app.models import db, init_db
from app.frontend_routes import frontend_bp  # Importa el Blueprint
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI','mysql+pymysql://root:Fausto-007@localhost:3306/armonia_utopia')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(frontend_bp)
    db.init_app(app)
    
    with app.app_context():
        init_db(app)
     
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)