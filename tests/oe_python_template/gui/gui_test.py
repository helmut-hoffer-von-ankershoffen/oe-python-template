"""Tests to verify the GUI functionality."""

from nicegui.testing import User

from oe_python_template.gui import register_pages


async def test_index(user: User) -> None:
    """Test that the user sees the index page, and sees the output of the Hello service on click."""
    register_pages()
    await user.open("/")
    await user.should_see("Click me")
    user.find("Click me").click()
    await user.should_see("Hello, world!")
    await user.should_see("Choose file")
    user.find("Choose file").click()
    await user.should_see("Cancel")
    user.find("Cancel").click()
    await user.should_see("You chose None")
