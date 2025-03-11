"""Tests to verify the API functionality of OE Python Template."""

import pytest
from fastapi.testclient import TestClient

from oe_python_template.api import app

ECHO_PATH = "/echo"


@pytest.fixture
def client() -> TestClient:
    """Provide a FastAPI test client fixture."""
    return TestClient(app)


def test_root_endpoint_returns_404(client: TestClient) -> None:
    """Test that the root endpoint returns a 404 status code."""
    response = client.get("/")
    assert response.status_code == 404
    assert "Not Found" in response.json()["detail"]


def test_hello_world_endpoint(client: TestClient) -> None:
    """Test that the hello-world endpoint returns the expected message."""
    response = client.get("/hello-world")
    assert response.status_code == 200
    assert response.json()["message"].startswith("Hello, world!")


def test_echo_endpoint_valid_input(client: TestClient) -> None:
    """Test that the echo endpoint returns the input text."""
    test_text = "Test message"
    response = client.post(ECHO_PATH, json={"text": test_text})
    assert response.status_code == 200
    assert response.json() == {"message": test_text}


def test_echo_endpoint_empty_text(client: TestClient) -> None:
    """Test that the echo endpoint validates empty text."""
    response = client.post(ECHO_PATH, json={"text": ""})
    assert response.status_code == 422  # Validation error


def test_echo_endpoint_missing_text(client: TestClient) -> None:
    """Test that the echo endpoint validates missing text field."""
    response = client.post(ECHO_PATH, json={})
    assert response.status_code == 422  # Validation error
