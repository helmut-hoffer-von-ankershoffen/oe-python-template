"""Example script demonstrating the usage of the service provided by OE Python Template."""

from dotenv import load_dotenv
from rich.console import Console

from oe_python_template.hello import Service

console = Console()

load_dotenv()

service = Service()

message = service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
