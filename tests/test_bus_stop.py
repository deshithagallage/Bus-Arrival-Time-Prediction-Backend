from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test case for get bus stop by ID
def test_read_stop():
    stop_id = "00AXLneAkJFXla02jsdc"
    response = client.get(f"/api/bus_stops/{stop_id}")
    assert response.status_code == 200
    assert response.json()["id"] == stop_id

# Test case for get bus stop by ID when stop is not found
def test_read_stop_not_found():
    stop_id = "1234"
    response = client.get(f"/api/bus_stops/{stop_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Bus stop not found"}

# Test case for get bus stop by name
def test_read_stop_by_name():
    stop_name = "BERGEN ST/BEDFORD AV"
    response = client.get(f"/api/bus_stops/by-name/{stop_name}")
    assert response.status_code == 200
    assert response.json()["name"] == stop_name

# Test case for get bus stop by name when stop is not found
def test_read_stop_by_name_not_found():
    stop_name = "Wrong Name"
    response = client.get(f"/api/bus_stops/by-name/{stop_name}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Bus stop not found"}
