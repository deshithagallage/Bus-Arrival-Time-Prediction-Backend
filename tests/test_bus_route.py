from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test case for get all bus routes
def test_read_all_route_names():
    response = client.get("/api/bus_routes/all")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test case for get bus route by ID
def test_read_route():
    route_id = "2hbFiL0vXFhR62eaHrzb"
    response = client.get(f"/api/bus_routes/{route_id}")
    assert response.status_code == 200
    assert response.json()["id"] == route_id

# Test case for get bus route by ID when route is not found
def test_read_route_not_found():
    route_id = "1234"
    response = client.get(f"/api/bus_routes/{route_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Bus route not found"}

# Test case for get bus route by name
def test_read_route_by_name():
    route_name = "M50"
    direction = 0
    response = client.get(f"/api/bus_routes/by-name/{route_name}/{direction}")
    assert response.status_code == 200
    assert response.json()["name"] == route_name
    assert response.json()["direction"] == direction

# Test case for get bus route by name when route is not found
def test_read_route_by_name_not_found():
    route_name = "Wrong Name"
    direction = 1
    response = client.get(f"/api/bus_routes/by-name/{route_name}/{direction}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Bus route not found"}
