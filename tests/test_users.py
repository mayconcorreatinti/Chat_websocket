from fastapi.testclient import TestClient
from app.main import app
from http import HTTPStatus


def test_get_users():
    client = TestClient(app)
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK

def test_create_user():
    client = TestClient(app)
    response = client.post(
        '/users',json={
            'username': 'test_user',
            'email': 'test_use@gmail.com',
            'password': 'my_password'
        }
    )
    assert response.status_code == HTTPStatus.CREATED


