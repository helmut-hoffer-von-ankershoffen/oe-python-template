"""API operations of system module.

This module provides a webservice API with several operations:
- A health/healthz endpoint that returns the health status of the service

The endpoints use Pydantic models for request and response validation.
"""

from collections.abc import Callable, Generator
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from ..constants import API_VERSIONS  # noqa: TID252
from ..utils import Health, VersionedAPIRouter  # noqa: TID252
from ._service import Service


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


def register_health_endpoint(router: APIRouter) -> Callable[..., Health]:
    """Register health endpoint to the given router.

    Args:
        router: The router to register the health endpoint to.

    Returns:
        Callable[..., Health]: The health endpoint function.
    """

    @router.get("/healthz")
    @router.get("/health")
    def health_endpoint(service: Annotated[Service, Depends(get_service)], response: Response) -> Health:
        """Check the health of the system.

        This operation returns the health of the system.
        The status can be either UP or DOWN.
        If the service is healthy, the status will be UP.
        If the service is unhealthy, the status will be DOWN and a reason will be provided.
        The response will have a 200 OK status code if the service is healthy,
        and a 500 Internal Server Error status code if the service is unhealthy.

        Returns:
            Health: The health of the system.
        """
        health = service.health()
        if health.status == Health.Status.DOWN:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return health

    return health_endpoint


api_routers = {}
for version in API_VERSIONS:
    router = VersionedAPIRouter(version, tags=["system"])
    api_routers[version] = router
    health = register_health_endpoint(api_routers[version])
