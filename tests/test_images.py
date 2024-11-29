import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    with app.test_client() as client:
        yield client

def test_list_images_sucess(client):
    response = client.get("/api/images")

    assert response.status_code == 200