"""Service of the hello module."""

import secrets
import string
from http import HTTPStatus
from typing import Any

import logfire
import requests

from oe_python_template.utils import BaseService, Health

from ._constants import HELLO_WORLD_DE_DE, HELLO_WORLD_EN_US
from ._models import Echo, Utterance
from ._settings import Language, Settings


# Services derived from BaseService and exported by modules via their __init__.py are automatically registered
# with the system module, enabling for dynamic discovery of health, info and further functionality.
class Service(BaseService):
    """Service of the hello module."""

    _settings: Settings

    def __init__(self) -> None:
        """Initialize service."""
        super().__init__(Settings)  # automatically loads and validates the settings

    def info(self) -> dict[str, Any]:  # noqa: PLR6301
        """Determine info of this service.

        Returns:
            dict[str,Any]: The info of this service.
        """
        random_string = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(5))

        return {"noise": random_string}

    @staticmethod
    def _determine_connectivity() -> Health:
        """Determine healthiness of connectivity with the Internet.

        - Performs HTTP GET request to https://connectivitycheck.gstatic.com/generate_204
        - If the call fails or does not return the expected response status, the health is DOWN.
        - If the call succeeds, the health is UP.

        Returns:
            Health: The healthiness of connectivity.
        """
        try:
            response = requests.get("https://connectivitycheck.gstatic.com/generate_204", timeout=5)
            if response.status_code == HTTPStatus.NO_CONTENT:
                return Health(status=Health.Code.UP)
            return Health(status=Health.Code.DOWN, reason=f"Unexpected response status: {response.status_code}")
        except requests.RequestException as e:
            return Health(status=Health.Code.DOWN, reason=str(e))

    def health(self) -> Health:
        """Determine health of hello service.

        Returns:
            Health: The health of the service.
        """
        return Health(
            status=Health.Code.UP,
            components={
                "connectivity": self._determine_connectivity(),
            },
        )

    def get_hello_world(self) -> str:
        """
        Get a hello world message.

        Returns:
            str: Hello world message.
        """
        messages_sent = logfire.metric_counter("hello_world_messages_sent")
        messages_sent.add(1)

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
