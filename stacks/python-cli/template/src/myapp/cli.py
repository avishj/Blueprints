"""CLI entry point."""

from typing import Annotated

from cyclopts import App, Parameter
from rich.console import Console
from rich.markup import escape

from myapp import __version__
from myapp.config import settings

app = App(
    name="myapp",
    help="myapp CLI.",
    version=__version__,
    version_flags=["--version", "-V"],
)
console = Console()


@app.command
def hello(name: str) -> None:
    """Greet someone.

    Parameters
    ----------
    name:
        Name to greet.
    """
    if settings.verbose:
        console.print(f"[dim]greeting name={escape(name)}[/dim]")
    console.print(f"Hello, [bold]{escape(name)}[/bold]!")


@app.meta.default
def main(
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    verbose: Annotated[
        bool,
        Parameter("--verbose", help="Enable verbose output."),
    ] = settings.verbose,
) -> None:
    """Run the myapp CLI."""
    settings.verbose = verbose
    app(tokens)
