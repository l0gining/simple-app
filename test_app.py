import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"DevSecOps Lab Application" in response.data

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_user_endpoint(client):
    """Test user endpoint"""
    response = client.get('/api/user/testuser')
    assert response.status_code == 200
    assert b"testuser" in response.data

