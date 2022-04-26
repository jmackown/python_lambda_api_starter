import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture(scope="session", autouse=True)
def test_client():
    with TestClient(app) as client:
        yield client
