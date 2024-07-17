def test_create_enrollment(client, init_database, auth_header):
    response = client.post('/enrollments', json={
        'student_id': 1,
        'course_id': 1
    }, headers=auth_header)
    assert response.status_code == 201

def test_get_enrollment(client, init_database, auth_header):
    response = client.get('/enrollments/1', headers=auth_header)
    assert response.status_code == 200

def test_update_enrollment(client, init_database, auth_header):
    response = client.put('/enrollments/1', json={
        'student_id': 1,
        'course_id': 2
    }, headers=auth_header)
    assert response.status_code == 200

def test_delete_enrollment(client, init_database, auth_header):
    response = client.delete('/enrollments/1', headers=auth_header)
    assert response.status_code == 200

def test_get_final_price(client, init_database, auth_header):
    response = client.get('/enrollments/1/final_price', headers=auth_header)
    assert response.status_code == 200

