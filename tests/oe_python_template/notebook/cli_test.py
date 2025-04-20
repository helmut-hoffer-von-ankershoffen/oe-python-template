"""Tests to verify the CLI functionality of the notebook module."""

import pytest
from fastapi import FastAPI
from typer.testing import CliRunner

from oe_python_template.cli import cli


@pytest.fixture
def runner() -> CliRunner:
    """Provide a CLI test runner fixture."""
    return CliRunner()


def test_cli_notebook_help(runner: CliRunner) -> None:
    """Check notebook help works."""
    result = runner.invoke(cli, ["notebook", "--help"])
    assert result.exit_code == 0


def test_cli_notebook_run(runner: CliRunner, monkeypatch: pytest.MonkeyPatch) -> None:
    """Check uvicorn.run is called with FastAPI app from the notebook service."""
    # Create a mock for uvicorn.run to capture the app instance
    mock_called = False
    mock_args = {}

    def mock_uvicorn_run(app, host=None, port=None):
        """Mock uvicorn.run function that captures the arguments."""
        nonlocal mock_called, mock_args
        mock_called = True
        mock_args = {
            "app": app,
            "host": host,
            "port": port,
        }

    # Apply the mock to uvicorn.run
    monkeypatch.setattr("uvicorn.run", mock_uvicorn_run)

    # Create a mock for the Service._settings.directory.is_dir to avoid errors
    monkeypatch.setattr("pathlib.Path.is_dir", lambda _: True)

    # Run the CLI command
    result = runner.invoke(cli, ["notebook"])

    # Check that the command executed successfully
    assert result.exit_code == 0

    # Check that uvicorn.run was called
    assert mock_called, "uvicorn.run was not called"

    # Check that uvicorn.run was called with the expected arguments
    assert isinstance(mock_args["app"], FastAPI), "uvicorn.run was not called with a FastAPI app"
    assert mock_args["host"] == "127.0.0.1", "host parameter is incorrect"
    assert mock_args["port"] == 8001, "port parameter is incorrect"
