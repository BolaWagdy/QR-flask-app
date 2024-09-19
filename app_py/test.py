import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_qr_code_generation(client):
    response = client.post('/', data={})
    assert response.status_code == 400

def test_invalid_data(client):
    response = client.post('/', data={})
    assert response.status_code == 400