"""Hello module."""

from ._api import api_v1, api_v2
from ._cli import cli
from ._models import Echo, Utterance
from ._service import Service
from ._settings import Settings

__all__ = [
    "Echo",
    "Service",
    "Settings",
    "Utterance",
    "api_v1",
    "api_v2",
    "cli",
]


from importlib.util import find_spec

# advertise PageBuuilder to enable auto-discovery
if find_spec("nicegui"):
    from ._gui import PageBuilder

    __all__ += [
        "PageBuilder",
    ]
