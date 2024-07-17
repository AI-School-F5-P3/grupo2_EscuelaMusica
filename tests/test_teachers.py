def test_create_teacher(client, init_database, auth_header):
    response = client.post('/teachers', json={
        'name': 'Test Teacher',
        'email': 'test_teacher@example.com'
    }, headers=auth_header)
    assert response.status_code == 201

def test_get_teacher(client, init_database, auth_header):
    response = client.get('/teachers/1', headers=auth_header)
    assert response.status_code == 200

def test_update_teacher(client, init_database, auth_header):
    response = client.put('/teachers/1', json={
        'name': 'Updated Teacher',
        'email': 'updated_teacher@example.com'
    }, headers=auth_header)
    assert response.status_code == 200

def test_delete_teacher(client, init_database, auth_header):
    response = client.delete('/teachers/1', headers=auth_header)
    assert response.status_code == 200

def test_get_all_teachers(client, init_database, auth_header):
    response = client.get('/teachers', headers=auth_header)
    assert response.status_code == 200

def test_add_instrument_to_teacher(client, init_database, auth_header):
    response = client.post('/teachers/1/instruments', json={
        'instrument_id': 1
    }, headers=auth_header)
    assert response.status_code == 200

def test_get_teacher_instruments(client, init_database, auth_header):
    response = client.get('/teachers/1/instruments', headers=auth_header)
    assert response.status_code == 200

