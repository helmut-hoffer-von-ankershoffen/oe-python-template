"""Copier template to scaffold Python projects compliant with best practices and modern tooling."""

from .constants import (
    __project_name__,
    __project_path__,
    __version__,
)

from .service import Service

__all__ = [
    "__project_name__",
    "__project_path__",
    "__version__",
    "Service",
]
