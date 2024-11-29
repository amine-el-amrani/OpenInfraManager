import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    with app.test_client() as client:
        yield client


def test_create_server_success(client):
    payload = {
        "name": "MyServer",
        "image_id": "12345",
        "flavor_id": "abcd",
        "network_id": "6789"
    }
    response = client.post("/api/servers", json=payload)

    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data["status"] == "created"
    assert response_data["details"] == payload

def test_create_server_missing_fields(client):
    payload = {
        "name": "TestServer"
    }
    response = client.post("/api/servers", json=payload)

    assert response.status_code == 404
    response_data = response.get_json()
    assert "error" in response_data

def test_list_servers_success(client):
    response = client.get("/api/servers")

    assert response.status_code == 200

    response_data = response.get_json()
    assert response_data["status"] == "success"