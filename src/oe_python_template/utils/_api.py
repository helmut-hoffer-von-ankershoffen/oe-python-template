"""API router utilities for versioned FastAPI routers."""

from typing import ClassVar


class VersionedAPIRouter:
    """APIRouter with version attribute.

    - Use this class to create versioned routers for your FastAPI application
        that are automatically registered into the FastAPI app.
    - The version attribute is used to identify the version of the API
        that the router corresponds to.
    - See constants.por versions defined for this system.
    """

    # Class variable to track all created instances
    _instances: ClassVar[list["VersionedAPIRouter"]] = []

    @classmethod
    def get_instances(cls) -> list["VersionedAPIRouter"]:
        """Get all created router instances.

        Returns:
            A list of all router instances created.
        """
        return cls._instances.copy()

    def __new__(cls, version: str, *args, **kwargs) -> "VersionedAPIRouter":  # type: ignore[no-untyped-def]
        """Create a new instance with lazy-loaded dependencies.

        Args:
            version: The API version this router belongs to.
            *args: Arguments to pass to the FastAPI APIRouter.
            **kwargs: Keyword arguments to pass to the FastAPI APIRouter.

        Returns:
            An instance of VersionedAPIRouter with lazy-loaded dependencies.
        """
        from fastapi import APIRouter  # Import only when creating an instance  # noqa: PLC0415

        # Define the actual implementation class with the imports available
        class VersionedAPIRouterImpl(APIRouter):
            """Implementation of VersionedAPIRouter with lazy-loaded dependencies."""

            version: str

            def __init__(self, version: str, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
                """Initialize the router.

                Args:
                    version: The API version this router belongs to.
                    *args: Arguments to pass to the FastAPI APIRouter.
                    **kwargs: Keyword arguments to pass to the FastAPI APIRouter.
                """
                super().__init__(*args, **kwargs)
                self.version = version

        # Create an instance
        instance = VersionedAPIRouterImpl(version, *args, **kwargs)

        # Add to registry of instances
        cls._instances.append(instance)  # type: ignore

        # Return the instance but tell mypy it's a VersionedAPIRouter
        return instance  # type: ignore[return-value]
