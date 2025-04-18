from nicegui import app, ui
from nicegui import native as native_app

from ._constants import __project_name__
from ._log import get_logger

logger = get_logger(__name__)


def handle_shutdown() -> None:
    """Handle shutdown of the GUI."""
    logger.info("Shutdown initiated")


def gui_run(  # noqa: PLR0913, PLR0917
    native: bool = True,
    show: bool = False,
    host: str | None = None,
    port: int | None = 8000,
    title: str = __project_name__,
    icon: str = "",
    watch: bool = False,
    with_api: bool = False,
    with_notebook: bool = False,
    notebook_path: str | None = None,
) -> None:
    """Start the GUI.

    Args:
        native: Whether to run the GUI in native mode.
        show: Whether to show the GUI.
        host: Host to run the GUI on.
        port: Port to run the GUI on.
        title: Title of the GUI.
        icon: Icon for the GUI.
        watch: Whether to watch for changes and reload the GUI.
        with_api: Whether to mount the API.
        with_notebook: Whether to mount a notebook.
        notebook_path: Path to the notebook file.

    Raises:
        ValueError: If with_notebook is True but notebook_path is None.
    """
    app.on_shutdown(handle_shutdown)
    if with_api:
        from ..api import api  # noqa: PLC0415, TID252

        app.mount("/api", api)
    if with_notebook:
        from ._notebook import notebook_app  # noqa: PLC0415

        if notebook_path is None:
            message = "notebook_path must be provided when with_notebook is True"
            raise ValueError(message)
        app.mount("/notebook", notebook_app(path=notebook_path))
    ui.run(
        title=title,
        favicon=icon,
        native=native,
        reload=watch,
        dark=False,
        host=host,
        port=port or native_app.find_open_port(),
        frameless=False,
        show_welcome_message=True,
        show=show,
    )
