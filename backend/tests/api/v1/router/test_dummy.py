from fastapi.testclient import TestClient

from app.core.config import settings


def test_echo(client: TestClient):
    data = {"msg": "dummy_msg"}
    resp = client.post(url=f"{settings.API_V1_STR}/dummy/echo", json=data)
    resp_body = resp.json()
    assert resp_body["msg"] == "dummy_msg"
