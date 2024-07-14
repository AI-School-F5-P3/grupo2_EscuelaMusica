from app.models import Enrollment
from app.schemas import enrollment_schema, enrollments_schema
from app.__init__ import db

def add_enrollment(data):
    new_enrollment = Enrollment(**data)
    db.session.add(new_enrollment)
    db.session.commit()
    return enrollment_schema.jsonify(new_enrollment)

def get_all_enrollments():
    enrollments = Enrollment.query.all()
    return enrollments_schema.dump(enrollments)

def get_enrollment_by_id(enrollment_id):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    return enrollment_schema.jsonify(enrollment)

def update_enrollment(enrollment_id, data):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    for key, value in data.items():
        setattr(enrollment, key, value)
    db.session.commit()
    return enrollment_schema.jsonify(enrollment)

def delete_enrollment(enrollment_id):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    db.session.delete(enrollment)
    db.session.commit()
    return enrollment_schema.jsonify(enrollment)