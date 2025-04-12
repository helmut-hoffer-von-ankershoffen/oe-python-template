"""Tests to verify the CLI functionality of the hello module."""

import os
import subprocess

import pytest
from typer.testing import CliRunner

from oe_python_template.cli import cli

BUILT_WITH_LOVE = "built with love in Berlin"


@pytest.fixture
def runner() -> CliRunner:
    """Provide a CLI test runner fixture."""
    return CliRunner()


def test_cli_info_de() -> None:
    """Check hello world printed."""
    env_de = os.environ.copy()
    env_de.update({"OE_PYTHON_TEMPLATE_HELLO_LANGUAGE": "de_DE"})
    cli = "oe-python-template"
    completed_process = subprocess.run([cli, "system", "info"], capture_output=True, check=False, env=env_de)
    assert b'"OE_PYTHON_TEMPLATE_HELLO_LANGUAGE": "de_DE"' in completed_process.stdout


def test_cli_echo(runner: CliRunner) -> None:
    """Check hello world printed."""
    result = runner.invoke(cli, ["hello", "echo", "hello"])
    assert result.exit_code == 0
    assert "HELLO" in result.output


def test_cli_echo_fails_on_silence(runner: CliRunner) -> None:
    """Check hello world printed."""
    result = runner.invoke(cli, ["hello", "echo", ""])
    assert result.exit_code == 1


def test_cli_echo_json(runner: CliRunner) -> None:
    """Check hello world printed."""
    result = runner.invoke(cli, ["hello", "echo", "hello", "--json"])
    assert result.exit_code == 0
    assert '{\n  "text": "HELLO"\n}\n' in result.output


def test_cli_hello_world(runner: CliRunner) -> None:
    """Check hello world printed."""
    result = runner.invoke(cli, ["hello", "world"])
    assert result.exit_code == 0
    assert "Hello, world!" in result.output


def test_cli_hello_world_german() -> None:
    """Check hello world printed."""
    env_de = os.environ.copy()
    env_de.update({"OE_PYTHON_TEMPLATE_HELLO_LANGUAGE": "de_DE"})
    completed_process = subprocess.run(
        ["oe-python-template", "hello", "world"], capture_output=True, check=False, env=env_de
    )
    assert completed_process.stdout == b"Hallo, Welt!\n"
