#Primero hay que hacer la importación de las librerías de ALCHEMY
#pip install sqlalchemy
#pip install pymysql
from tabulate import tabulate #pip install tabulate
#Importación de los módulos
from sqlalchemy import create_engine #Se usa para crear un motor de bbdd
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import relationship
from faker import Faker #pip install faker


# Creamos una base para nuestros modelos
Base = declarative_base() #es una clase base para definiciones de clases declarativas.



# Definimos los modelos correspondientes a las tablas de la base de datos
class Student(Base):
    __tablename__ = 'students'

    id_student = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    phone = Column(String(20))
    email = Column(String(20))
    #enrollments = relationship('Enrollment', backref='student')
    

class Teacher(Base):
    __tablename__ = 'teachers'

    id_teacher = Column(Integer, primary_key=True, autoincrement=True)
    name_teacher = Column(String(20))
    last_name=Column(String(20))
    telphone = Column(String(20))
    email = Column(String(20))
    instruments = relationship('Instrument', secondary='teachers_instruments',backref='teacher')



class Instrument(Base):
    __tablename__ = 'instruments'

    id_instrument = Column(Integer, primary_key=True, autoincrement=True)
    instrument = Column(String(20), nullable=False)

    teacher_instruments = relationship('TeacherInstrument', backref='instrument')
    
    
    instrument_levels = relationship('Level',secondary="instruments_levels", backref='instruments')
    #enrollments = relationship('Enrollment', backref='instrument')
    

class Level(Base):
    __tablename__ = 'levels'

    id_level = Column(Integer, primary_key=True, autoincrement=True)
    name_level = Column(String(25))

    instrument_level= relationship('InstrumentLevel', backref='level') 

    
