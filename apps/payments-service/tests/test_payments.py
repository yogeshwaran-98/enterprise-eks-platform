from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_payments():
    response = client.get("/payments")

    assert response.status_code == 200