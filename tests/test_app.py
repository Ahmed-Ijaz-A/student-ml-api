from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert body["application"] == "student-ml-api"
    assert body["application_version"] == "1.1.0"
    assert body["model_version"] == "model-1"

def test_predict_success():
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    assert response.json()["prediction"] == 20

def test_predict_missing_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422

def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "not-a-number"})
    assert response.status_code == 422