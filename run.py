from app import create_app, db
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Base de datos inicializada correctamente.")
    app.run()