"""Settings of the notebook module."""

from pathlib import Path
from typing import Annotated

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from ..utils import OpaqueSettings, __env_file__, __project_name__  # noqa: TID252


class Settings(OpaqueSettings):
    """Settings."""

    model_config = SettingsConfigDict(
        env_prefix=f"{__project_name__.upper()}_NOTEBOOK_",
        extra="ignore",
        env_file=__env_file__,
        env_file_encoding="utf-8",
    )

    directory: Annotated[
        Path,
        Field(
            description=("Directory where the notebook files are stored. "),
            default=Path(__file__).parent.parent.parent.parent / "examples",
        ),
    ]
