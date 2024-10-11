from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "Backend is running smoothly",
        "api_version": "1.0.0",
        "message": "Welcome to the Bus Arrival Prediction API"
    }
