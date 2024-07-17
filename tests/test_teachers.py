import pytest
from flask import json
from app import create_app, db
from app.models import Teacher, Instrument

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

def test_create_teacher(test_client, init_database):
    response = test_client.post('/teachers', json={
        "name_teacher": "John",
        "last_name": "Doe",
        "telphone": "123-456-7890",
        "email": "john.doe@example.com"
    })

    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id_teacher" in data
    assert data["name_teacher"] == "John"
    assert data["last_name"] == "Doe"

def test_get_teacher(test_client, init_database):
    # Primero, creamos un profesor
    test_client.post('/teachers', json={
        "name_teacher": "Jane",
        "last_name": "Smith",
        "telphone": "098-765-4321",
        "email": "jane.smith@example.com"
    })

    # Luego, intentamos obtenerlo
    response = test_client.get('/teachers/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id_teacher"] == 1
    assert data["name_teacher"] == "Jane"
    assert data["last_name"] == "Smith"

def test_update_teacher(test_client, init_database):
    # Primero, creamos un profesor
    test_client.post('/teachers', json={
        "name_teacher": "Michael",
        "last_name": "Johnson",
        "telphone": "555-123-4567",
        "email": "michael.johnson@example.com"
    })

    # Luego, intentamos actualizarlo
    response = test_client.put('/teachers/1', json={
        "telphone": "555-987-6543"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["telphone"] == "555-987-6543"

def test_delete_teacher(test_client, init_database):
    # Primero, creamos un profesor
    test_client.post('/teachers', json={
        "name_teacher": "Emily",
        "last_name": "Williams",
        "telphone": "789-012-3456",
        "email": "emily.williams@example.com"
    })

    # Luego, intentamos eliminarlo
    response = test_client.delete('/teachers/1')
    assert response.status_code == 200

    # Verificamos que ya no existe
    response = test_client.get('/teachers/1')
    assert response.status_code == 404

def test_get_all_teachers(test_client, init_database):
    # Creamos varios profesores
    test_client.post('/teachers', json={
        "name_teacher": "Teacher1",
        "last_name": "Last1",
        "telphone": "111-111-1111",
        "email": "teacher1@example.com"
    })
    test_client.post('/teachers', json={
        "name_teacher": "Teacher2",
        "last_name": "Last2",
        "telphone": "222-222-2222",
        "email": "teacher2@example.com"
    })

    # Obtenemos todos los profesores
    response = test_client.get('/teachers')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 2  # Debería haber al menos 2 profesores

def test_add_instrument_to_teacher(test_client, init_database):
    # Primero, creamos un profesor y un instrumento
    test_client.post('/teachers', json={
        "name_teacher": "MusicTeacher",
        "last_name": "Instrumental",
        "telphone": "333-333-3333",
        "email": "music.teacher@example.com"
    })
    test_client.post('/instruments', json={
        "instrument": "Guitar",
        "pack_id": 1  # Asegúrate de que este pack_id exista en tu base de datos de prueba
    })

    # Luego, añadimos el instrumento al profesor
    response = test_client.post('/teachers/1/instruments', json={
        "id_instrument": 1
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "Guitar" in [instrument["instrument"] for instrument in data["rel_instrument"]]

def test_get_teacher_instruments(test_client, init_database):
    # Asumiendo que ya tenemos un profesor con instrumentos
    response = test_client.get('/teachers/1/instruments')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0  # Debería haber al menos un instrumento
