# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db

# Configura la conexión a la base de datos
engine = create_engine('mysql://username:password@localhost/ArmoniaUtopia')
Session = sessionmaker(bind=engine)

# Crea las tablas en la base de datos si no existen
db.metadata.create_all(engine)

