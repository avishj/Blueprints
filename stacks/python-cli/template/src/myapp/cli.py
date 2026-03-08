"""CLI entry point."""

from typing import Annotated

import typer
from rich.console import Console
from rich.markup import escape

from myapp import __version__

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
) -> None:
    """myapp CLI."""


@app.command()
def hello(
    name: Annotated[str, typer.Argument(help="Name to greet.")],
) -> None:
    """Greet someone."""
    console.print(f"Hello, [bold]{escape(name)}[/bold]!")
