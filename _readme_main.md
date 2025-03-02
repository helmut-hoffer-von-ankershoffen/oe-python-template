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
  - [Streamlit web application](https://oe-python-template.streamlit.app/) deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  - [Jupyter notebook](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/jupyter.ipynb)
  - [Simple Python script]https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/script.py)
* [Complete reference documenation](https://oe-python-template.readthedocs.io/en/latest/reference.html) on Read the Docs
* [Transparent test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template) including unit and E2E tests (reported on Codecov)
* Matrix tested with [multiple python versions](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/noxfile.py) to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
* Compliant with modern linting and formatting standards (powered by [Ruff](https://github.com/astral-sh/ruff))
* Up-to-date dependencies (monitored by [Renovate](https://github.com/renovatebot/renovate))
* [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template) in security, maintainability, and reliability with low technical debt and low codesmell (verified by SonarQube)
* 1-liner for installation and execution of command line interface (CLI) via [uv(x)](https://github.com/astral-sh/uv) or [Docker](https://hub.docker.com/r/helmuthva/oe-python-template/tags)
* Setup for developing inside a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included (supports VSCode and GitHub Codespaces)

## Usage Examples

### Streamlit App

[Try it out!](https://oe-python-template.streamlit.app) - [Show the code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/streamlit.py)


### Minimal Python Script:

```python
"""
Example script demonstrating the usage of OE Python Template.

"""

print("Hello World")
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/script.py) - [Read the reference documentation](https://oe-python-template.readthedocs.io/en/latest/reference.html)

## Jupyter Notebook

[Show notebook code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/jupyter.ipynb)

## Command Line Interface (CLI)

### Run with [uvx](https://docs.astral.sh/uv/guides/tools/)

Show available commands:

```shell
uvx oe-python-template --help
```

Execute command:

```shell
uvx oe-python-template command "Lorem Ipsum"
```

### Run with Docker

Note: Replace ENV_KEY_TEST with Lorem Ipsum.

Show available commands:

```bash
docker run helmuthva/oe-python-template --help
```

Execute command:

```bash
docker run --env ENV_KEY_TEST=ENV_VALUE_TEST helmuthva/oe-python-template command "Lorem Ipsum"
```

Or use docker compose

File .env is passed through

```bash
docker compose up
docker compose run oe-python-template --help
```

## Extra: Lorem Ipsum

Dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam.
