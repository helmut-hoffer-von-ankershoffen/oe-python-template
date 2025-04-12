"""System service."""

import json
import os
import platform
import pwd
import sys
import time
from typing import Any

from pydantic_settings import BaseSettings

from ..utils import (  # noqa: TID252
    BaseService,
    Health,
    __env__,
    __project_name__,
    __project_path__,
    __repository_url__,
    __version__,
    get_process_info,
    load_settings,
    locate_subclasses,
)


class Service(BaseService):
    """System service."""

    is_healthy: bool

    def __init__(self) -> None:
        """Initialize service."""
        super().__init__()
        self.is_healthy = True

    def health(self) -> Health:  # noqa: PLR6301
        """Determine aggregate health of the system.

        Returns:
            Health: The aggregate health of the system.

        """
        components: dict[str, Health] = {}
        for service_class in locate_subclasses(BaseService):
            if service_class is not Service:
                components[f"{service_class.__module__}.{service_class.__name__}"] = service_class().health()

        return Health(status=Health.Status.UP, components=components)

    @staticmethod
    def info(include_environ: bool = False, filter_secrets: bool = True) -> dict[str, Any]:
        """
        Get info about configuration of service.

        Returns:
            dict[str, Any]: Service configuration.
        """
        rtn = {
            "package": {
                "version": __version__,
                "name": __project_name__,
                "repository": __repository_url__,
                "local": __project_path__,
            },
            "runtime": {
                "environment": __env__,
                "python": {
                    "version": platform.python_version(),
                    "compiler": platform.python_compiler(),
                    "implementation": platform.python_implementation(),
                },
                "interpreter_path": sys.executable,
                "command_line": " ".join(sys.argv),
                "entry_point": sys.argv[0] if sys.argv else None,
                "process_info": json.loads(get_process_info().model_dump_json()),
                "username": pwd.getpwuid(os.getuid())[0],
                "host": {
                    "system": platform.system(),
                    "release": platform.release(),
                    "version": platform.version(),
                    "machine": platform.machine(),
                    "processor": platform.processor(),
                    "hostname": platform.node(),
                    "ip_address": platform.uname().node,
                    "cpu_count": os.cpu_count(),
                },
            },
        }

        if include_environ:
            if filter_secrets:
                rtn["runtime"]["environ"] = {
                    k: v
                    for k, v in os.environ.items()
                    if not (
                        "token" in k.lower()
                        or "key" in k.lower()
                        or "secret" in k.lower()
                        or "password" in k.lower()
                        or "auth" in k.lower()
                    )
                }
            else:
                rtn["runtime"]["environ"] = dict(os.environ)

        settings = {}
        for settings_class in locate_subclasses(BaseSettings):
            settings_instance = load_settings(settings_class)
            env_prefix = settings_instance.model_config.get("env_prefix", "")
            settings_dict = json.loads(settings_instance.model_dump_json())
            for key, value in settings_dict.items():
                flat_key = f"{env_prefix}{key}".upper()
                settings[flat_key] = value
        rtn["settings"] = settings

        for service_class in locate_subclasses(BaseService):
            if service_class is not Service:
                service = service_class()
                rtn[service.key()] = service.info()

        return rtn

    @staticmethod
    def div_by_zero() -> float:
        """Divide by zero to trigger an error.

        Returns:
            float: This function will raise a ZeroDivisionError before returning.
        """
        return 1 / 0

    @staticmethod
    def sleep(seconds: int) -> None:
        """Sleep for a given number of seconds.

        Args:
            seconds (int): Number of seconds to sleep.
        """
        time.sleep(seconds)
