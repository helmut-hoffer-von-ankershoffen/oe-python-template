"""Webservice API of Hello module.

This module provides a webservice API with several operations:
- A hello/world operation that returns a greeting message
- A hello/echo endpoint that echoes back the provided text
"""

from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel, Field

from oe_python_template.utils import VersionedAPIRouter

from ._models import Echo, Utterance
from ._service import Service

HELLO_WORLD_EXAMPLE = "Hello, world!"

# VersionedAPIRouters exported by modules via their __init__.py are automatically registered
# and injected into the main API app, see ../api.py.
api_v1 = VersionedAPIRouter("v1", prefix="/hello", tags=["hello"])
api_v2 = VersionedAPIRouter("v2", prefix="/hello", tags=["hello"])


def get_service() -> Generator[Service, None, None]:
    """Get instance of Service.

    Yields:
        Service: The service instance.
    """
    service = Service()
    try:
        yield service
    finally:
        # Cleanup code if needed
        pass


class _HelloWorldResponse(BaseModel):
    """Response model for hello-world endpoint."""

    message: str = Field(
        ...,
        description="The hello world message",
        examples=[HELLO_WORLD_EXAMPLE],
    )


@api_v1.get("/world")
@api_v2.get("/world")
def hello_world(service: Annotated[Service, Depends(get_service)]) -> _HelloWorldResponse:
    """
    Return a hello world message.

    Returns:
        _HelloWorldResponse: A response containing the hello world message.
    """
    return _HelloWorldResponse(message=service.get_hello_world())


@api_v1.get("/echo/{text}")
def echo(text: str) -> Echo:
    """
    Echo back the provided text.

    Args:
        text (str): The text to echo.

    Returns:
        Echo: The echo.

    Raises:
        422 Unprocessable Entity: If text is not provided or empty.
    """
    return Service.echo(Utterance(text=text))


@api_v2.post("/echo")
def echo_v2(request: Utterance) -> Echo:
    """
    Echo back the provided utterance.

    Args:
        request (Utterance): The utterance to echo back.

    Returns:
        Echo: The echo.

    Raises:
        422 Unprocessable Entity: If utterance is not provided or empty.
    """
    return Service.echo(request)
