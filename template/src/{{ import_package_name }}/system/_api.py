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
        """Determine aggregate health of the system.

        The health is aggregated from all modules that make
            up this system including external dependencies.

        The response is to be interpreted as follows:
        - The status can be either UP or DOWN.
        - If the service is healthy, the status will be UP.
        - If the service is unhealthy, the status will be DOWN and a reason will be provided.
        - The response will have a 200 OK status code if the service is healthy,
            and a 503 Service Unavailable status code if the service is unhealthy.

        Args:
            service (Service): The service instance.
            response (Response): The FastAPI response object.

        Returns:
            Health: The health of the system.
        """
        health = service.health()
        if health.status == Health.Code.DOWN:
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

        return health

    return health_endpoint


api_routers = {}
for version in API_VERSIONS:
    router = VersionedAPIRouter(version, tags=["system"])
    api_routers[version] = router
    health = register_health_endpoint(api_routers[version])
