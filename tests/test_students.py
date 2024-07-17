import pytest
from flask import json
from app import create_app, db
from app.models import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()
    yield db
    db.drop_all()

def test_create_student(test_client, init_database):
    response = test_client.post('/students', json={
        "first_name": "John",
        "last_name": "Doe",
        "age": 20,
        "phone": "123-456-7890",
        "email": "john.doe@example.com"
    })

    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id_student" in data
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"

def test_get_student(test_client, init_database):
    # Primero, creamos un estudiante
    test_client.post('/students', json={
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 22,
        "phone": "098-765-4321",
        "email": "jane.smith@example.com"
    })

    # Luego, intentamos obtenerlo
    response = test_client.get('/students/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id_student"] == 1
    assert data["first_name"] == "Jane"
    assert data["last_name"] == "Smith"

def test_update_student(test_client, init_database):
    # Primero, creamos un estudiante
    test_client.post('/students', json={
        "first_name": "Michael",
        "last_name": "Johnson",
        "age": 25,
        "phone": "555-123-4567",
        "email": "michael.johnson@example.com"
    })

    # Luego, intentamos actualizarlo
    response = test_client.put('/students/1', json={
        "age": 26
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["age"] == 26

def test_delete_student(test_client, init_database):
    # Primero, creamos un estudiante
    test_client.post('/students', json={
        "first_name": "Emily",
        "last_name": "Williams",
        "age": 21,
        "phone": "789-012-3456",
        "email": "emily.williams@example.com"
    })

    # Luego, intentamos eliminarlo
    response = test_client.delete('/students/1')
    assert response.status_code == 200

    # Verificamos que ya no existe
    response = test_client.get('/students/1')
    assert response.status_code == 404

def test_get_all_students(test_client, init_database):
    # Creamos varios estudiantes
    test_client.post('/students', json={
        "first_name": "Student1",
        "last_name": "Last1",
        "age": 20,
        "phone": "111-111-1111",
        "email": "student1@example.com"
    })
    test_client.post('/students', json={
        "first_name": "Student2",
        "last_name": "Last2",
        "age": 21,
        "phone": "222-222-2222",
        "email": "student2@example.com"
    })

    # Obtenemos todos los estudiantes
    response = test_client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 2  # Debería haber al menos 2 estudiantes
