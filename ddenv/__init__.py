"""Docker Dev Environment, easily develop your programs using containers"""

__version__ = "0.0.1"

import os
from typing import Optional

from typer import Argument, Option, Typer, echo

from ddenv.managers.core import get_manager

app = Typer()


@app.command()
def run(
    command: Optional[list[str]] = Argument(None),
    manager: str = Option(..., "--manager", "-m"),
    version: Optional[str] = Option(None, "--version", "-v"),
):
    echo(f"ddenv {__version__}, running {manager}:{version}")
    handler = get_manager(manager, version, os.getcwd())
    if not handler.image_exists:
        echo("Building image")
        handler.build_base_image()
    else:
        echo("Image found")

    echo("Running command")
    for output in handler.run_command(command):
        echo(output.rstrip())


def main():
    app()
