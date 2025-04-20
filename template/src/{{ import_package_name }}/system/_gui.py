"""Homepage (index) of GUI."""

from pathlib import Path

from nicegui import ui

from ..utils import GUILocalFilePicker, __project_name__, __version__  # noqa: TID252
from ._service import Service


async def pick_file() -> None:
    """Open a file picker dialog and show notifier when closed again."""
    result = await GUILocalFilePicker(str(Path.cwd() / "examples"), multiple=True)
    ui.notify(f"You chose {result}")


@ui.page("/info")
def page_info() -> None:
    """Homepage of GUI."""
    ui.label(f"{__project_name__} v{__version__}").mark("LABEL_VERSION")
    ui.json_editor({
        "content": {"json": Service().info(True, True)},
        "readOnly": True,
    }).mark("JSON_EDITOR_INFO")
    ui.link("Home", "/").mark("LINK_HOME")
