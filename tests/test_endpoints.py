import logging
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_healthz():
    response = client.get("/api/healthz")
    assert response.status_code == 204

def test_not_found():
    response = client.get("/notfound")
    assert response.status_code == 404

def test_classify_1():
    response = client.post("/api/classify")
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}]}

def test_classify_2():
    payload = {
        "text": "L'équipe de France joue aujourd'hui au Parc des Princes"
    }
    response = client.post("/api/classify", json=payload)
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "labels"], "msg": "field required", "type": "value_error.missing"}]}

def test_classify_3():
    payload = {
        "labels": ["sport","politique","science"],
        "text": "L'équipe de France joue aujourd'hui au Parc des Princes"
    }
    response = client.post("/api/classify", json=payload)
    assert response.status_code == 200
    assert response.json()["predictions"][0]["score"] > 99