from app import create_app, db

app = create_app('development')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Base de datos inicializada correctamente.")
    app.run()
