"""Tests to verify the CLI functionality of OE Python Template."""

import pytest
from typer.testing import CliRunner

from oe_python_template import (
    __version__,
)
from oe_python_template.cli import cli

BUILT_WITH_LOVE = "built with love in Berlin"


@pytest.fixture
def runner() -> CliRunner:
    """Provide a CLI test runner fixture."""
    return CliRunner()


def test_cli_built_with_love(runner) -> None:
    """Check epilog shown."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert BUILT_WITH_LOVE in result.output
    assert __version__ in result.output


def test_cli_echo(runner: CliRunner) -> None:
    """Check hello world printed."""
    result = runner.invoke(cli, ["echo", "4711"])
    assert result.exit_code == 0
    assert "4711" in result.output


def test_cli_hello_world(runner: CliRunner) -> None:
    """Check hello world printed."""
    result = runner.invoke(cli, ["hello-world"])
    assert result.exit_code == 0
    assert "Hello, world!" in result.output
