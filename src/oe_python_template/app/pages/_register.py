"""Register pages of app."""

from ._index import register_index


def register_pages() -> None:
    """Register pages of app."""
    register_index()
