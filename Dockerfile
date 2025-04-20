# We share the base in the builder and targets
FROM python:3.13-slim-bookworm AS base

FROM base AS builder

# Copy in UV
COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /bin/uv

# We use the system interpreter managed by uv
ENV UV_PYTHON_DOWNLOADS=0

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project into `/app`
WORKDIR /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"


# The slim builder does not take in the extras
FROM builder AS builder-slim

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --no-editable

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY pyproject.toml /app
COPY .python-version /app
COPY uv.lock /app
COPY src /app/src
COPY LICENSE /app
COPY *.md /app

COPY .env.example /app/.env.example
COPY tests /app/tests
COPY examples /app/examples

# Install project specifics
# Nothing yet

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable


# The all builder takes them all
FROM builder AS builder-all

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --all-extras --no-dev --no-editable

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY pyproject.toml /app
COPY .python-version /app
COPY uv.lock /app
COPY src /app/src
COPY LICENSE /app
COPY *.md /app

COPY .env.example /app/.env.example
COPY tests /app/tests
COPY examples /app/examples

# Install project specifics
# Nothing yet

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --all-extras --no-dev --no-editable


FROM base AS target

ENV OE_PYTHON_TEMPLATE_RUNNING_IN_CONTAINER=1

# We don't want to run the app as root
RUN <<EOT
groupadd -r app
useradd -r -d /app -g app -N app
EOT

USER app
WORKDIR /app

# We place executables in the environment at the front of the path
# Remember: we don't have UV, as we only copied the app from the builder
ENV PATH="/app/.venv/bin:$PATH"

# API will run on port 8000 by default
EXPOSE 8000/tcp

# No healthcheck by default
HEALTHCHECK NONE

# Default entrypoint is our CLI
ENTRYPOINT ["oe-python-template"]


# Target slim
FROM target AS slim

# Copy slim app
COPY --from=builder-slim --chown=app:app /app /app


# And with all extras
FROM target AS all

# Copy fat app with all extras
COPY --from=builder-all --chown=app:app /app /app

