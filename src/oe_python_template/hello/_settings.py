"""Settings of the hello module."""

from enum import StrEnum
from typing import Annotated

from pydantic import BeforeValidator, Field, PlainSerializer, SecretStr
from pydantic_settings import SettingsConfigDict

from oe_python_template.utils import OpaqueSettings, __env_file__, __project_name__, strip_to_none_before_validator


class Language(StrEnum):
    """Supported languages."""

    GERMAN = "de_DE"
    US_ENGLISH = "en_US"


# Settings derived from BaseSettings and exported by modules via their __init__.py are automatically registered
# by the system module e.g. for showing all settings via the system info command.
class Settings(OpaqueSettings):
    """Settings."""

    model_config = SettingsConfigDict(
        env_prefix=f"{__project_name__.upper()}_HELLO_",
        extra="ignore",
        env_file=__env_file__,
        env_file_encoding="utf-8",
    )

    language: Annotated[
        Language,
        Field(
            Language.US_ENGLISH,
            description="Language to use for output - defaults to US english.",
        ),
    ]

    token: Annotated[
        SecretStr | None,
        BeforeValidator(strip_to_none_before_validator),  # strip and if empty set to None
        PlainSerializer(
            func=OpaqueSettings.serialize_sensitive_info, return_type=str, when_used="always"
        ),  # allow to unhide sensitive info from CLI or if user presents valid token via API
        Field(
            description="Secret token of Hello module.",
            default=None,
        ),
    ]
