"""Tests to verify the API functionality of the hello module."""

from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from requests.models import Response

from oe_python_template.api import api

HEALTH_PATH_V1 = "/api/v1/system/health"
HEALTH_PATH_V2 = "/api/v2/system/health"

HEALTHZ_PATH_V1 = "/api/v1/healthz"
HEALTHZ_PATH_V2 = "/api/v2/healthz"

HELLO_WORLD_PATH_V1 = "/api/v1/hello/world"
HELLO_WORLD_PATH_V2 = "/api/v2/hello/world"

ECHO_PATH_V1 = "/api/v1/hello/echo"
ECHO_PATH_V2 = "/api/v2/hello/echo"

HELLO_WORLD = "Hello, world!"

SERVICE_UP = "UP"
SERVICE_DOWN = "DOWN"
STATUS = "status"
COMPONENTS = "components"
COMPONENT_ID = "oe_python_template.hello._service.Service"
REASON = "reason"


@pytest.fixture
def client() -> TestClient:
    """Provide a FastAPI test client fixture."""
    return TestClient(api)


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


@patch("requests.get")
def test_health_endpoint_down(mock_requests_get, client: TestClient) -> None:
    """Test that the health endpoint returns 503 status when service is unhealthy.

    This test mocks the request to the connectivity check URL to return a 404 status code
    instead of the expected 204 (No Content), which should cause the hello service's
    _determine_connectivity method to report DOWN status, making the aggregate health go DOWN.
    """
    # Create a mock response with status_code 404
    mock_response = Response()
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response

    # Check v1 health endpoints
    response = client.get(HEALTH_PATH_V1)
    assert response.status_code == 503  # Service Unavailable
    assert response.json()[STATUS] == SERVICE_DOWN
    assert COMPONENT_ID in response.json()[REASON]
    assert "Component 'connectivity' is DOWN" in response.json()[COMPONENTS][COMPONENT_ID][REASON]
    assert (
        response.json()[COMPONENTS][COMPONENT_ID][COMPONENTS]["connectivity"][REASON]
        == "Unexpected response status: 404"
    )

    response = client.get(HEALTHZ_PATH_V1)
    assert response.status_code == 503
    assert response.json()[STATUS] == SERVICE_DOWN
    assert COMPONENT_ID in response.json()[REASON]

    # Check v2 health endpoints
    response = client.get(HEALTH_PATH_V2)
    assert response.status_code == 503
    assert response.json()[STATUS] == SERVICE_DOWN
    assert COMPONENT_ID in response.json()[REASON]

    response = client.get(HEALTHZ_PATH_V2)
    assert response.status_code == 503
    assert response.json()[STATUS] == SERVICE_DOWN
    assert COMPONENT_ID in response.json()[REASON]

    # Verify our mock was called with the correct URL
    mock_requests_get.assert_called_with("https://connectivitycheck.gstatic.com/generate_204", timeout=5)
