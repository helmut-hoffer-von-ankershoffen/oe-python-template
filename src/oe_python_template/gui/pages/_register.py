"""Register pages of GUI."""

from ._index import register_index


def register_pages() -> None:
    """Register pages of GUI."""
    register_index()
