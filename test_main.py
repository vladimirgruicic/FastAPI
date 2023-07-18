# File: tests/test_user.py

import pytest
from fastapi.testclient import TestClient
from main import app  # Use an absolute import


@pytest.fixture
def client():
    return TestClient(app)

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the Home page!" in response.text