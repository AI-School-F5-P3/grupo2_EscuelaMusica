from tabulate import tabulate
from sqlalchemy import create_engine #Se usa para crear un motor de bbdd
from sqlalchemy import Column, Integer, String, Boolean, Float, Enum, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from faker import Faker #pip install faker
from __init__ import db

# Definimos los modelos correspondientes a las tablas de la base de datos
class Student(db.Models):
    __tablename__ = 'students'

    id_student = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(20))
    #enrollments = relationship('Enrollment', backref='student')
    
class Teacher(db.Models):
    __tablename__ = 'teachers'

    id_teacher = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_teacher = db.Column(db.String(20))
    last_name = db.Column(String(20))
    telphone = db.Column(String(20))
    email = db.Column(String(20))
    rel_instrument = db.relationship('Instrument', secondary='teachers_instruments',backref='instruments_teacher') #relación de regreso

class Instrument(db.Models):
    __tablename__ = 'instruments'
    id_instrument = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument = db.Column(db.String(20), nullable=False)

    rel_levels = db.relationship('Level',secondary="instruments_levels", backref='back_levels')
    #enrollments = relationship('Enrollment', backref='instrument')

    #Creación de una columna para que identifique Price
    #pack_id = Column(Integer, ForeignKey('price_instrument.id_price'))
class Level(db.Models):
    __tablename__ = 'levels'
    id_level = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_level = db.Column(db.String(25))
    #----instrument_level= relationship('InstrumentLevel', backref='level') #----------------

class TeacherInstrument(db.Models): #Parece ser que no es necesario
    __tablename__ = 'teachers_instruments'    
    id_teacher = db.Column('id_teacher',db.Integer, ForeignKey('teachers.id_teacher'), primary_key=True)
    id_instrument = db.Column('id_instrument',db.Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    #id_level = Column(Integer, ForeignKey('levels.id_level'))

class InstrumentLevel(db.Models): ##Parece ser que no es necesario
    __tablename__ = 'instruments_levels'
    id_instrument = db.Column(db.Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    id_level = db.Column(db.Integer, ForeignKey('levels.id_level'), primary_key=True)

""" class PriceInstrument(db.Models):
    __tablename__ = 'price_instrument'

    id_price = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pack = db.Column(db.String(10))
    pack_price = db.Column(db.Float)

    #enrollments = relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')
    instruments = relationship("Instrument", backref="pack")
 """



    
# Configura la conexión a la base de datos
#engine = create_engine('mysql+pymysql://root:"Fausto-007"@localhost:3306/')
#Session = sessionmaker(bind=engine)
#conn=engine.connect()

#def get_session():
    #return db.session()

#db.session=Session()
#-------------------------| FIN de creación de estructuras tablas |------------------
#Hay que añadirle esto
#db.Models.metadata.create_all(engine)

relations = {
    "Mar":["Piano", "Guitarra", "Batería", "Flauta"],
    "Flor":["Piano", "Guitarra"],
    "Álvaro": ["Piano"],
    "Marifé": ["Piano", "Canto"],
    "Nayara": ["Piano", "Violín", "Bajo"],
    "Sofía": ["Percusión"]
}

#db.session = Session()


teachers = []
instruments = []

for name, instrument_list in relations.items():
    teacher = Teacher(name_teacher=name)
    db.session.add(teacher)
    teachers.append(teacher)
    
    for instrument_name in instrument_list:
        instrument = db.session.query(Instrument).filter_by(instrument=instrument_name).first()
        if not instrument:
            instrument = Instrument(instrument=instrument_name)
            db.session.add(instrument)
        instruments.append(instrument)
        teacher.rel_instrument.append(instrument)

db.session.flush() #guardar las relaciones en la tabla puente utilizando el método flush de la sesión.

#--------| Commit the changes ----------
db.session.commit()

#------| Crea las tablas en la base de datos si no existen  |-------------
#db.Models.metadata.create_all(engine)

#*********************************** RELATIONS *****************************
relations_levels= {
    "Piano":["Cero", "Iniciación", "Medio", "Avanzado"],
    "Guitarra":["Iniciación", "Medio"],
    "Batería": ["Iniciación", "Medio", "Avanzado"],
    "Flauta": ["Iniciación", "Medio"],
    "Bajo": ["Iniciación", "Medio"],
    "Violin": ["Cero"],
    "Canto":["Cero"],
    "Saxofon":["Cero"],
    "Clarinete":["Cero"],
    "Percusion":["Cero"]
    }
        
for i, valor in relations_levels.items():
    varinstrument = db.session.query(Instrument).filter_by(instrument=i).first()
    if not varinstrument:
        varinstrument = Instrument(instrument=i)
        db.session.add(varinstrument)
    for level_name in valor:
        varlevel = db.session.query(Level).filter_by(name_level=level_name).first()
        if not varlevel:
            varlevel = Level(name_level=level_name)
            db.session.add(varlevel)
        varinstrument.rel_levels.append(varlevel)        
                
db.session.flush()
db.session.commit()
#db.Models.metadata.create_all(engine)

#////////////////////////////////////////////////////////////////////////////////////
students = [
    {"first_name": "John", "last_name": "Doe", "age": 20, "phone": "123-456-7890", "email": "john.doe@example.com"},
    {"first_name": "Jane", "last_name": "Smith", "age": 22, "phone": "098-765-4321", "email": "jane.smith@example.com"},
    {"first_name": "Michael", "last_name": "Johnson", "age": 25, "phone": "555-123-4567", "email": "michael.johnson@example.com"},
    {"first_name": "Emily", "last_name": "Williams", "age": 21, "phone": "789-012-3456", "email": "emily.williams@example.com"},
 ]

for student in students:
    new_student = Student(**student)
    db.session.add(new_student)
db.session.commit()

result = db.session.query(Student).all()

fake=Faker()
names=["Mar", "Flor", "Nayara", "Marifé", "Álvaro", "Nieves", "Sofía"]
for i in range(7):
    teacher=Teacher(
      name_teacher=names[i],
      last_name=fake.last_name(),
      telphone=fake.phone_number(),
      email=fake.email()
    )
    db.session.add(teacher)

list=["Piano", "Guitarra", "Bateria","Violin","Canto", "Flauta","Saxofon","Clarinete", "Percusión", "Bajo"]
for i in range(len(list)):
    instruments=Instrument(
        instrument=list[i]
    )
    db.session.add(instruments)

list_level=['cero', 'iniciacion', 'medio', 'avanzado']
for i in range(len(list_level)):
    level=Level(
        name_level=list_level[i]
    )
    db.session.add(level)

""" Es para hacer una consulta en mysql--------------

SELECT t.name_teacher, i.instrument
FROM teachers t
JOIN teachers_instruments ti ON t.id_teacher = ti.id_teacher
JOIN instruments i ON ti.id_instrument = i.id_instrument;

"""
db.session.commit()

""" 
result = db.session.query(Student).all()
print(tabulate([row.__dict__ for row in result], headers="keys"))  # Imprime una tabla con los atributos y valores

"""

""" 
Me lo saca como un diccionario

from pprint import pprint

result = db.session.query(Student).all()
for row in result:
    pprint(row.__dict__)  # 
"""
