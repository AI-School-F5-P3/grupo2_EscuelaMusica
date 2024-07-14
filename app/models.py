from sqlalchemy import Column, Integer, String, Boolean, Float, Enum, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
#OJO. añadido aparte para solucionar 13 problemas:
from __init__ import db



# Definimos los modelos correspondientes a las tablas de la db.Model de datos
class Student(db.Model):
    __tablename__ = 'students'

    id_student = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)
    phone = Column(String(255))
    email = Column(String(255))

    enrollments = relationship('Enrollment', backref='student')

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id_teacher = Column(Integer, primary_key=True, autoincrement=True)
    name_teacher = Column(String(255), nullable=False)

    instruments = relationship('TeacherInstrument', backref='teacher')

class Level(db.Model):
    __tablename__ = 'levels'

    id_level = Column(Integer, primary_key=True, autoincrement=True)
    name_level = Column(String(255))

    instruments = relationship('InstrumentLevel', backref='level')

class Instrument(db.Model):
    __tablename__ = 'instruments'

    id_instrument = Column(Integer, primary_key=True, autoincrement=True)
    instrument = Column(String(255), nullable=False)

    teacher_instruments = relationship('TeacherInstrument', backref='instrument')
    instrument_levels = relationship('InstrumentLevel', backref='instrument')
    enrollments = relationship('Enrollment', backref='instrument')

class TeacherInstrument(db.Model):
    __tablename__ = 'teachers_instruments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_teacher = Column(Integer, ForeignKey('teachers.id_teacher'))
    id_instrument = Column(Integer, ForeignKey('instruments.id_instrument'))
    id_level = Column(Integer, ForeignKey('levels.id_level'))

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
    pack = Column(Enum('pack1', 'pack2', 'pack3'))
    pack_price = Column(Float)

    enrollments = relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')

class Discount(db.Model):
    __tablename__ = 'discount'

    id_discount = Column(Integer, primary_key=True, autoincrement=True)
    group_discount = Column(Enum('pack1', 'pack2', 'pack3'))
    count_instrument = Column(Integer)
    discount_percentage = Column(Float)

    enrollments = relationship('Enrollment', secondary='discount_enrollments', backref='discount')

class InstrumentLevel(db.Model):
    __tablename__ = 'instruments_levels'

    instruments_id_instrument = Column(Integer, ForeignKey('instruments.id_instrument'), primary_key=True)
    levels_id_level = Column(Integer, ForeignKey('levels.id_level'), primary_key=True)

class PriceInstrumentEnrollment(db.Model):
    __tablename__ = 'price_instrument_enrollments'

    price_instrument_pack = Column(Enum('pack1', 'pack2', 'pack3'), primary_key=True)
    enrollments_base_price = Column(Float, primary_key=True)

class DiscountEnrollment(db.Model):
    __tablename__ = 'discount_enrollments'

    discount_discount_percentage = Column(Float, primary_key=True)
    enrollments_final_price = Column(Float, primary_key=True)




