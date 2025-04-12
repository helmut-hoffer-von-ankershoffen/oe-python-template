"""Tests to verify the API functionality of the hello module."""

import pytest
from fastapi.testclient import TestClient

from oe_python_template.api import app

HELLO_WORLD_PATH_V1 = "/api/v1/hello/world"
HELLO_WORLD_PATH_V2 = "/api/v2/hello/world"

ECHO_PATH_V1 = "/api/v1/hello/echo"
ECHO_PATH_V2 = "/api/v2/hello/echo"

HELLO_WORLD = "Hello, world!"


@pytest.fixture
def client() -> TestClient:
    """Provide a FastAPI test client fixture."""
    return TestClient(app)


def test_hello_world_endpoint(client: TestClient) -> None:
    """Test that the hello-world endpoint returns the expected message."""
    response = client.get(HELLO_WORLD_PATH_V1)
    assert response.status_code == 200
    assert response.json()["message"].startswith(HELLO_WORLD)

    response = client.get(HELLO_WORLD_PATH_V2)
    assert response.status_code == 200
    assert response.json()["message"].startswith(HELLO_WORLD)


def test_echo_endpoint_valid_input(client: TestClient) -> None:
    """Test that the echo endpoint returns the input text."""
    test_text = "Test message"

    response = client.get(f"{ECHO_PATH_V1}/{test_text}")
    assert response.status_code == 200
    assert response.json() == {"text": test_text.upper()}

    response = client.post(ECHO_PATH_V2, json={"text": test_text})
    assert response.status_code == 200
    assert response.json() == {"text": test_text.upper()}


def test_echo_endpoint_empty_text(client: TestClient) -> None:
    """Test that the echo endpoint validates empty text."""
    response = client.post(ECHO_PATH_V2, json={"text": ""})
    assert response.status_code == 422  # Validation error


def test_echo_endpoint_missing_text(client: TestClient) -> None:
    """Test that the echo endpoint validates missing text field."""
    response = client.get(ECHO_PATH_V1)
    assert response.status_code == 404  # Not found

    response = client.post(ECHO_PATH_V2, json={})
    assert response.status_code == 422  # Validation error
