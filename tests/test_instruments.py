import pytest
from flask import json
from app import create_app, db
from app.models import Instrument, Level, PriceInstrument

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()
    
    # Crear un pack de precios para las pruebas
    price_pack = PriceInstrument(pack="Test_Pack", pack_price=50.0)
    db.session.add(price_pack)
    db.session.commit()
    
    yield db
    db.drop_all()

def test_create_instrument(test_client, init_database):
    response = test_client.post('/instruments', json={
        "instrument": "Guitar",
        "pack_id": 1  # Asumiendo que el pack creado en init_database tiene id 1
    })

    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id_instrument" in data
    assert data["instrument"] == "Guitar"

def test_get_instrument(test_client, init_database):
    # Primero, creamos un instrumento
    test_client.post('/instruments', json={
        "instrument": "Piano",
        "pack_id": 1
    })

    # Luego, intentamos obtenerlo
    response = test_client.get('/instruments/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id_instrument"] == 1
    assert data["instrument"] == "Piano"

def test_update_instrument(test_client, init_database):
    # Primero, creamos un instrumento
    test_client.post('/instruments', json={
        "instrument": "Drums",
        "pack_id": 1
    })

    # Luego, intentamos actualizarlo
    response = test_client.put('/instruments/1', json={
        "instrument": "Electric Drums"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["instrument"] == "Electric Drums"

def test_delete_instrument(test_client, init_database):
    # Primero, creamos un instrumento
    test_client.post('/instruments', json={
        "instrument": "Violin",
        "pack_id": 1
    })

    # Luego, intentamos eliminarlo
    response = test_client.delete('/instruments/1')
    assert response.status_code == 200

    # Verificamos que ya no existe
    response = test_client.get('/instruments/1')
    assert response.status_code == 404

def test_get_all_instruments(test_client, init_database):
    # Creamos varios instrumentos
    test_client.post('/instruments', json={
        "instrument": "Flute",
        "pack_id": 1
    })
    test_client.post('/instruments', json={
        "instrument": "Clarinet",
        "pack_id": 1
    })

    # Obtenemos todos los instrumentos
    response = test_client.get('/instruments')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 2  # Debería haber al menos 2 instrumentos

def test_add_level_to_instrument(test_client, init_database):
    # Primero, creamos un instrumento y un nivel
    test_client.post('/instruments', json={
        "instrument": "Saxophone",
        "pack_id": 1
    })
    test_client.post('/levels', json={
        "name_level": "Beginner"
    })

    # Luego, añadimos el nivel al instrumento
    response = test_client.post('/instruments/1/levels', json={
        "id_level": 1
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "Beginner" in [level["name_level"] for level in data["rel_levels"]]

def test_get_instrument_levels(test_client, init_database):
    # Asumiendo que ya tenemos un instrumento con niveles
    response = test_client.get('/instruments/1/levels')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0  # Debería haber al menos un nivel
