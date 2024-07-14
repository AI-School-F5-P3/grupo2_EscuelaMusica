# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import db

# Configura la conexión a la base de datos
<<<<<<< HEAD
engine = create_engine('mysql://root:1319@localhost/armonia1')
=======
engine = create_engine('mysql://root:3306@localhost/armonia_utopia')
>>>>>>> d28e4fe4d6bfc66ba28a4fd5cdf18cdc5e3532f4
Session = sessionmaker(bind=engine)

# Crea las tablas en la base de datos si no existen
db.metadata.create_all(engine)