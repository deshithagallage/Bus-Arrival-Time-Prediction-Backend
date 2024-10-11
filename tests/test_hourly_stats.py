from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test case for successful response
def test_read_hourly_stats():
    route_name = "M50"
    day_of_week = "Monday"
    
    response = client.get(f"/api/hourly_stats/{route_name}/{day_of_week}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["route_name"] == route_name
    assert data["day_of_week"] == day_of_week
    assert "hourly_counts" in data

# Test case for non-existing route or day
def test_read_hourly_stats_not_found():
    route_name = "Wrong Route"
    day_of_week = "Friday"
    
    response = client.get(f"/api/hourly_stats/{route_name}/{day_of_week}")
    
    assert response.status_code == 404
    assert response.json() == {"detail": f"Hourly stats not found for route '{route_name}' on '{day_of_week}'"}
