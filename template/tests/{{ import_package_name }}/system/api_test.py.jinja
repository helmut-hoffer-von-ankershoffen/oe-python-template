"""Tests to verify the API functionality of the system module."""

from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from oe_python_template.api import app
from oe_python_template.system._service import Service

HEALTH_PATH_V1 = "/api/v1/system/health"
HEALTH_PATH_V2 = "/api/v2/system/health"

HEALTHZ_PATH_V1 = "/api/v1/healthz"
HEALTHZ_PATH_V2 = "/api/v2/healthz"

SERVICE_UP = "UP"
SERVICE_DOWN = "DOWN"
REASON = "reason"
STATUS = "status"
SERVICE_IS_UNHEALTHY = "System marked as unhealthy"

INFO_PATH_V1 = "/api/v1/system/info"
INFO_PATH_V2 = "/api/v2/system/info"

RUNTIME = "runtime"
ENVIRONMENT = "environment"


@pytest.fixture
def client() -> TestClient:
    """Provide a FastAPI test client fixture."""
    return TestClient(app)


def test_health_endpoint(client: TestClient) -> None:
    """Test that the health endpoint returns UP status."""
    response = client.get(HEALTH_PATH_V1)
    assert response.status_code == 200
    assert response.json()[STATUS] == SERVICE_UP
    assert response.json()[REASON] is None

    response = client.get(HEALTH_PATH_V2)
    assert response.status_code == 200
    assert response.json()[STATUS] == SERVICE_UP
    assert response.json()[REASON] is None

    response = client.get(HEALTHZ_PATH_V1)
    assert response.status_code == 200
    assert response.json()[STATUS] == SERVICE_UP
    assert response.json()[REASON] is None

    response = client.get(HEALTHZ_PATH_V2)
    assert response.status_code == 200
    assert response.json()[STATUS] == SERVICE_UP
    assert response.json()[REASON] is None


def test_health_endpoint_down(client: TestClient) -> None:
    """Test that the health endpoint returns 503 status when service is unhealthy.

    We patch the _is_healthy method to return False, simulating an unhealthy service.
    """
    # Patch the _is_healthy method to always return False
    with patch.object(Service, "_is_healthy", return_value=False):
        # Test v1 health endpoints

        # Test v1 health endpoints
        response = client.get(HEALTHZ_PATH_V1)
        assert response.status_code == 503
        assert response.json()[STATUS] == SERVICE_DOWN
        assert SERVICE_IS_UNHEALTHY in response.json()[REASON]

        # Test v2 health endpoints
        response = client.get(HEALTH_PATH_V2)
        assert response.status_code == 503
        assert response.json()[STATUS] == SERVICE_DOWN
        assert SERVICE_IS_UNHEALTHY in response.json()[REASON]

        response = client.get(HEALTHZ_PATH_V2)
        assert response.status_code == 503
        assert response.json()[STATUS] == SERVICE_DOWN
        assert SERVICE_IS_UNHEALTHY in response.json()[REASON]


def test_info_endpoint(client: TestClient) -> None:
    """Test that the info endpoint returns what's expected."""
    response = client.get(INFO_PATH_V1)
    assert response.status_code == 422

    response = client.get(INFO_PATH_V2)
    assert response.status_code == 422

    response = client.get(f"{INFO_PATH_V1}?token=wrong")
    assert response.status_code == 403

    response = client.get(f"{INFO_PATH_V2}?token=wrong")
    assert response.status_code == 403

    # Test with valid token (patched validation)
    with patch.object(Service, "is_token_valid", return_value=True):
        response = client.get(f"{INFO_PATH_V1}?token=valid_token")
        assert response.status_code == 200
        assert RUNTIME in response.json()
        assert ENVIRONMENT in response.json()[RUNTIME]

        response = client.get(f"{INFO_PATH_V2}?token=valid_token")
        assert response.status_code == 200
        assert RUNTIME in response.json()
        assert ENVIRONMENT in response.json()[RUNTIME]
