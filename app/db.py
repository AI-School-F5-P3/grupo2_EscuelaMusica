from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

password = quote_plus("rocio99")
engine = create_engine(f'mysql+pymysql://root:{password}@localhost:3306/armonia_utopia', pool_pre_ping=True)
Session = sessionmaker(bind=engine)

db = SQLAlchemy()

# Crea las tablas en la base de datos si no existen
db.metadata.create_all(engine)

