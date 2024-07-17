def test_create_level(client, init_database, auth_header):
    response = client.post('/levels', json={
        'name': 'Beginner'
    }, headers=auth_header)
    assert response.status_code == 201

def test_get_level(client, init_database, auth_header):
    response = client.get('/levels/1', headers=auth_header)
    assert response.status_code == 200

def test_update_level(client, init_database, auth_header):
    response = client.put('/levels/1', json={
        'name': 'Intermediate'
    }, headers=auth_header)
    assert response.status_code == 200

def test_delete_level(client, init_database, auth_header):
    response = client.delete('/levels/1', headers=auth_header)
    assert response.status_code == 200

def test_get_all_levels(client, init_database, auth_header):
    response = client.get('/levels', headers=auth_header)
    assert response.status_code == 200

def test_add_instrument_to_level(client, init_database, auth_header):
    response = client.post('/levels/1/instruments', json={
        'instrument_id': 1
    }, headers=auth_header)
    assert response.status_code == 200

def test_get_level_instruments(client, init_database, auth_header):
    response = client.get('/levels/1/instruments', headers=auth_header)
    assert response.status_code == 200

