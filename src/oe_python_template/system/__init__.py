"""Hello module."""

from ._api import api_routers
from ._cli import cli
from ._service import Service
from ._settings import Settings

__all__ = [
    "Service",
    "Settings",
    "api_routers",
    "cli",
]

# Export all individual API routers so they are picked up by depdency injection (DI)
for version, router in api_routers.items():
    router_name = f"api_{version}"
    globals()[router_name] = router
    del router
