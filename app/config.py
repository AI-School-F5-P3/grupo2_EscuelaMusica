import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:Fausto-007@localhost:3306/armonia_utopia')

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # Para pruebas, es mejor usar una base de datos en memoria
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI', 'mysql+pymysql://test_user:test_password@localhost:3306/test_armonia_utopia')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:Fausto-007@localhost:3306/armonia_utopia')

config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig}
