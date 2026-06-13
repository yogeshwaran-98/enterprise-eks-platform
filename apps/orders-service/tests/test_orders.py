from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_orders():
    response = client.get("/orders")

    assert response.status_code == 200