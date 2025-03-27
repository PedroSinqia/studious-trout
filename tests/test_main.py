from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cities_route_with_spain():
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "Madrid" in response.json()  # Substitua "Madrid" por uma cidade válida no seu JSON