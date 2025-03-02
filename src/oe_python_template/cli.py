"""Command line interface of OE Python Template."""

from typing import Annotated

import typer
from rich.console import Console

from oe_python_template import __version__, Service

console = Console()

cli = typer.Typer(name="Command Line Interface of OE Python Template")


@cli.command()
def echo(
    text: Annotated[
        str, typer.Argument(help="The text to echo")
    ] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    json: Annotated[
        bool,
        typer.Option(
            help=("Print as JSON"),
        ),
    ] = False,
) -> None:
    """Echo the text."""
    if json:
        console.print_json(data={"text": text})
    else:
        console.print(text)


@cli.command()
def hello_world() -> None:
    """Print hello world message and what's in the environment variable THE_VAR."""
    console.print(Service.get_hello_world())


def _apply_cli_settings(cli: typer.Typer, epilog: str) -> None:
    """Add epilog to all typers in the tree and configure default behavior."""
    cli.info.epilog = epilog
    cli.info.no_args_is_help = True
    for command in cli.registered_commands:
        command.epilog = cli.info.epilog


_apply_cli_settings(
    cli,
    f"🧠 OE Python Template v{__version__} - built with love in Berlin 🐻",
)


if __name__ == "__main__":
    cli()
