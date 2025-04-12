"""Service of the hello module."""

import random
import string
from typing import Any

from oe_python_template.utils import BaseService, Health

from ._constants import HELLO_WORLD_DE_DE, HELLO_WORLD_EN_US
from ._models import Echo, Utterance
from ._settings import Language, Settings


class Service(BaseService):
    """Service of the hello module."""

    _settings: Settings

    def __init__(self) -> None:
        """Initialize service."""
        super().__init__(Settings)

    def info(self) -> dict[str, Any]:  # noqa: PLR6301
        """Determine info of this service.

        Returns:
            dict[str,Any]: The info of this service.
        """
        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=5))  # noqa: S311

        return {"noise": random_string}

    def health(self) -> Health:  # noqa: PLR6301
        """Determine health of hello service.

        Returns:
            Health: The health of the service.
        """
        return Health(status=Health.Status.UP)

    def get_hello_world(self) -> str:
        """
        Get a hello world message.

        Returns:
            str: Hello world message.
        """
        match self._settings.language:
            case Language.GERMAN:
                return HELLO_WORLD_DE_DE
        return HELLO_WORLD_EN_US

    @staticmethod
    def echo(utterance: Utterance) -> Echo:
        """
        Loudly echo utterance.

        Args:
            utterance (Utterance): The utterance to echo.

        Returns:
            Echo: The loudly echoed utterance.

        Raises:
            ValueError: If the utterance is empty or contains only whitespace.
        """
        return Echo(text=utterance.text.upper())
