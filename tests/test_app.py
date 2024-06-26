from http import HTTPStatus


def test_root_should_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World :)'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'arnaldo',
            'email': 'arnaldo@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'arnaldo',
        'email': 'arnaldo@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'arnaldo',
                'email': 'arnaldo@example.com',
                'id': 1,
            }
        ]
    }


def test_read_single_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'arnaldo',
        'email': 'arnaldo@example.com',
        'id': 1,
    }


def test_read_single_user_not_found(client):
    response = client.get('/users/322')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'vitor',
            'email': 'vitor@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'vitor',
        'email': 'vitor@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/322',
        json={
            'username': 'vitor',
            'email': 'vitor@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/322')

    assert response.status_code == HTTPStatus.NOT_FOUND
