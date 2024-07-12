from app import ma
from app.models import Student, Teacher, Level, Instrument, Enrollment, PriceInstrument, Discount, InstrumentLevel, PriceInstrumentEnrollment, DiscountEnrollment

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        include_fk = True

class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        include_fk = True

class LevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Level
        include_fk = True

class InstrumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Instrument
        include_fk = True

class EnrollmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Enrollment
        include_fk = True

class PriceInstrumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PriceInstrument
        include_fk = True

class DiscountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Discount
        include_fk = True

class InstrumentLevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InstrumentLevel
        include_fk = True

class PriceInstrumentEnrollmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PriceInstrumentEnrollment
        include_fk = True

class DiscountEnrollmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DiscountEnrollment
        include_fk = True

# Inicializamos los schemas
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)
level_schema = LevelSchema()
levels_schema = LevelSchema(many=True)
instrument_schema = InstrumentSchema()
instruments_schema = InstrumentSchema(many=True)
enrollment_schema = EnrollmentSchema()
enrollments_schema = EnrollmentSchema(many=True)
price_instrument_schema = PriceInstrumentSchema()
price_instruments_schema = PriceInstrumentSchema(many=True)
discount_schema = DiscountSchema()
discounts_schema = DiscountSchema(many=True)
instrument_level_schema = InstrumentLevelSchema()
instruments_levels_schema = InstrumentLevelSchema(many=True)
price_instrument_enrollment_schema = PriceInstrumentEnrollmentSchema()
price_instrument_enrollments_schema = PriceInstrumentEnrollmentSchema(many=True)
discount_enrollment_schema = DiscountEnrollmentSchema()
discount_enrollments_schema = DiscountEnrollmentSchema(many=True)
