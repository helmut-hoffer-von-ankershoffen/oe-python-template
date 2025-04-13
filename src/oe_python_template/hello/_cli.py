"""CLI (Command Line Interface) of OE Python Template."""

from typing import Annotated

import typer

from oe_python_template.utils import console, get_logger

from ._models import Utterance
from ._service import Service

logger = get_logger(__name__)

# CLI apps exported by modules via their __init__.py are automatically registered and injected into the main CLI app
cli = typer.Typer(name="hello", help="Hello commands")
_service = Service()


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
    """Echo the text.

    Args:
        text (str): The text to echo.
        json (bool): Print as JSON.
    """
    echo = Service.echo(Utterance(text=text))
    if json:
        console.print_json(data={"text": echo.text})
    else:
        console.print(echo.text)


@cli.command()
def world() -> None:
    """Print hello world message and what's in the environment variable THE_VAR."""
    console.print(_service.get_hello_world())
