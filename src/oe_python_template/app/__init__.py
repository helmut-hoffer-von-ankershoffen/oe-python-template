"""Module providing graphical user interface (GUI) served as native or web application."""

from importlib.util import find_spec

if find_spec("nicegui"):
    from ._cli import cli  # type: ignore
    from .components._local_file_picker import LocalFilePicker
    from .pages._index import index

    __all__ = [
        "LocalFilePicker",
        "cli",
        "index",
    ]
