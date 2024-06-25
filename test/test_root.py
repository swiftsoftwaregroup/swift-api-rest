from fastapi.testclient import TestClient
from swift_api_rest.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Swift API REST"}
