from tabulate import tabulate
from sqlalchemy import create_engine #Se usa para crear un motor de bbdd
from sqlalchemy import Column, Integer, String, Boolean, Float, Enum, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker #pip install faker
from __init__ import db

db.Model = declarative_base()
class Student(db.Model):
    __tablename__ = 'students'

    id_student = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    phone = Column(String(20))
    email = Column(String(20))
    #enrollments = relationship('Enrollment', backref='student')

    enrollments = relationship('Enrollment', backref='student')

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id_teacher = Column(Integer, primary_key=True, autoincrement=True)
    name_teacher = Column(String(20))
    last_name=Column(String(20))
    telphone = Column(String(20))
    email = Column(String(20))
    instruments = relationship('Instrument', secondary='teachers_instruments',backref='teacher')

    #instruments = relationship('TeacherInstrument', backref='teacher')
class Level(db.Model):
    __tablename__ = 'levels'

    id_level = Column(Integer, primary_key=True, autoincrement=True)
    name_level = Column(String(25))

    instruments = relationship('InstrumentLevel', backref='level')

class Instrument(db.Model):
    __tablename__ = 'instruments'

    id_instrument = Column(Integer, primary_key=True, autoincrement=True)
    instrument = Column(String(20), nullable=False)

    teacher_instruments = relationship('TeacherInstrument', backref='instrument')
    
    
    instrument_levels = relationship('Level',secondary="instruments_levels", backref='instruments')
    #enrollments = relationship('Enrollment', backref='instrument')

class TeacherInstrument(db.Model):
    __tablename__ = 'teachers_instruments'
    
    id_teacher = Column('id_teacher',Integer, ForeignKey('teachers.id_teacher'), primary_key=True)
    id_instrument = Column('id_instrument',Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    #id_level = Column(Integer, ForeignKey('levels.id_level'))

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_student = Column(Integer, ForeignKey('students.id_student'))
    id_level = Column(Integer, ForeignKey('levels.id_level'))
    id_instrument = Column(Integer, ForeignKey('instruments.id_instrument'))
    id_teacher = Column(Integer, ForeignKey('teachers.id_teacher'))
    base_price = Column(Float)
    final_price = Column(Float)
    family_discount = Column(Boolean)

class PriceInstrument(db.Model):
    __tablename__ = 'price_instrument'

    id_price = Column(Integer, primary_key=True, autoincrement=True)
    pack = Column(String(10))
    pack_price = Column(Float)

    #enrollments = relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')
class Discount(db.Model):
    __tablename__ = 'discount'

    id_discount = Column(Integer, primary_key=True, autoincrement=True)
    group_discount = Column(Enum('pack1', 'pack2', 'pack3'))
    count_instrument = Column(Integer)
    discount_percentage = Column(Float)

    enrollments = relationship('Enrollment', secondary='discount_enrollments', backref='discount')

class InstrumentLevel(db.Model):
    __tablename__ = 'instruments_levels'

    id_instrument = Column(Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    id_level = Column(Integer, ForeignKey('levels.id_level'), primary_key=True)

class PriceInstrumentEnrollment(db.Model):
    __tablename__ = 'price_instrument_enrollments'

    price_instrument_pack = Column(Enum('pack1', 'pack2', 'pack3'), primary_key=True)
    enrollments_base_price = Column(Float, primary_key=True)

class DiscountEnrollment(db.Model):
    __tablename__ = 'discount_enrollments'

    discount_discount_percentage = Column(Float, primary_key=True)
    enrollments_final_price = Column(Float, primary_key=True)
