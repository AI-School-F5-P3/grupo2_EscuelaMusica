from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError
from faker import Faker

db = SQLAlchemy()

# Definición de modelos
class Student(db.Model):
    __tablename__ = 'students'
    id_student = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id_teacher = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_teacher = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    telphone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    rel_instrument = db.relationship('Instrument', secondary='teachers_instruments', backref='instruments_teacher')

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id_instrument = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument = db.Column(db.String(20), nullable=False)
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

    for name, instrument_list in relations.items():
        teacher = Teacher(name_teacher=name)
        db.session.add(teacher)
        for instrument_name in instrument_list:
            instrument = Instrument.query.filter_by(instrument=instrument_name).first()
            if not instrument:
                instrument = Instrument(instrument=instrument_name)
                db.session.add(instrument)
            teacher.rel_instrument.append(instrument)

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

    for instrument_name, level_names in relations_levels.items():
        instrument = Instrument.query.filter_by(instrument=instrument_name).first()
        if not instrument:
            instrument = Instrument(instrument=instrument_name)
            db.session.add(instrument)
        for level_name in level_names:
            level = Level.query.filter_by(name_level=level_name).first()
            if not level:
                level = Level(name_level=level_name)
                db.session.add(level)
            instrument.rel_levels.append(level)

    students = [
        {"first_name": "John", "last_name": "Doe", "age": 20, "phone": "123-456-7890", "email": "john.doe@example.com"},
        {"first_name": "Jane", "last_name": "Smith", "age": 22, "phone": "098-765-4321", "email": "jane.smith@example.com"},
        {"first_name": "Michael", "last_name": "Johnson", "age": 25, "phone": "555-123-4567", "email": "michael.johnson@example.com"},
        {"first_name": "Emily", "last_name": "Williams", "age": 21, "phone": "789-012-3456", "email": "emily.williams@example.com"},
    ]

    for student_data in students:
        student = Student(**student_data)
        db.session.add(student)

    fake = Faker()
    names = ["Mar", "Flor", "Nayara", "Marifé", "Álvaro", "Nieves", "Sofía"]
    for name in names:
        teacher = Teacher(
            name_teacher=name,
            last_name=fake.last_name(),
            telphone=fake.phone_number(),
            email=fake.email()
        )
        db.session.add(teacher)

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
        db.create_all()
        populate_database()