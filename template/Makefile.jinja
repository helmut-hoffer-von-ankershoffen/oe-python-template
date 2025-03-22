# Makefile for running common development tasks

# Define all PHONY targets
.PHONY: all audit bump build clean docs lint setup setup test update_from_template \
        patch minor major pdf py311 py312 py313

# Main targets
all:
	uv run nox

# General command pattern that forwards arguments to nox
# If no arguments provided, just run the session
# If arguments provided, pass them to the session
# For bump, show usage hint if no arguments provided
nox-cmd = @if [ -n "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
	uv run nox -s $@ -- $(filter-out $@,$(MAKECMDGOALS)); \
elif [ "$@" = "bump" ]; then \
	echo "Usage: make bump [patch|minor|major|x.y.z]"; \
	exit 1; \
else \
	uv run nox -s $@; \
fi

# Targets that use the nox-cmd pattern
act audit bump docs lint setup test update_from_template:
	$(nox-cmd)

# Standalone targets
clean:
	rm -rf .mypy_cache
	rm -rf .nox
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .venv
	rm -rf dist
	rm -rf .coverage
	make -C docs clean
	rm -rf reports && mkdir -p reports && touch reports/.keep

# Empty rules for argument targets
patch minor major pdf py311 py312 py313:
	@:

# Help text
help:
	@echo "Available targets:"
	@echo "  act                 - Run GitHub actions locally via act"
	@echo "  all                 - Run all default nox sessions, i.e. lint, test, docs, audit"
	@echo "  audit               - Run security and license compliance audit"
	@echo "  build               - Build wheel package with uv"
	@echo "  bump patch|minor|major|x.y.z - Bump version"
	@echo "  clean               - Clean build artifacts"
	@echo "  docs [pdf]          - Build documentation (add pdf for PDF format)"
	@echo "  lint                - Run linting and formatting checks"
	@echo "  setup               - Setup development environment"
	@echo "  test [py311|py312|py313] - Run tests (for specific Python version)"
	@echo "  update_from_template - Update from template using copier"
