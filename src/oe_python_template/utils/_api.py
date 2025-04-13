from fastapi import APIRouter


class VersionedAPIRouter(APIRouter):
    """APIRouter with version attribute.

    - Use this class to create versioned routers for your FastAPI application
        that are automatically registered into the FastAPI app.
    - The version attribute is used to identify the version of the API
        that the router corresponds to.
    - See constants.por versions defined for this system.
    """

    version: str

    def __init__(self, version: str, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self.version = version
