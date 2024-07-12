# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db

# Configura la conexión a la base de datos
<<<<<<< HEAD
engine = create_engine('mysql://username:password@localhost/armonia_utopia')
=======
engine = create_engine('mysql://username:password@localhost/ArmoniaUtopia')
>>>>>>> 1c1b9334719f2bac87909f46f9ad5f730134490c
Session = sessionmaker(bind=engine)

# Crea las tablas en la base de datos si no existen
db.metadata.create_all(engine)

