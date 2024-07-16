import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, ForeignKey, delete
from sqlalchemy.exc import IntegrityError
from faker import Faker
from sqlalchemy import Float, ForeignKey #se agrego neuvo sugerencia claude

db = SQLAlchemy()

# Definición de modelos
class Student(db.Model):
    __tablename__ = 'students'
    id_student = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(20))

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id_teacher = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_teacher = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    telphone = db.Column(db.String(20))
    email = db.Column(db.String(20))
    rel_instrument = db.relationship('Instrument', secondary='teachers_instruments', backref='instruments_teacher')

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id_instrument = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument = db.Column(db.String(20), nullable=False)
    pack_id = db.Column(db.Integer, db.ForeignKey('price.id_pack')) # agregado nuevo sugerencia claude
    rel_levels = db.relationship('Level', secondary="instruments_levels", backref='back_levels')

class Level(db.Model):
    __tablename__ = 'levels'
    id_level = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_level = db.Column(db.String(25))

class TeacherInstrument(db.Model):
    __tablename__ = 'teachers_instruments'
    id_teacher = db.Column('id_teacher', db.Integer, db.ForeignKey('teachers.id_teacher'), primary_key=True)
    id_instrument = db.Column('id_instrument', db.Integer, db.ForeignKey('instruments.id_instrument'), primary_key=True)

class InstrumentLevel(db.Model):
    __tablename__ = 'instruments_levels'
    id_instrument = db.Column(db.Integer, db.ForeignKey('instruments.id_instrument'), primary_key=True)
    id_level = db.Column(db.Integer, db.ForeignKey('levels.id_level'), primary_key=True)

def reset_database():
    db.session.execute(delete(InstrumentLevel))
    db.session.execute(delete(TeacherInstrument))
    db.session.execute(delete(Level))
    db.session.execute(delete(Instrument))
    db.session.execute(delete(Teacher))
    db.session.execute(delete(Student))
    db.session.commit()
    
class PriceInstrument(db.Model):
    __tablename__ = 'price'

    id_pack = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pack = db.Column(db.String(10))
    pack_price = db.Column(Float)

    #enrollments = relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')
    instruments = db.relationship("Instrument", backref="pack", lazy='dynamic') # agregado nuevo sugerencia claude
    
class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id_enrollment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_student = db.Column(db.Integer, ForeignKey('students.id_student'))
    id_instrument= db.Column(db.Integer, ForeignKey('instruments.id_instrument'))
    discount= db.Column(db.Float, default=0.0)
    family_discount = db.Column(db.Boolean, default=False)

    
    student = db.relationship("Student", backref="enrollments")
    instrument = db.relationship("Instrument", backref="enroll")


