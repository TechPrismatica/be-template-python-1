import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    from main import app

    client = TestClient(app)
    return client
