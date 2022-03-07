import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture()
def client():
    yield TestClient(app)