def populate_database():
    reset_database()
    db.create_all()

    relations = {
        "Mar": ["Piano", "Guitarra", "Batería", "Flauta"],
        "Flor": ["Piano", "Guitarra"],
        "Álvaro": ["Piano"],
        "Marifé": ["Piano", "Canto"],
        "Nayara": ["Piano", "Violín", "Bajo"],
        "Sofía": ["Percusión"]
    }

    teachers = []
    instruments = []    

    for name, instrument_list in relations.items():
        teacher = Teacher(name_teacher=name)
        db.session.add(teacher)
        for instrument_name in instrument_list:
            instrument = Instrument.query.filter_by(instrument=instrument_name).first()
            if not instrument:
                instrument = Instrument(instrument=instrument_name)
                db.session.add(instrument)
            instruments.append(instrument)
            teacher.rel_instrument.append(instrument)
    
    db.session.flush()

    db.session.commit()
            
    
    #relations
    
    relations_levels = {
        "Piano": ["Cero", "Iniciación", "Medio", "Avanzado"],
        "Guitarra": ["Iniciación", "Medio"],
        "Batería": ["Iniciación", "Medio", "Avanzado"],
        "Flauta": ["Iniciación", "Medio"],
        "Bajo": ["Iniciación", "Medio"],
        "Violin": ["Cero"],
        "Canto": ["Cero"],
        "Saxofon": ["Cero"],
        "Clarinete": ["Cero"],
        "Percusion": ["Cero"]
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
        db.session.add(price)
    
    
    """ 
    for pack, instruments in relations_packs.items():
        price = PriceInstrument(
            pack=pack,
            pack_price=list_packs[pack]
        )
        db.session.add(price)
        db.session.flush()
        for instrument_name in instruments:
            instrument = Instrument(
            instrument=instrument_name,
                pack_id=price.id_pack
            )
            db.session.add(instrument)
     """

    for pack, instruments in relations_packs.items():
        price = db.session.query(PriceInstrument).filter_by(pack=pack).first()
        for instrument_name in instruments:
            instrument = db.session.query(Instrument).filter_by(instrument=instrument_name).first()
            if not instrument:
                instrument = Instrument(instrument=instrument_name, pack=price)
                db.session.add(instrument)
            else:
                instrument.pack = price
            
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
    
    fake = Faker()
    names = ["Mar", "Flor", "Nayara", "Marifé", "Álvaro", "Nieves", "Sofía"]
    for i in range(7):
        teacher=Teacher(
          name_teacher=names[i],
          last_name=fake.last_name(),
          telphone=fake.phone_number(),
          email=fake.email()
        )
        db.session.add(teacher)

    """ 
    list=["Piano", "Guitarra", "Bateria","Violin","Canto", "Flauta","Saxofon","Clarinete", "Percusión", "Bajo"]
    for i in range(len(list)):
        instruments=Instrument(
            instrument=list[i]
        )
        db.session.add(instruments)

     """
    
    list_level=['cero', 'iniciacion', 'medio', 'avanzado']
    for i in range(len(list_level)):
        level=Level(
            name_level=list_level[i]
        )
        db.session.add(level)

    try:
        students = db.session.query(Student).all()
        instruments = db.session.query(Instrument).all()

        if not students or not instruments:
            print("No hay estudiantes o instrumentos en la base de datos.")
        else:
            for student in students:
                instrument = random.choice(instruments)
                enrollment = Enrollment(
                    id_student=student.id_student,
                    id_instrument=instrument.id_instrument
                )
                db.session.add(enrollment)

        db.session.commit()
        print("Inscripciones creadas con éxito.")
    except Exception as e:
        print(f"Error al crear inscripciones: {e}")
        db.session.rollback()

    db.session.commit()


    def enroll_student(student_id, instrument_id):
        student = db.session.query(Student).get(student_id)
        new_instrument = db.session.query(Instrument).get(instrument_id)
    
        # Verificar si el estudiante ya está inscrito en otro instrumento del mismo pack
        existing_enrollments = db.session.query(Enrollment).filter_by(id_student=student_id).all()
        for enrollment in existing_enrollments:
            if enrollment.instrument.pack_id == new_instrument.pack_id:
                # Aplicar descuento a ambas inscripciones
                enrollment.discount = 0.5
                new_enrollment = Enrollment(id_student=student_id, id_instrument=instrument_id, discount=0.5)
                db.session.add(new_enrollment)
                db.session.commit()
                return "Descuento aplicado"
    
        # Si no hay coincidencia, crear una nueva inscripción sin descuento
        new_enrollment = Enrollment(id_student=student_id, id_instrument=instrument_id)
        db.session.add(new_enrollment)
        db.session.commit()
        return "Nueva inscripción creada"

    def get_final_price(enrollment_id):
        enrollment = db.session.query(Enrollment).get(enrollment_id)
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
    enrollments = db.session.query(Enrollment).filter_by(id_student=1).all()
    if enrollments:
        for enrollment in enrollments:
            print(f"Inscripción: {enrollment.id_enrollment}, Estudiante: {enrollment.id_student}, Instrumento: {enrollment.id_instrument}")
    else:
        print("No se encontraron inscripciones para el estudiante 1")

    db.session.commit()

    try:
        db.session.commit()
        print("Base de datos poblada exitosamente.")
    except IntegrityError as e:
        db.session.rollback()
        print(f"Error de integridad: {str(e)}")
    except Exception as e:
        db.session.rollback()
        print(f"Error inesperado: {str(e)}")

def init_db(app):
    with app.app_context():
        db.drop_all()  # Esto eliminará todas las tablas existente #se agrego nuevo sugerencia claude
        db.create_all()
        populate_database()
