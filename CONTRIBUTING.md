# Contributing

Thank you for considering contributing to OE Python Template!

## Setup

Clone this GitHub repository via ```git clone git@github.com:helmut-hoffer-von-ankershoffen/oe-python-template.git``` and change into the directory of your local OE Python Template repository: ```cd oe-python-template```

Install the dependencies:

### macOS

```shell
if ! command -v brew &> /dev/null; then # if Homebrew package manager not present ...
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # ... install it
else
  which brew # ... otherwise inform where brew command was found
fi
# Install required tools if not present
which jq &> /dev/null || brew install jq
which xmllint &> /dev/null || brew install xmllint
which act &> /dev/null || brew install act
uv run pre-commit install             # install pre-commit hooks, see https://pre-commit.com/
```

### Linux

```shell
sudo sudo apt install -y curl jq libxml2-utils gnupg2  # tooling
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash # act
uv run pre-commit install # see https://pre-commit.com/
```

## Code

```
src/oe_python_template/
├── __init__.py          # Package initialization
└── cli.py               # Command Line Interface
tests/                   # Unit and E2E tests
├── cli_tests.py         # Verifies the CLI functionality
└── fixtures/            # Fixtures and mock data
examples/                # Example code demonstrating use of the project
├── streamlit.py         # Streamlit App, deployed in Streamlit Community Cloud
├── notebook.py          # Marimo notebook
├── notebook.ipynb       # Jupyter notebook
└── script.py            # Minimal script
```

## Run

### .env file

Don't forget to configure your `.env` file with the required environment variables.

Notes:
* .env.example is provided as a template.
* .env is excluded from version control, so feel free to add secret values.

### update dependencies and create virtual environment

```shell
uv sync                      # install dependencies
uv sync --all-extras         # install all extras, required for examples
uv venv                      # create a virtual environment
source .venv/bin/activate    # activate it
uv run pre-commit install    # Install pre-commit hook etc.
```

### run the CLI

```shell
uv run oe-python-template # shows help
```

## Build

All build steps are defined in `noxfile.py`.

```shell
uv run nox        # Runs all build steps except setup_dev
```

You can run individual build steps - called sessions in nox as follows:

```shell
uv run nox -s test      # run tests
uv run nox -s lint      # run formatting and linting
uv run nox -s audit     # run security and license audit, inc. sbom generation
uv run nox -s docs      # build documentation, output in docs/build/html
```

As a shortcut, you can run build steps using `./n`:

```shell
./n test
./n lint
# ...
```

Generate a wheel using uv
```shell
uv build
```

Notes:
1. Reports dumped into ```reports/```
3. Documentation dumped into ```docs/build/html/```
2. Distribution dumped into ```dist/```

### Running GitHub CI workflow locally

```shell
uv run nox -s act
```

Notes:

- Workflow defined in `.github/workflows/*.yml`
- test-and-report.yml calls all build steps defined in noxfile.py

### Docker

```shell
docker build -t oe-python-template .
```

```shell
docker run --env THE_VAR=THE_VALUE oe-python-template --help
```

### Copier

Update from template

```shell
uv run nox -s update_from_template
```

### Generate PDF manual

```shell
brew install mactex # install MacTeX, will take a while and requires sudo
./n docs_pdf        # build latex, then generate pdf from it. Output in docs/build/latex/oe-python-template.pdf
```


## Pull Request Guidelines

- Before starting to write code read the [code style guide](CODE_STYLE.md) document for mandatory coding style
  guidelines.
- **Pre-Commit Hooks:** We use pre-commit hooks to ensure code quality. Please install the pre-commit hooks by running `uv run pre-commit install`. This ensure all tests, linting etc. pass locally before you can commit.
- **Squash Commits:** Before submitting a pull request, please squash your commits into a single commit.
- **Branch Naming:** Use descriptive branch names like `feature/your-feature` or `fix/issue-number`.
- **Testing:** Ensure new features have appropriate test coverage.
- **Documentation:** Update documentation to reflect any changes or new features.
