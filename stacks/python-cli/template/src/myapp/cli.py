"""CLI entry point."""

from typing import Annotated

import typer
from rich.console import Console
from rich.markup import escape

from myapp import __version__
from myapp.config import settings

app = typer.Typer(
    name="myapp",
    help="myapp CLI.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    add_completion=False,
)
console = Console()


def version_callback(value: bool) -> None:  # noqa: FBT001
    """Print version and exit."""
    if value:
        console.print(f"myapp {__version__}")
        raise typer.Exit


@app.callback()
def main(
    _version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            help="Show version and exit.",
            callback=version_callback,
            is_eager=True,
        ),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Enable verbose output."),
    ] = settings.verbose,
) -> None:
    """Run the myapp CLI."""
    settings.verbose = verbose


@app.command()
def hello(
    name: Annotated[str, typer.Argument(help="Name to greet.")],
) -> None:
    """Greet someone."""
    if settings.verbose:
        console.print(f"[dim]greeting name={escape(name)}[/dim]")
    console.print(f"Hello, [bold]{escape(name)}[/bold]!")
