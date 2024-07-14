# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import db

# Configura la conexión a la base de datos
engine = create_engine('mysql://root:1319@localhost/armonia1')
Session = sessionmaker(bind=engine)

# Crea las tablas en la base de datos si no existen
db.metadata.create_all(engine)