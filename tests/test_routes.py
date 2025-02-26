import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_endpoint_valid(client):
    response = client.post('/api/chat', json={'message': 'Hello'})
    assert response.status_code == 200
    data = response.get_json()
    assert "response" in data

def test_chat_endpoint_invalid(client):
    response = client.post('/api/chat', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
