"""System module."""

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


from importlib.util import find_spec

# advertise PageBuuilder to enable auto-discovery
if find_spec("nicegui"):
    from ._gui import PageBuilder

    __all__ += [
        "PageBuilder",
    ]

# Export all individual API routers so they are picked up by depdency injection (DI)
for version, router in api_routers.items():
    router_name = f"api_{version}"
    globals()[router_name] = router
    del router
