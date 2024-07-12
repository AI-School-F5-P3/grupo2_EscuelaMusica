# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Configura la conexión a la base de datos
engine = create_engine('mysql://root:3306@localhost/armonia_utopia')
Session = sessionmaker(bind=engine)

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

