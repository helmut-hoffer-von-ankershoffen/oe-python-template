"""System service."""

from collections.abc import Callable
from typing import Any

import marimo
from fastapi import APIRouter, FastAPI

from ..utils import (  # noqa: TID252
    BaseService,
    Health,
    get_logger,
)
from ._settings import Settings

logger = get_logger(__name__)


def register_health_endpoint(router: APIRouter) -> Callable[..., Health]:
    """Register health endpoint to the given router.

    Args:
        router: The router to register the health endpoint to.

    Returns:
        Callable[..., Health]: The health endpoint function.
    """

    @router.get("/healthz")
    def health_endpoint() -> Health:
        """Determine health of the app.

        Returns:
            Health: Health.
        """
        return Health(status=Health.Code.UP)

    return health_endpoint


class Service(BaseService):
    """System service."""

    _settings: Settings

    def __init__(self) -> None:
        """Initialize service."""
        super().__init__(Settings)

    def health(self) -> Health:  # noqa: PLR6301
        """Determine aggregate health of the system.

        - Health exposed by implementations of BaseService in other
            modules is automatically included into the health tree.
        - See utils/_health.py:Health for an explanation of the health tree.

        Returns:
            Health: The aggregate health of the system.
        """
        return Health(status=Health.Code.UP)

    @staticmethod
    def info() -> dict[str, Any]:
        """
        Get info about configuration of service.

        Returns:
            dict[str, Any]: Service configuration.
        """
        # Nothing yet
        return {}

    def create_marimo_app(self) -> FastAPI:
        """Create a FastAPI app with marimo notebook server.

        Returns:
            FastAPI: FastAPI app with marimo notebook server.

        Raises:
            ValueError: If the notebook directory does not exist.
        """
        server = marimo.create_asgi_app(include_code=True)
        if not self._settings.directory.is_dir():
            logger.critical(
                "Directory %s does not exist. Please create the directory and add your notebooks.",
                self._settings.directory,
            )
            message = f"Directory {self._settings.directory} does not exist. Please create and add your notebooks."
            raise ValueError(message)
        server = server.with_app(path="/", root=str(self._settings.directory / "notebook.py"))
        #            .with_dynamic_directory(path="/dashboard", directory=str(self._settings.directory))
        app = FastAPI()
        router = APIRouter(tags=["marimo"])
        register_health_endpoint(router)
        app.include_router(router)
        app.mount("/", server.build())
        return app
