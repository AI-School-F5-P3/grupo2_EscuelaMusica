from __init__ import create_app, db
from models import User

app = create_app()
with app.app_context():
    new_user = User(username='root')
    new_user.set_password('rocio99')
    db.session.add(new_user)
    db.session.commit()
    print("Usuario creado exitosamente")