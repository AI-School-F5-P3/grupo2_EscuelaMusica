from flask_jwt_extended import create_access_token

def login_user(user):
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return access_token
