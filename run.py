from app import create_app, db
<<<<<<< HEAD
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
=======
>>>>>>> 192f38db33b52b6933ee1b3372958f77151642f0

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Base de datos inicializada correctamente.")
<<<<<<< HEAD
    app.run()
=======
    app.run()
>>>>>>> 192f38db33b52b6933ee1b3372958f77151642f0
