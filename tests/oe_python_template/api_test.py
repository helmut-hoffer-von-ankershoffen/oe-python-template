"""Tests to verify the API functionality of OE Python Template."""

import pytest
from fastapi.testclient import TestClient

from oe_python_template.api import api


@pytest.fixture
def client() -> TestClient:
    """Provide a FastAPI test client fixture."""
    return TestClient(api)


def test_root_endpoint_returns_404(client: TestClient) -> None:
    """Test that the root endpoint returns a 404 status code."""
    response = client.get("/")
    assert response.status_code == 404
    assert "Not Found" in response.json()["detail"]
