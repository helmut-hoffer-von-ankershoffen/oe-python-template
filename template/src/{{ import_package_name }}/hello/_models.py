"""Models of the hello module."""

from pydantic import BaseModel, Field

_UTTERANCE_EXAMPLE = "Hello, world!"
_ECHO_EXAMPLE = "HELLO, WORLD!"


class Utterance(BaseModel):
    """Model representing a text utterance."""

    text: str = Field(
        ...,
        min_length=1,
        description="The utterance to echo back",
        examples=[_UTTERANCE_EXAMPLE],
    )


class Echo(BaseModel):
    """Response model for echo endpoint."""

    text: str = Field(
        ...,
        min_length=1,
        description="The echo",
        examples=[_ECHO_EXAMPLE],
    )