class TeacherInstrument(Base):
    __tablename__ = 'teachers_instruments'
    
    id_teacher = Column('id_teacher',Integer, ForeignKey('teachers.id_teacher'), primary_key=True)
    id_instrument = Column('id_instrument',Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    #id_level = Column(Integer, ForeignKey('levels.id_level'))



class InstrumentLevel(Base):
    __tablename__ = 'instruments_levels'

    id_instrument = Column(Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    id_level = Column(Integer, ForeignKey('levels.id_level'), primary_key=True)




class PriceInstrument(Base):
    __tablename__ = 'price_instrument'

    id_price = Column(Integer, primary_key=True, autoincrement=True)
    pack = Column(String(10))
    pack_price = Column(Float)

    #enrollments = relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')



    
# Configura la conexión a la base de datos
engine = create_engine('mysql+pymysql://root:''@localhost:3206/academia_test')
Session = sessionmaker(bind=engine)
#conn=engine.connect()

def get_session():
    return Session()

sesion=Session()
#-------------------------| FIN de creación de estructuras tablas |------------------
#Hay que añadirle esto
Base.metadata.create_all(engine)

relations = {
    "Mar":["Piano", "Guitarra", "Batería", "Flauta"],
    "Flor":["Piano", "Guitarra"],
    "Álvaro": ["Piano"],
    "Marifé": ["Piano", "Canto"],
    "Nayara": ["Piano", "Violín", "Bajo"],
    "Sofía": ["Percusión"]
}

sesion = Session()

relations = {
    "Mar":["Piano", "Guitarra", "Batería", "Flauta"],
    "Flor":["Piano", "Guitarra"],
    "Álvaro": ["Piano"],
    "Marifé": ["Piano", "Canto"],
    "Nayara": ["Piano", "Violín", "Bajo"],
    "Sofía": ["Percusión"]
}

sesion = Session()



for teacher_name, valor in relations.items():
    teacher = sesion.query(Teacher).filter_by(name_teacher=teacher_name).first()
    if not teacher:
        teacher = Teacher(name_teacher=teacher_name)
    for instrument_name in valor:
        instrument = sesion.query(Instrument).filter_by(instrument=instrument_name).first()
        if not instrument:
            instrument = Instrument(instrument=instrument_name)
        if instrument not in teacher.instruments:
            teacher.instruments.append(instrument)

sesion.flush()
sesion.commit()

sesion.flush() #guardar las relaciones en la tabla puente utilizando el método flush de la sesión.

#--------| Commit the changes ----------
sesion.commit()

#------| Crea las tablas en la base de datos si no existen  |-------------
Base.metadata.create_all(engine)


#*******************************************
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
    varlevel = sesion.query(Level).filter_by(name_level=i).first()
    if not varlevel:
        varlevel = Level(name_level=i)
        sesion.add(varlevel)
    for j in valor:
        varinstrument = sesion.query(Instrument).filter_by(instrument=j).first()
        if not varinstrument:
            varinstrument = Instrument(instrument=j)
            sesion.add(varinstrument)
        # Establecer la relación entre el instrumento y el nivel en la tabla instruments_levels
        varinstrument.instrument_levels.append(varlevel)
        sesion.add(varinstrument)
sesion.flush()
sesion.commit()
Base.metadata.create_all(engine)
            
            


#///////////////////////////////// INSERTADO LOS VALORES PROPIOS /////////////////////////////////////
students = [
    {"first_name": "John", "last_name": "Doe", "age": 20, "phone": "123-456-7890", "email": "john.doe@example.com"},
    {"first_name": "Jane", "last_name": "Smith", "age": 22, "phone": "098-765-4321", "email": "jane.smith@example.com"},
    {"first_name": "Michael", "last_name": "Johnson", "age": 25, "phone": "555-123-4567", "email": "michael.johnson@example.com"},
    {"first_name": "Emily", "last_name": "Williams", "age": 21, "phone": "789-012-3456", "email": "emily.williams@example.com"},
 ]

for student in students:
    new_student = Student(**student)
    sesion.add(new_student)
sesion.commit()


result = sesion.query(Student).all()

# Imprime los resultados
for row in result:
    print(row.first_name, row.last_name, row.age, row.phone, row.email) #Hay que imprimir a través de los atributos



fake=Faker()
names=["Mar", "Flor", "Nayara", "Marifé", "Álvaro", "Nieves", "Sofía"]
for i in range(7):
    teacher=Teacher(
      name_teacher=names[i],
      last_name=fake.last_name(),
      telphone=fake.phone_number(),
      email=fake.email()
    )
    sesion.add(teacher)


list=["Piano", "Guitarra", "Bateria","Violin","Canto", "Flauta","Saxofon","Clarinete", "Percusión", "Bajo"]
for i in range(len(list)):
    instruments=Instrument(
        instrument=list[i]
    )
    sesion.add(instruments)



list_level=['cero', 'iniciacion', 'medio', 'avanzado']
for i in range(len(list_level)):
    level=Level(
        name_level=list_level[i]
    )
    sesion.add(level)



list_packs={"Pack_1": 35, "Pack_2": 40, "Pack_3": 40, "Pack_4":40}
for key, value in list_packs.items():
    price = PriceInstrument(
        pack=key,
        pack_price=value
    )
    sesion.add(price)


""" Es para hacer una consulta en mysql--------------


#Primera relación------------

SELECT t.name_teacher, i.instrument
FROM teachers t
JOIN teachers_instruments ti ON t.id_teacher = ti.id_teacher
JOIN instruments i ON ti.id_instrument = i.id_instrument;






#Segunda relación----------

SELECT i.instrument, l.name_level
FROM instruments i
JOIN instruments_levels il ON i.id_instrument = il.id_instrument
JOIN levels l ON il.id_level = l.id_level
ORDER BY i.instrument;

#o también para ver esa consulta agrupada
SELECT i.instrument, GROUP_CONCAT(l.name_level) AS levels
FROM instruments i
JOIN instruments_levels il ON i.id_instrument = il.id_instrument
JOIN levels l ON il.id_level = l.id_level
GROUP BY i.instrument
ORDER BY i.instrument;


"""

sesion.commit()

""" 
result = sesion.query(Student).all()
print(tabulate([row.__dict__ for row in result], headers="keys"))  # Imprime una tabla con los atributos y valores

"""




""" 
Me lo saca como un diccionario

from pprint import pprint

result = sesion.query(Student).all()
for row in result:
    pprint(row.__dict__)  # 
"""




