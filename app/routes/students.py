from flask import Blueprint, request, jsonify
from app.models import Student
from app.schemas import student_schema, students_schema
from app import db
from flask_jwt_extended import jwt_required

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
@jwt_required()
def add_student():
    # Implementación...

@students_bp.route('/students', methods=['GET'])
@jwt_required()
def get_students():
    # Implementación...

# Resto de las rutas...
