"""CLI (Command Line Interface) of OE Python Template."""

import sys

import typer

from .utils import __version__, console, get_logger, prepare_cli

logger = get_logger(__name__)

cli = typer.Typer(help="Command Line Interface of OE Python Template")

prepare_cli(cli, f"🧠 OE Python Template v{__version__} - built with love in Berlin 🐻")

if __name__ == "__main__":  # pragma: no cover
    try:
        cli()
    except Exception as e:  # noqa: BLE001
        logger.critical("Fatal error occurred: %s", e)
        console.print(f"Fatal error occurred: {e}", style="error")
        sys.exit(1)
