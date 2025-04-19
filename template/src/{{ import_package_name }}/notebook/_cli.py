"""Notebook CLI commands."""

from typing import Annotated

import typer
import uvicorn

from ..cli import cli  # noqa: TID252
from ..utils import console, get_logger  # noqa: TID252
from ._service import Service

logger = get_logger(__name__)


@cli.command()
def notebook(
    host: Annotated[str, typer.Option(help="Host to bind the server to")] = "127.0.0.1",
    port: Annotated[int, typer.Option(help="Port to bind the server to")] = 8001,
) -> None:
    """Start notebook in web browser."""
    console.print(f"Starting marimo notebook server at http://{host}:{port}")
    uvicorn.run(
        Service().create_marimo_app(),
        host=host,
        port=port,
    )
