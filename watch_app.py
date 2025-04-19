"""Graphical User Interface (GUI) of Aignostics Python SDK."""

from oe_python_template.app import index
from oe_python_template.utils import gui_run

root = index

# For development run via `uv run watch_gui.py``
gui_run(native=False, show=True, watch=True)
