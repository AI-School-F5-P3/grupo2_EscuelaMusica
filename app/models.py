from .db import db

class Student(db.Model):
    __tablename__ = 'students'
    id_student = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))

    enrollments = db.relationship('Enrollment', backref='student')

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id_teacher = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_teacher = db.Column(db.String(255), nullable=False)

    instruments = db.relationship('TeacherInstrument', backref='teacher')

class Level(db.Model):
    __tablename__ = 'levels'
    id_level = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_level = db.Column(db.String(255))

    instruments = db.relationship('InstrumentLevel', backref='level')

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id_instrument = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument = db.Column(db.String(255), nullable=False)

    teacher_instruments = db.relationship('TeacherInstrument', backref='instrument')
    instrument_levels = db.relationship('InstrumentLevel', backref='instrument')
    enrollments = db.relationship('Enrollment', backref='instrument')

class TeacherInstrument(db.Model):
    __tablename__ = 'teachers_instruments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_teacher = db.Column(db.Integer, db.ForeignKey('teachers.id_teacher'))
    id_instrument = db.Column(db.Integer, db.ForeignKey('instruments.id_instrument'))
    id_level = db.Column(db.Integer, db.ForeignKey('levels.id_level'))

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_student = db.Column(db.Integer, db.ForeignKey('students.id_student'))
    id_level = db.Column(db.Integer, db.ForeignKey('levels.id_level'))
    id_instrument = db.Column(db.Integer, db.ForeignKey('instruments.id_instrument'))
    id_teacher = db.Column(db.Integer, db.ForeignKey('teachers.id_teacher'))
    base_price = db.Column(db.Float)
    final_price = db.Column(db.Float)
    family_discount = db.Column(db.Boolean)

class PriceInstrument(db.Model):
    __tablename__ = 'price_instrument'
    id_price = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pack = db.Column(db.Enum('pack1', 'pack2', 'pack3'))
    pack_price = db.Column(db.Float)

    enrollments = db.relationship('Enrollment', secondary='price_instrument_enrollments', backref='price_instrument')

class Discount(db.Model):
    __tablename__ = 'discount'
    id_discount = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_discount = db.Column(db.Enum('pack1', 'pack2', 'pack3'))
    count_instrument = db.Column(db.Integer)
    discount_percentage = db.Column(db.Float)

    enrollments = db.relationship('Enrollment', secondary='discount_enrollments', backref='discount')

class InstrumentLevel(db.Model):
    __tablename__ = 'instruments_levels'
    instruments_id_instrument = db.Column(db.Integer, db.ForeignKey('instruments.id_instrument'), primary_key=True)
    levels_id_level = db.Column(db.Integer, db.ForeignKey('levels.id_level'), primary_key=True)

class PriceInstrumentEnrollment(db.Model):
    __tablename__ = 'price_instrument_enrollments'
    price_instrument_pack = db.Column(db.Enum('pack1', 'pack2', 'pack3'), primary_key=True)
    enrollments_base_price = db.Column(db.Float, primary_key=True)

class DiscountEnrollment(db.Model):
    __tablename__ = 'discount_enrollments'
    discount_discount_percentage = db.Column(db.Float, primary_key=True)
    enrollments_final_price = db.Column(db.Float, primary_key=True)
