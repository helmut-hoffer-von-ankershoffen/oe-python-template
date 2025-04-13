"""Tests to verify the CLI functionality of OE Python Template."""

import os
import subprocess
import sys

import pytest
from typer.testing import CliRunner

from oe_python_template.cli import cli
from oe_python_template.utils import (
    __version__,
)

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


def test_cli_fails_on_invalid_setting_with_env_arg() -> None:
    """Check system fails on boot with invalid setting using subprocess."""
    # Run the CLI as a subprocess with environment variable
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "oe_python_template.cli",
            "system",
            "info",
            "--env",
            "OE_PYTHON_TEMPLATE_LOG_LEVEL=FAIL",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    # Check the return code (78 indicates validation failed)
    assert result.returncode == 78
    # Check that the error message is in the stderr
    assert "Input should be 'CRITICAL'" in result.stdout


def test_cli_fails_on_invalid_setting_with_environ(runner) -> None:
    """Check system fails on boot with invalid setting using CliRunner and environment variables."""
    # Set the environment variable directly
    with runner.isolated_filesystem():
        # Set environment variable for the test
        env = os.environ.copy()
        env["OE_PYTHON_TEMPLATE_LOG_LEVEL"] = "DEBUG"

        # Run the CLI with the runner
        result = runner.invoke(cli, ["system", "info"], env=env)

        # Check the exit code (0 indicates all good)
        assert result.exit_code == 0

        # Set environment variable for the test
        env = os.environ.copy()
        env["OE_PYTHON_TEMPLATE_LOG_LEVEL"] = "FAIL"

        # Run the CLI with the runner
        result = runner.invoke(cli, ["system", "info"], env=env)

        # Check the exit code (78 indicates validation failed)
        assert result.exit_code == 78
        # Check that the error message is in the output
        assert "Input should be 'CRITICAL'" in result.output
