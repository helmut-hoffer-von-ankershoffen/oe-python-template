
[//]: # (README.md generated from docs/partials/README_*.md)

# 🧠 OE Python Template

[![License](https://img.shields.io/github/license/helmut-hoffer-von-ankershoffen/oe-python-template?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/oe-python-template.svg?logo=python&color=204361&labelColor=1E2933)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/noxfile.py)
[![CI](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/actions/workflows/test-and-report.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/actions/workflows/test-and-report.yml)
[![Read the Docs](https://img.shields.io/readthedocs/oe-python-template)](https://oe-python-template.readthedocs.io/en/latest/)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template)
[![CodeQL](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/actions/workflows/codeql.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/security/code-scanning)
[![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/security/dependabot)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/issues?q=is%3Aissue%20state%3Aopen%20Dependency%20Dashboard)
[![Coverage](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template/graph/badge.svg?token=SX34YRP30E)](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Ruff](https://img.shields.io/badge/style-Ruff-blue?color=D6FF65)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/noxfile.py)
[![MyPy](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/noxfile.py)
[![GitHub - Version](https://img.shields.io/github/v/release/helmut-hoffer-von-ankershoffen/oe-python-template?label=GitHub&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/releases)
[![GitHub - Commits](https://img.shields.io/github/commit-activity/m/helmut-hoffer-von-ankershoffen/oe-python-template/main?label=commits&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/commits/main/)
[![PyPI - Version](https://img.shields.io/pypi/v/oe-python-template.svg?label=PyPI&logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/oe-python-template)
[![PyPI - Status](https://img.shields.io/pypi/status/oe-python-template?logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/oe-python-template)
[![Docker - Version](https://img.shields.io/docker/v/helmuthva/oe-python-template?sort=semver&label=Docker&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/oe-python-template/tags)
[![Docker - Size](https://img.shields.io/docker/image-size/helmuthva/oe-python-template?sort=semver&arch=arm64&label=image&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/oe-python-template/)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Vercel Deploy](https://deploy-badge.vercel.app/vercel/oe-python-template?root=docs)](https://oe-python-template.vercel.app/api/v1/hello/world)
[![Better Stack Uptime](https://uptime.betterstack.com/status-badges/v1/monitor/1vze5.svg)](https://helmut-hoffer-von-ankershoffen.betteruptime.com/)

<!---
[![ghcr.io - Version](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/oe-python-template/tags?color=%2344cc11&ignore=0.0%2C0%2Clatest&n=3&label=ghcr.io&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/pkgs/container/oe-python-template)
[![ghcr.io - Sze](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/oe-python-template/size?color=%2344cc11&tag=latest&label=size&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/pkgs/container/oe-python-template)
-->

> [!TIP]
> 📚 [Online documentation](https://oe-python-template.readthedocs.io/en/latest/) - 📖 [PDF Manual](https://oe-python-template.readthedocs.io/_/downloads/en/latest/pdf/)

---


Copier template to scaffold Python projects compliant with best practices and modern tooling.

### Scaffolding

This [Copier](https://copier.readthedocs.io/en/stable/) template enables you to quickly generate (scaffold) a Python package with fully functioning build and test automation:

1. Projects generated from this template can be [easily updated](https://copier.readthedocs.io/en/stable/updating/) to benefit from improvements and new features of the template.
2. During project generation, you can flexibly configure naming of the Python distribution, import package, main author, GitHub repository, organization, and many other aspects to match your specific requirements (see [copier.yml](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/copier.yml) for all available options).

### Development Infrastructure

Projects generated with this template come with a comprehensive development toolchain and quality assurance framework that supports the entire software development lifecycle - from coding and testing to documentation, release management, and compliance auditing. This infrastructure automates routine tasks, enforces code quality standards, and streamlines the path to production:

1. Linting with [Ruff](https://github.com/astral-sh/ruff)
2. Static type checking with [mypy](https://mypy.readthedocs.io/en/stable/)
3. Complete set of [pre-commit](https://pre-commit.com/) hooks including [detect-secrets](https://github.com/Yelp/detect-secrets) and [pygrep](https://github.com/pre-commit/pygrep-hooks)
4. Unit and E2E testing with [pytest](https://docs.pytest.org/en/stable/) including parallel test execution
5. Matrix testing in multiple environments with [nox](https://nox.thea.codes/en/stable/)
6. Test coverage reported with [Codecov](https://codecov.io/) and published as release artifact
7. CI/CD pipeline automated with [GitHub Actions](https://github.com/features/actions)
8. CI/CD pipeline can be run locally with [act](https://github.com/nektos/act)
9. Code quality and security checks with [SonarQube](https://www.sonarsource.com/products/sonarcloud) and [GitHub CodeQL](https://codeql.github.com/)
10. Dependency monitoring and vulnerability scanning with [pip-audit](https://pypi.org/project/pip-audit/), [trivy](https://trivy.dev/latest/), [Renovate](https://github.com/renovatebot/renovate), and [GitHub Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
11. Error monitoring and profiling with [Sentry](https://sentry.io/)  (optional)
12. Logging and metrics with [Logfire](https://logfire.dev/) (optional)
13. Prepared for uptime monitoring with [betterstack](https://betterstack.com/) or alternatives
13. Licenses of dependencies extracted with [pip-licenses](https://pypi.org/project/pip-licenses/), matched with allow list, and published as release artifacts in CSV and JSON format for further compliance checks
14. Generation of attributions from extracted licenses
15. Software Bill of Materials (SBOM) generated in [CycloneDX](https://cyclonedx.org/) and [SPDX](https://spdx.dev/) formats with [cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) resp. [trivy](https://trivy.dev/latest/), published as release artifacts
16. Version and release management with [bump-my-version](https://callowayproject.github.io/bump-my-version/)
17. Changelog and release notes generated with [git-cliff](https://git-cliff.org/)
18. Documentation generated with [Sphinx](https://www.sphinx-doc.org/en/master/) including reference documentation for the library, CLI, and API
19. Documentation published to [Read The Docs](https://readthedocs.org/) including generation of PDF and single page HTML versions
20. Interactive OpenAPI specification with [Swagger](https://swagger.io/)
21. Python package published to [PyPI](https://pypi.org/)
22. Docker images published to [Docker.io](https://hub.docker.com/) and [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) with [artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)
23. One-click development environments with [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) and [GitHub Codespaces](https://github.com/features/codespaces)
24. Settings for use with [VSCode](https://code.visualstudio.com/)
25. Settings and custom instructions for use with [GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
26. API deployed as serverless function to [Vercel](https://vercel.com/) (optional)

### Application Features

Beyond development tooling, projects generated with this template include the code, documentation, and configuration of a fully functioning application and service. This reference implementation serves as a starting point for your own business logic with modern patterns and enterprise practices already in place:

1. Usable as library with "Hello" module exposing a simple service that can say "Hello, world!" and echo utterances.
2. Command-line interface (CLI) with [Typer](https://typer.tiangolo.com/)
3. Versioned webservice API with [FastAPI](https://fastapi.tiangolo.com/)
4. [Interactive Jupyter notebook](https://jupyter.org/) and [reactive Marimo notebook](https://marimo.io/)
5. Simple Web UI with [Streamlit](https://streamlit.io/)
6. Configuration to run the CLI and API in a Docker container including setup for [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/)
7. Validation and settings management with [pydantic](https://docs.pydantic.dev/)
8. Info command enabling to inspect the runtime, compiled settings, and further info provided dynamically by modules
9. Health endpoint exposing system health dynamically aggregated from all modules and dependencies
10. Flexible logging and instrumentation, including support for [Sentry](https://sentry.io/) and [Logfire](https://logfire.dev/) 
11. Hello service demonstrates use of custom real time metrics collected via Logfire
12. Modular architecture including auto-registration of services, CLI commands and API routes exposed by modules
13. Documentation including dynamic badges, setup instructions, contribution guide and security policy

Explore [here](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example) for what's generated out of the box.

## Generate a new project

To generate, build and release a fully functioning project in a few minutes, follow these 5 steps:

**Step 1**: Execute the following command to install or update tooling.
```shell
# Install Homebrew, uv package manager, copier and further dev tools
curl -LsSf https://raw.githubusercontent.com/helmut-hoffer-von-ankershoffen/oe-python-template/HEAD/install.sh | sh
```

**Step 2**: [Create a repository on GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), clone to your local machine, and change into it's directory.

**Step 3**: Execute the following command to generate a new project based on this template.
```shell
# Ensure to stand in your freshly created git repository before executing this command
copier copy --trust gh:helmut-hoffer-von-ankershoffen/oe-python-template .
```

**Step 4**: Execute the following commands to push your initial commit to GitHub.
```shell
git add .
git commit -m "chore: Initial commit"
git push
```

Check the [Actions tab](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/actions) of your GitHub repository: The CI/CD workflow of your project is already running!

The workflow will fail at the SonarQube step, as this external service is not yet configured for our new repository. We will configure SonarQube and other services in the next step!

Notes:
1. Check out [this manual](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key) on how to set up signed commits

**Step 5**: Follow the [instructions](SERVICE_CONNECTIONS.md) to wire up
external services such as CloudCov, SonarQube Cloud, Read The Docs, Docker.io, and Streamlit Community Cloud.

**Step 6**: Release the first version of your project
```shell
make bump
```
Notes:
1. You can remove the above sections - from "Scaffolding" to this notes - post having successfully generated your project.
2. The following sections refer to the dummy application and service generated into the `tests` and `src` folder by this template.
   Use the documentation and code as inspiration, adapt to your business logic, or remove and start documenting and coding from scratch.


## Overview

Adding OE Python Template to your project as a dependency is easy. See below for usage examples.

```shell
uv add oe-python-template             # add dependency to your project
```

If you don't have uv installed follow [these instructions](https://docs.astral.sh/uv/getting-started/installation/). If you still prefer pip over the modern and fast package manager [uv](https://github.com/astral-sh/uv), you can install the library like this:


```shell
pip install oe-python-template        # add dependency to your project
```

Executing the command line interface (CLI) in an isolated Python environment is just as easy:

```shell
uvx oe-python-template hello-world       # prints "Hello, world! [..]"
uvx oe-python-template serve             # serves web API
uvx oe-python-template serve --port=4711 # serves web API on port 4711
```

Notes:
1. The API is versioned, mounted at `/api/v1` resp. `/api/v2`
2. While serving the web API go to [http://127.0.0.1:8000/api/v1/hello-world](http://127.0.0.1:8000/api/v1/hello-world) to see the respons of the `hello-world` operation.
3. Interactive documentation is provided at [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)


The CLI provides extensive help:

```shell
uvx oe-python-template --help                # all CLI commands
uvx oe-python-template hello-world --help    # help for specific command
uvx oe-python-template echo --help
uvx oe-python-template openapi --help
uvx oe-python-template serve --help
```


## Operational Excellence

This project is designed with operational excellence in mind, using modern Python tooling and practices. It includes:

1. Various examples demonstrating usage:
  a. [Simple Python script](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/script.py)
  b. [Streamlit web application](https://oe-python-template.streamlit.app/) deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  c. [Jupyter](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.ipynb) and [Marimo](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.py) notebook
2. Complete reference documentation [for the library](https://oe-python-template.readthedocs.io/en/latest/lib_reference.html), [for the CLI](https://oe-python-template.readthedocs.io/en/latest/cli_reference.html) and [for the API](https://oe-python-template.readthedocs.io/en/latest/api_reference_v1.html) on Read the Docs
3. [Transparent test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template) including unit and E2E tests (reported on Codecov)
4. Matrix tested with [multiple python versions](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/noxfile.py) to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
5. Compliant with modern linting and formatting standards (powered by [Ruff](https://github.com/astral-sh/ruff))
6. Up-to-date dependencies (monitored by [Renovate](https://github.com/renovatebot/renovate) and [Dependabot](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/security/dependabot))
7. [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template) in security, maintainability, and reliability with low technical debt and codesmell (verified by SonarQube)
8. Additional code security checks using [CodeQL](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/security/code-scanning)
9. [Security Policy](SECURITY.md)
10. [License](LICENSE) compliant with the Open Source Initiative (OSI)
11. 1-liner for installation and execution of command line interface (CLI) via [uv(x)](https://github.com/astral-sh/uv) or [Docker](https://hub.docker.com/r/helmuthva/oe-python-template/tags)
12. Setup for developing inside a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included (supports VSCode and GitHub Codespaces)


## Usage Examples

The following examples run from source - clone this repository using
`git clone git@github.com:helmut-hoffer-von-ankershoffen/oe-python-template.git`.

### Minimal Python Script:

```python
"""Example script demonstrating the usage of the service provided by OE Python Template."""

from dotenv import load_dotenv
from rich.console import Console

from oe_python_template.hello import Service

console = Console()

load_dotenv()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/script.py) - [Read the reference documentation](https://oe-python-template.readthedocs.io/en/latest/lib_reference.html)


### Streamlit App

Serve the functionality provided by OE Python Template in the web by easily integrating the service into a Streamlit application.

[Try it out!](https://oe-python-template.streamlit.app) - [Show the code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/streamlit.py)

... or serve the app locally
```shell
uv sync --all-extras                                # Install streamlit dependency part of the examples extra, see pyproject.toml
uv run streamlit run examples/streamlit.py          # Serve on localhost:8501, opens browser
```

### Vercel Serverless Function

Serve the API as a [serverless function on Vercel](https://oe-python-template.vercel.app/)


## Notebooks

### Jupyter

[Show the Jupyter code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/blob/main/examples/notebook.ipynb)

... or run within VSCode

```shell
uv sync --all-extras                                # Install dependencies required for examples such as Juypyter kernel, see pyproject.toml
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
uvx oe-python-template hello world
uvx oe-python-template hello echo --help
uvx oe-python-template hello echo "Lorem"
uvx oe-python-template hello echo "Lorem" --json
uvx oe-python-template system info
uvx oe-python-template system health
uvx oe-python-template system openapi
uvx oe-python-template system openapi --output-format=json
uvx oe-python-template system serve
```

See the [reference documentation of the CLI](https://oe-python-template.readthedocs.io/en/latest/cli_reference.html) for detailed documentation of all CLI commands and options.


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
docker run helmuthva/oe-python-template hello world
docker run helmuthva/oe-python-template hello echo --help
docker run helmuthva/oe-python-template hello echo "Lorem"
docker run helmuthva/oe-python-template hello echo "Lorem" --json
docker run helmuthva/oe-python-template system info
docker run helmuthva/oe-python-template system health
docker run helmuthva/oe-python-template system openapi
docker run helmuthva/oe-python-template system openapi --output-format=json
docker run helmuthva/oe-python-template system serve
```

Execute command:

```shell
docker run --env THE_VAR=MY_VALUE helmuthva/oe-python-template hello echo "Lorem Ipsum"
```

Or use docker compose

The .env is passed through from the host to the Docker container.

```shell
docker compose run --remove-orphans oe-python-template --help
docker compose run --remove-orphans oe-python-template hello world
docker compose run --remove-orphans oe-python-template hello echo --help
docker compose run --remove-orphans oe-python-template hello echo "Lorem"
docker compose run --remove-orphans oe-python-template hello echo "Lorem" --json
docker compose run --remove-orphans oe-python-template system info
docker compose run --remove-orphans oe-python-template system health
docker compose run --remove-orphans oe-python-template system openapi
docker compose run --remove-orphans oe-python-template system openapi --output-format=json
echo "Running OE Python Template's API container as a daemon ..."
docker compose up -d
echo "Waiting for the API server to start ..."
sleep 5
echo "Checking health of v1 API ..."
curl http://127.0.0.1:8000/api/v1/healthz
echo ""
echo "Saying hello world with v1 API ..."
curl http://127.0.0.1:8000/api/v1/hello/world
echo ""
echo "Swagger docs of v1 API ..."
curl http://127.0.0.1:8000/api/v1/docs
echo ""
echo "Checking health of v2 API ..."
curl http://127.0.0.1:8000/api/v2/healthz
echo ""
echo "Saying hello world with v1 API ..."
curl http://127.0.0.1:8000/api/v2/hello/world
echo ""
echo "Swagger docs of v2 API ..."
curl http://127.0.0.1:8000/api/v2/docs
echo ""
echo "Shutting down the API container ..."
docker compose down
```

* See the [reference documentation of the API](https://oe-python-template.readthedocs.io/en/latest/api_reference_v1.html) for detailed documentation of all API operations and parameters.


## Extra: Lorem Ipsum

Dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam.


## Further Reading

* Inspect our [security policy](https://oe-python-template.readthedocs.io/en/latest/security.html) with detailed documentation of checks, tools and principles.
* Check out the [CLI Reference](https://oe-python-template.readthedocs.io/en/latest/cli_reference.html) with detailed documentation of all CLI commands and options.
* Check out the [Library Reference](https://oe-python-template.readthedocs.io/en/latest/lib_reference.html) with detailed documentation of public classes and functions.
* Check out the [API Reference](https://oe-python-template.readthedocs.io/en/latest/api_reference_v1.html) with detailed documentation of all API operations and parameters.
* Our [release notes](https://oe-python-template.readthedocs.io/en/latest/release-notes.html) provide a complete log of recent improvements and changes.
* In case you want to help us improve 🧠 OE Python Template: The [contribution guidelines](https://oe-python-template.readthedocs.io/en/latest/contributing.html) explain how to setup your development environment and create pull requests.
* We gratefully acknowledge the [open source projects](https://oe-python-template.readthedocs.io/en/latest/attributions.html) that this project builds upon. Thank you to all these wonderful contributors!

## Star History

<a href="https://star-history.com/#helmut-hoffer-von-ankershoffen/oe-python-template">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/oe-python-template&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/oe-python-template&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/oe-python-template&type=Date" />
 </picture>
</a>
