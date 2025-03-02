Copier template to scaffold Python projects compliant with best practices and modern tooling.

Use Cases:
1) Lorem Ipsum
2) Dolor Sit Amet
3) Consectetur Adipiscing Elit

## Overview

Adding OE Python Template to your project as a dependency is easy.

```shell
uv add oe-python-template             # add dependency to your project
```

If you don't have uv installed follow [these instructions](https://docs.astral.sh/uv/getting-started/installation/). If you still prefer pip over the modern and fast package manager [uv](https://github.com/astral-sh/uv), you can install the library like this:

```shell
pip install oe-python-template        # add dependency to your project
```

Executing the command line interface (CLI) is just as easy:

```shell
uvx oe-python-template
```

The CLI provides extensive help:

```shell
uvx oe-python-template --help              # all CLI commands
uvx oe-python-template command --help      # all options for command
```

## Highlights

* Copier template to scaffold Python projects compliant with best practices and modern tooling.
* Various Examples:
  - [Simple Python script]https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/script.py)
  - [Streamlit web application](https://oe-python-template.streamlit.app/) deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  - [Jupyter](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.ipynb) and [Marimo](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.py) notebook
* [Complete reference documenation](https://oe-python-template.readthedocs.io/en/latest/reference.html) on Read the Docs
* [Transparent test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template) including unit and E2E tests (reported on Codecov)
* Matrix tested with [multiple python versions](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/noxfile.py) to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
* Compliant with modern linting and formatting standards (powered by [Ruff](https://github.com/astral-sh/ruff))
* Up-to-date dependencies (monitored by [Renovate](https://github.com/renovatebot/renovate))
* [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template) in security, maintainability, and reliability with low technical debt and low codesmell (verified by SonarQube)
* 1-liner for installation and execution of command line interface (CLI) via [uv(x)](https://github.com/astral-sh/uv) or [Docker](https://hub.docker.com/r/helmuthva/oe-python-template/tags)
* Setup for developing inside a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included (supports VSCode and GitHub Codespaces)

## Usage Examples

### Minimal Python Script:

```python
"""Example script demonstrating the usage of the service provided by OE Python Template."""

from dotenv import load_dotenv
from rich.console import Console

from oe_python_template import Service

console = Console()

load_dotenv()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/script.py) - [Read the reference documentation](https://oe-python-template.readthedocs.io/en/latest/reference.html)

### Streamlit App

Serve the functionality provided by OE Python Template in the web by easily integrating the service into a Streamlit application.

[Try it out!](https://oe-python-template.streamlit.app) - [Show the code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/streamlit.py)

... or serve the app locally
```shell
uv sync --all-extras                                # Install streamlit dependency part of the examples extra, see pyproject.toml
uv run streamlit run examples/streamlit.py          # Serve on localhost:8501, opens browser
```

## Notebooks

### Jupyter

[Show the Jupyter code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.ipynb)

... or run within VSCode

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
```
Install the [Jupyter extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Click on `examples/notebook.ipynb` in VSCode and run it.

### Marimo

[Show the marimo code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.py)

Execute the notebook as a WASM based web app

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo run examples/notebook.py --watch      # Serve on localhost:2718, opens browser
```

or edit interactively in your browser

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo edit examples/notebook.py --watch     # Edit on localhost:2718, opens browser
```

... or edit interactively within VSCode

Install the [Marimo extension for VSCode](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)

Click on `examples/notebook.py` in VSCode and click on the caret next to the Run icon above the code (looks like a pencil) > "Start in marimo editor" (edit).

## Command Line Interface (CLI)

### Run with [uvx](https://docs.astral.sh/uv/guides/tools/)

Show available commands:

```shell
uvx oe-python-template --help
```

Execute commands:

```shell
uvx oe-python-template hello-world
uvx oe-python-template hello-world --json
uvx oe-python-template echo "Lorem Ipsum"
```

### Environment

The service loads environment variables including support for .env files.

```shell
cp .env.example .env              # copy example file
echo "THE_VAR=MY_VALUE" > .env    # overwrite with your values
```

Now run the usage examples again.

### Run with Docker

You can as well run the CLI within Docker.

```shell
docker run helmuthva/oe-python-template --help
docker run helmuthva/oe-python-template hello-world
docker run helmuthva/oe-python-template hello-world --json
docker run helmuthva/oe-python-template echo "Lorem"
```

Execute command:

```shell
docker run --env THE_VAR=MY_VALUE helmuthva/oe-python-template echo "Lorem Ipsum"
```

Or use docker compose

The .env is passed through from the host to the Docker container.

```shell
docker compose up
docker compose run oe-python-template --help
```

## Extra: Lorem Ipsum

Dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam.
