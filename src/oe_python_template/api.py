"""Webservice API of OE Python Template.

This module provides a webservice API with several endpoints:
- A health/healthz endpoint that returns the health status of the service
- A hello-world endpoint that returns a greeting message
- An echo endpoint that echoes back the provided text

The endpoints use Pydantic models for request and response validation.
"""

from collections.abc import Generator
from enum import StrEnum
from typing import Annotated

from fastapi import Depends, FastAPI, Response, status
from pydantic import BaseModel, Field

from oe_python_template import Service

HELLO_WORLD_EXAMPLE = "Hello, world!"


def get_service() -> Generator[Service, None, None]:
    """Get the service instance.

    Yields:
        Service: The service instance.
    """
    service = Service()
    try:
        yield service
    finally:
        # Cleanup code if needed
        pass


app = FastAPI(
    version="1.0.0",
    title="OE Python Template",
    contact={
        "name": "Helmut Hoffer von Ankershoffen",
        "email": "helmuthva@gmail.com",
        "url": "https://github.com/helmut-hoffer-von-ankershoffen",
    },
    terms_of_service="https://oe-python-template.readthedocs.io/en/latest/",
)


class _HealthStatus(StrEnum):
    """Health status enumeration.

    Args:
        StrEnum (_type_): _description_
    """

    UP = "UP"
    DOWN = "DOWN"


class Health(BaseModel):
    """Health status model.

    Args:
        BaseModel (_type_): _description_
    """

    status: _HealthStatus
    reason: str | None = None


class HealthResponse(BaseModel):
    """Response model for health endpoint."""

    health: str = Field(
        ...,
        description="The hello world message",
        examples=[HELLO_WORLD_EXAMPLE],
    )


@app.get("/healthz", tags=["Observability"])
@app.get("/health", tags=["Observability"])
async def health(service: Annotated[Service, Depends(get_service)], response: Response) -> Health:
    """Check the health of the service.

    This endpoint returns the health status of the service.
    The health status can be either UP or DOWN.
    If the service is healthy, the status will be UP.
    If the service is unhealthy, the status will be DOWN and a reason will be provided.
    The response will have a 200 OK status code if the service is healthy,
    and a 500 Internal Server Error status code if the service is unhealthy.

    Args:
        service (Annotated[Service, Depends): _description_
        response (Response): _description_

    Returns:
        Health: The health status of the service.
    """
    if service.healthy():
        health_result = Health(status=_HealthStatus.UP)
    else:
        health_result = Health(status=_HealthStatus.DOWN, reason="Service is unhealthy")

    if health_result.status == _HealthStatus.DOWN:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return health_result


class HelloWorldResponse(BaseModel):
    """Response model for hello-world endpoint."""

    message: str = Field(
        ...,
        description="The hello world message",
        examples=[HELLO_WORLD_EXAMPLE],
    )


@app.get("/hello-world", tags=["Basics"])
async def hello_world() -> HelloWorldResponse:
    """
    Return a hello world message.

    Returns:
        HelloWorldResponse: A response containing the hello world message.
    """
    return HelloWorldResponse(message=Service.get_hello_world())


class EchoResponse(BaseModel):
    """Response model for echo endpoint."""

    message: str = Field(
        ...,
        min_length=1,
        description="The message content",
        examples=[HELLO_WORLD_EXAMPLE],
    )


class EchoRequest(BaseModel):
    """Request model for echo endpoint."""

    text: str = Field(
        ...,
        min_length=1,
        description="The text to echo back",
        examples=[HELLO_WORLD_EXAMPLE],
    )


@app.post("/echo", tags=["Basics"])
async def echo(request: EchoRequest) -> EchoResponse:
    """
    Echo back the provided text.

    Args:
        request (EchoRequest): The request containing the text to echo back.

    Returns:
        EchoResponse: A response containing the echoed text.

    Raises:
        422 Unprocessable Entity: If text is not provided or empty.
    """
    return EchoResponse(message=request.text)
