import pytest
from flask import json
from app import create_app, db
from app.models import Level, Instrument

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

def test_create_level(test_client, init_database):
    response = test_client.post('/levels', json={
        "name_level": "Beginner"
    })

    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id_level" in data
    assert data["name_level"] == "Beginner"

def test_get_level(test_client, init_database):
    # Primero, creamos un nivel
    test_client.post('/levels', json={
        "name_level": "Intermediate"
    })

    # Luego, intentamos obtenerlo
    response = test_client.get('/levels/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id_level"] == 1
    assert data["name_level"] == "Intermediate"

def test_update_level(test_client, init_database):
    # Primero, creamos un nivel
    test_client.post('/levels', json={
        "name_level": "Advanced"
    })

    # Luego, intentamos actualizarlo
    response = test_client.put('/levels/1', json={
        "name_level": "Expert"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name_level"] == "Expert"

def test_delete_level(test_client, init_database):
    # Primero, creamos un nivel
    test_client.post('/levels', json={
        "name_level": "Master"
    })

    # Luego, intentamos eliminarlo
    response = test_client.delete('/levels/1')
    assert response.status_code == 200

    # Verificamos que ya no existe
    response = test_client.get('/levels/1')
    assert response.status_code == 404

def test_get_all_levels(test_client, init_database):
    # Creamos varios niveles
    test_client.post('/levels', json={
        "name_level": "Beginner"
    })
    test_client.post('/levels', json={
        "name_level": "Intermediate"
    })

    # Obtenemos todos los niveles
    response = test_client.get('/levels')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 2  # Debería haber al menos 2 niveles

def test_add_instrument_to_level(test_client, init_database):
    # Primero, creamos un nivel y un instrumento
    test_client.post('/levels', json={
        "name_level": "Advanced"
    })
    test_client.post('/instruments', json={
        "instrument": "Guitar",
        "pack_id": 1  # Asegúrate de que este pack_id exista en tu base de datos de prueba
    })

    # Luego, añadimos el instrumento al nivel
    response = test_client.post('/levels/1/instruments', json={
        "id_instrument": 1
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "Guitar" in [instrument["instrument"] for instrument in data["back_levels"]]

def test_get_level_instruments(test_client, init_database):
    # Asumiendo que ya tenemos un nivel con instrumentos
    response = test_client.get('/levels/1/instruments')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0  # Debería haber al menos un instrumento
