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
import random


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
    email = Column(String(200))
    rel_instrument = relationship('Instrument', secondary='teachers_instruments',backref='instruments_teacher') #relación de regreso


class Instrument(Base):
    __tablename__ = 'instruments'
    id_instrument = Column(Integer, primary_key=True, autoincrement=True)
    instrument = Column(String(20), nullable=False)

    rel_levels = relationship('Level',secondary="instruments_levels", backref='back_levels')
    #enrollments = relationship('Enrollment', backref='instrument')

    #Creación de una columna para que identifique Price. Lo he hecho así, usando una columna y no una tabla puente ya que es de one-to-many y se podía hacer de ambas ,aneras
    pack_id = Column(Integer, ForeignKey('price.id_pack'))

class Level(Base):
    __tablename__ = 'levels'

    id_level = Column(Integer, primary_key=True, autoincrement=True)
    name_level = Column(String(25))

    #----instrument_level= relationship('InstrumentLevel', backref='level') #----------------

    
class TeacherInstrument(Base): #Parece ser que no es necesario
    __tablename__ = 'teachers_instruments'
    
    id_teacher = Column('id_teacher',Integer, ForeignKey('teachers.id_teacher'), primary_key=True)
    id_instrument = Column('id_instrument',Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    #id_level = Column(Integer, ForeignKey('levels.id_level'))



class InstrumentLevel(Base): ##Parece ser que no es necesario
    __tablename__ = 'instruments_levels'

    id_instrument = Column(Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    id_level = Column(Integer, ForeignKey('levels.id_level'), primary_key=True)



class PriceInstrument(Base):
    __tablename__ = 'price'

    id_pack = Column(Integer, primary_key=True, autoincrement=True)
    pack = Column(String(10))
    pack_price = Column(Float)

    #enrollments = relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')
    instruments = relationship("Instrument", backref="pack")


class Enrollment(Base):
    __tablename__ = 'enrollments'
    id_enrollment = Column(Integer, primary_key=True, autoincrement=True)
    id_student = Column(Integer, ForeignKey('students.id_student'))
    id_instrument= Column(Integer, ForeignKey('instruments.id_instrument'))
    discount = Column(Float, default=0.0)
    
    student = relationship("Student", backref="enrollments")
    instrument = relationship("Instrument", backref="enroll")


    
# Configura la conexión a la base de datos
engine = create_engine('mysql+pymysql://root:''@localhost:3206/acad_discount')
Session = sessionmaker(bind=engine)
#conn=engine.connect()

def get_session():
    return Session()

sesion=Session()
#-------------------------| FIN de creación de estructuras tablas |------------------
#Hay que añadirle esto
Base.metadata.create_all(engine)

relations = {
    "Mar":["Piano", "Guitarra", "Bateria", "Flauta"],
    "Flor":["Piano", "Guitarra"],
    "Álvaro": ["Piano"],
    "Marifé": ["Piano", "Canto"],
    "Nayara": ["Piano", "Violín", "Bajo"],
    "Sofía": ["Percusion"]
}

sesion = Session()


teachers = []
instruments = []

for name, instrument_list in relations.items():
    teacher = Teacher(name_teacher=name)
    sesion.add(teacher)
    teachers.append(teacher)
    
    for instrument_name in instrument_list:
        instrument = sesion.query(Instrument).filter_by(instrument=instrument_name).first()
        if not instrument:
            instrument = Instrument(instrument=instrument_name)
            sesion.add(instrument)
        instruments.append(instrument)
        teacher.rel_instrument.append(instrument)


sesion.flush() #guardar las relaciones en la tabla puente utilizando el método flush de la sesión.

#--------| Commit the changes ----------
sesion.commit()

#------| Crea las tablas en la base de datos si no existen  |-------------
Base.metadata.create_all(engine)


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
    varinstrument = sesion.query(Instrument).filter_by(instrument=i).first()
    if not varinstrument:
        varinstrument = Instrument(instrument=i)
        sesion.add(varinstrument)
    for level_name in valor:
        varlevel = sesion.query(Level).filter_by(name_level=level_name).first()
        if not varlevel:
            varlevel = Level(name_level=level_name)
            sesion.add(varlevel)
        varinstrument.rel_levels.append(varlevel)        
        
        
        
sesion.flush()
sesion.commit()
Base.metadata.create_all(engine)




relations_packs = {
    "Pack_1":["Piano", "Guitarra", "Bateria", "Flauta"],
    "Pack_2":["Violin", "Bajo"],
    "Pack_3": ["Clarinete","Saxofon"],
    "Pack_4": ["Percusion", "Canto"],
}

list_packs={"Pack_1": 35, "Pack_2": 35, "Pack_3": 40, "Pack_4":40}
for key, value in list_packs.items():
    price = PriceInstrument(
        pack=key,
        pack_price=value
    )
    sesion.add(price)
    
    
""" 
for pack, instruments in relations_packs.items():
    price = PriceInstrument(
        pack=pack,
        pack_price=list_packs[pack]
    )
    sesion.add(price)
    sesion.flush()
    for instrument_name in instruments:
        instrument = Instrument(
            instrument=instrument_name,
            pack_id=price.id_pack
        )
        sesion.add(instrument)
 """

for pack, instruments in relations_packs.items():
    price = sesion.query(PriceInstrument).filter_by(pack=pack).first()
    for instrument_name in instruments:
        instrument = sesion.query(Instrument).filter_by(instrument=instrument_name).first()
        if not instrument:
            instrument = Instrument(instrument=instrument_name, pack=price)
            sesion.add(instrument)
        else:
            instrument.pack = price







#////////////////////////////////////////////////////////////////////////////////////
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

""" 
list=["Piano", "Guitarra", "Bateria","Violin","Canto", "Flauta","Saxofon","Clarinete", "Percusión", "Bajo"]
for i in range(len(list)):
    instruments=Instrument(
        instrument=list[i]
    )
    sesion.add(instruments)

 """

list_level=['cero', 'iniciacion', 'medio', 'avanzado']
for i in range(len(list_level)):
    level=Level(
        name_level=list_level[i]
    )
    sesion.add(level)


try:
    students = sesion.query(Student).all()
    instruments = sesion.query(Instrument).all()

    if not students or not instruments:
        print("No hay estudiantes o instrumentos en la base de datos.")
    else:
        for student in students:
            instrument = random.choice(instruments)
            enrollment = Enrollment(
                id_student=student.id_student,
                id_instrument=instrument.id_instrument
            )
            sesion.add(enrollment)

    sesion.commit()
    print("Inscripciones creadas con éxito.")
except Exception as e:
    print(f"Error al crear inscripciones: {e}")
    sesion.rollback()


""" for instrument in relations_packs[key]:
    instrument_obj = Instrument(
        instrument=instrument,
        pack_id=price.id_pack
    )
    sesion.add(instrument_obj)

 """


#-------------------------------------------Consultas mysql para comprobar---------------------------------
""" Es para hacer una consulta en mysql--------------

SELECT t.name_teacher, i.instrument
FROM teachers t
JOIN teachers_instruments ti ON t.id_teacher = ti.id_teacher
JOIN instruments i ON ti.id_instrument = i.id_instrument;




SELECT p.pack, i.instrument
FROM price p
JOIN instruments i ON p.id_pack = i.pack_id
ORDER BY p.pack;


"""

sesion.commit()

""" 
result = sesion.query(Student).all()
print(tabulate([row.__dict__ for row in result], headers="keys"))  # Imprime una tabla con los atributos y valores

"""


def enroll_student(student_id, instrument_id):
    student = sesion.query(Student).get(student_id)
    new_instrument = sesion.query(Instrument).get(instrument_id)
    
    # Verificar si el estudiante ya está inscrito en otro instrumento del mismo pack
    existing_enrollments = sesion.query(Enrollment).filter_by(id_student=student_id).all()
    for enrollment in existing_enrollments:
        if enrollment.instrument.pack_id == new_instrument.pack_id:
            # Aplicar descuento a ambas inscripciones
            enrollment.discount = 0.5
            new_enrollment = Enrollment(id_student=student_id, id_instrument=instrument_id, discount=0.5)
            sesion.add(new_enrollment)
            sesion.commit()
            return "Descuento aplicado"
    
    # Si no hay coincidencia, crear una nueva inscripción sin descuento
    new_enrollment = Enrollment(id_student=student_id, id_instrument=instrument_id)
    sesion.add(new_enrollment)
    sesion.commit()
    return "Nueva inscripción creada"







def get_final_price(enrollment_id):
    enrollment = sesion.query(Enrollment).get(enrollment_id)
    pack_price = enrollment.instrument.pack.pack_price
    discount = enrollment.discount
    return pack_price * (1 - discount)




# Inscribimos a un estudiante en un instrumento
result = enroll_student(student_id=1, instrument_id=1)
print(result)

# Obtener el precio final de una inscripción, cada una
final_price = get_final_price(enrollment_id=1)
print(f"Precio final: {final_price}")




# Verificar las inscripciones
enrollments = sesion.query(Enrollment).filter_by(id_student=1).all()
if enrollments:
    for enrollment in enrollments:
        print(f"Inscripción: {enrollment.id_enrollment}, Estudiante: {enrollment.id_student}, Instrumento: {enrollment.id_instrument}")
else:
    print("No se encontraron inscripciones para el estudiante 1")


sesion.commit()
""" 
Me lo saca como un diccionario

from pprint import pprint

result = sesion.query(Student).all()
for row in result:
    pprint(row.__dict__)  # 
"""
