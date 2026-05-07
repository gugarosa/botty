from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_speech_unconfigured_returns_503() -> None:
    response = client.post("/speech", json={"audio_path": "/tmp/missing.ogg"})
    assert response.status_code == 503


def test_chat_unconfigured_returns_503() -> None:
    response = client.post("/chat", json={"message": "hi"})
    assert response.status_code == 503


def test_chat_rejects_empty() -> None:
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 422
