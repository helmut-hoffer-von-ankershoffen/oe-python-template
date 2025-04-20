"""CLI (Command Line Interface) of gui module."""

from oe_python_template.utils import get_logger, gui_run

from ..cli import cli  # noqa: TID252

logger = get_logger(__name__)


@cli.command()
def gui() -> None:
    """Start graphical user interface (GUI) in native window."""
    gui_run(native=True, with_api=False, title="OE Python Template", icon="🧠")
