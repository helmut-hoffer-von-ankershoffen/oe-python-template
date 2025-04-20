"""Homepage (index) of GUI."""

from pathlib import Path

import numpy as np
from nicegui import ui

from oe_python_template.hello import Service

from .. import LocalFilePicker  # noqa: TID252


async def pick_file() -> None:
    result = await LocalFilePicker(str(Path.cwd() / "examples"), multiple=True)
    ui.notify(f"You chose {result}")


def register_index() -> None:
    """Register the index page."""

    @ui.page("/")
    def index() -> None:
        """Homepage of GUI."""
        service = Service()

        ui.button("Choose file", on_click=pick_file, icon="folder")

        ui.button("Click me", on_click=lambda: ui.notify(service.get_hello_world()), icon="check")

        with ui.card().tight():  # noqa: SIM117
            with ui.matplotlib(figsize=(4, 3)).figure as fig:
                x = np.linspace(0.0, 5.0)
                y = np.cos(2 * np.pi * x) * np.exp(-x)
                ax = fig.gca()
                ax.plot(x, y, "-")
