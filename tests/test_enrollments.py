import pytest
from flask import json
from app import create_app, db
from app.models import Student, Instrument, Enrollment
from datetime import date

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()

    # Crear datos de prueba
    student = Student(first_name="Test", last_name="Student", age=20, phone="123-456-7890", email="test@example.com")
    instrument = Instrument(instrument="Piano")
    db.session.add(student)
    db.session.add(instrument)
    db.session.commit()

    yield db

    db.drop_all()

def test_create_enrollment(test_client, init_database):
    response = test_client.post('/enrollments', json={
        "id_student": 1,
        "id_instrument": 1,
        "enrollment_date": str(date.today()),
        "name_student": "Test",
        "lastname_student": "Student",
        "family": False
    })

    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id_enrollment" in data
    assert data["name_student"] == "Test"
    assert data["lastname_student"] == "Student"

def test_get_enrollment(test_client, init_database):
    # Primero, creamos una inscripción
    test_client.post('/enrollments', json={
        "id_student": 1,
        "id_instrument": 1,
        "enrollment_date": str(date.today()),
        "name_student": "Test",
        "lastname_student": "Student",
        "family": False
    })

    # Luego, intentamos obtenerla
    response = test_client.get('/enrollments/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id_enrollment"] == 1
    assert data["name_student"] == "Test"
    assert data["lastname_student"] == "Student"

def test_update_enrollment(test_client, init_database):
    # Primero, creamos una inscripción
    test_client.post('/enrollments', json={
        "id_student": 1,
        "id_instrument": 1,
        "enrollment_date": str(date.today()),
        "name_student": "Test",
        "lastname_student": "Student",
        "family": False
    })

    # Luego, intentamos actualizarla
    response = test_client.put('/enrollments/1', json={
        "family": True
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["family"] == True

def test_delete_enrollment(test_client, init_database):
    # Primero, creamos una inscripción
    test_client.post('/enrollments', json={
        "id_student": 1,
        "id_instrument": 1,
        "enrollment_date": str(date.today()),
        "name_student": "Test",
        "lastname_student": "Student",
        "family": False
    })

    # Luego, intentamos eliminarla
    response = test_client.delete('/enrollments/1')
    assert response.status_code == 200

    # Verificamos que ya no existe
    response = test_client.get('/enrollments/1')
    assert response.status_code == 404

def test_get_final_price(test_client, init_database):
    # Primero, creamos una inscripción
    test_client.post('/enrollments', json={
        "id_student": 1,
        "id_instrument": 1,
        "enrollment_date": str(date.today()),
        "name_student": "Test",
        "lastname_student": "Student",
        "family": False
    })

    # Luego, obtenemos el precio final
    response = test_client.get('/enrollments/1/final-price')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "final_price" in data
    assert isinstance(data["final_price"], float)
