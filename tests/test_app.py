from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_should_return_ok_and_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World :)'}


def test_html_hello_world_works_well(hello_world_html_string):
    client = TestClient(app)

    response = client.get('/html_hello_world')

    assert response.status_code == HTTPStatus.OK
    assert response.text == hello_world_html_string
