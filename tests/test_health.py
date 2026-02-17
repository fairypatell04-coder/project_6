from fastapi.testclient import TestClient
from services.app.main import app   # ← use your real app module

client = TestClient(app)

def test_docs():
    r = client.get("/docs")
    assert r.status_code == 200

def test_metrics(client):
    res = client.get("/metrics")
    assert res.status_code == 200
