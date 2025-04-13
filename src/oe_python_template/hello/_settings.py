"""Settings of the hello module."""

from enum import StrEnum
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from oe_python_template.utils import __env_file__, __project_name__


class Language(StrEnum):
    """Supported languages."""

    GERMAN = "de_DE"
    US_ENGLISH = "en_US"


# Settings derived from BaseSettings and exported by modules via their __init__.py are automatically registered
# by the system module e.g. for showing all settings via the system info command.
class Settings(BaseSettings):
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
