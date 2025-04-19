"""CLI (Command Line Interface) of app module."""

from oe_python_template.utils import get_logger, gui_run

from ..cli import cli  # noqa: TID252

logger = get_logger(__name__)


@cli.command()
def app() -> None:
    """Start app in native window."""
    gui_run(title="OE Python Template", icon="🧠")
