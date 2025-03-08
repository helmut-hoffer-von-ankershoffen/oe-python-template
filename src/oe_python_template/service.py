"""Service of OE Python Template."""

import os
from dotenv import load_dotenv

load_dotenv()
THE_VAR = os.getenv("THE_VAR", "not defined")


class Service:
    """Service of OE Python Template."""

    def __init__(self) -> None:
        """Initialize service."""

    @staticmethod
    def get_hello_world() -> str:
        """
        Get a hello world message.

        Returns:
            str: Hello world message.
        """
        return f"Hello, world! The value of THE_VAR is {THE_VAR}"
