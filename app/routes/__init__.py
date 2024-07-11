# app/routes/__init__.py

from flask import Blueprint

students_bp = Blueprint('students', __name__)
teachers_bp = Blueprint('teachers', __name__)
levels_bp = Blueprint('levels', __name__)
instruments_bp = Blueprint('instruments', __name__)
enrollments_bp = Blueprint('enrollments', __name__)
