from fastapi import APIRouter


class VersionedAPIRouter(APIRouter):
    """APIRouter with version attribute."""

    version: str

    def __init__(self, version: str, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self.version = version
