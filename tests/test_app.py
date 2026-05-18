import pytest
from fastapi.testclient import TestClient

from app import app, ENV_KEYS

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_test_endpoint(monkeypatch):
    monkeypatch.setitem(ENV_KEYS, "key1", "valor_falso_1")
    monkeypatch.setitem(ENV_KEYS, "key2", "valor_falso_2")

    response = client.get("/test")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Env variables loaded"
    assert {"key": "key1", "value": "valor_falso_1"} in data["values"]
