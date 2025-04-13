"""Sentry integration for application monitoring."""

from typing import Annotated

import sentry_sdk
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sentry_sdk.integrations.typer import TyperIntegration

from ._constants import __env__, __env_file__, __project_name__, __version__
from ._settings import load_settings


class SentrySettings(BaseSettings):
    """Configuration settings for Sentry integration."""

    model_config = SettingsConfigDict(
        env_prefix=f"{__project_name__.upper()}_SENTRY_",
        env_file=__env_file__,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    dsn: Annotated[
        SecretStr | None,
        Field(description="Sentry DSN", examples=["https://SECRET@SECRET.ingest.de.sentry.io/SECRET"], default=None),
    ]

    debug: Annotated[
        bool,
        Field(description="Debug (https://docs.sentry.io/platforms/python/configuration/options/)", default=False),
    ]

    send_default_pii: Annotated[
        bool,
        Field(
            description="Send default personal identifiable information (https://docs.sentry.io/platforms/python/configuration/options/)",
            default=False,
        ),
    ]

    max_breadcrumbs: Annotated[
        int,
        Field(
            description="Max breadcrumbs (https://docs.sentry.io/platforms/python/configuration/options/#max_breadcrumbs)",
            default=5.0,
        ),
    ]
    sample_rate: Annotated[
        float,
        Field(
            description="Sample Rate (https://docs.sentry.io/platforms/python/configuration/sampling/#sampling-error-events)",
            default=1.0,
        ),
    ]
    traces_sample_rate: Annotated[
        float,
        Field(
            description="Traces Sample Rate (https://docs.sentry.io/platforms/python/configuration/sampling/#configuring-the-transaction-sample-rate)",
            default=1.0,
        ),
    ]
    profiles_sample_rate: Annotated[
        float,
        Field(
            description="Traces Sample Rate (https://docs.sentry.io/platforms/python/tracing/#configure)",
            default=1.0,
        ),
    ]


def sentry_initialize() -> bool:
    """Initialize Sentry integration.

    Returns:
        bool: True if initialized successfully, False otherwise
    """
    settings = load_settings(SentrySettings)

    if settings.dsn is None:
        return False

    sentry_sdk.init(
        release=f"{__project_name__}@{__version__}",  # https://docs.sentry.io/platforms/python/configuration/releases/,
        environment=__env__,
        dsn=settings.dsn.get_secret_value(),
        max_breadcrumbs=settings.max_breadcrumbs,
        debug=settings.debug,
        send_default_pii=settings.send_default_pii,
        sample_rate=settings.sample_rate,
        traces_sample_rate=settings.traces_sample_rate,
        profiles_sample_rate=settings.profiles_sample_rate,
        integrations=[TyperIntegration()],
    )

    return True
