def test_create_instrument(client, init_database, auth_header):
    response = client.post('/instruments', json={
        'name': 'Guitar'
    }, headers=auth_header)
    assert response.status_code == 201

def test_get_instrument(client, init_database, auth_header):
    response = client.get('/instruments/1', headers=auth_header)
    assert response.status_code == 200

def test_update_instrument(client, init_database, auth_header):
    response = client.put('/instruments/1', json={
        'name': 'Electric Guitar'
    }, headers=auth_header)
    assert response.status_code == 200

def test_delete_instrument(client, init_database, auth_header):
    response = client.delete('/instruments/1', headers=auth_header)
    assert response.status_code == 200

def test_get_all_instruments(client, init_database, auth_header):
    response = client.get('/instruments', headers=auth_header)
    assert response.status_code == 200

def test_add_level_to_instrument(client, init_database, auth_header):
    response = client.post('/instruments/1/levels', json={
        'level_id': 1
    }, headers=auth_header)
    assert response.status_code == 200

def test_get_instrument_levels(client, init_database, auth_header):
    response = client.get('/instruments/1/levels', headers=auth_header)
    assert response.status_code == 200
