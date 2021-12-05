"""Docker Dev Environment, easily develop your programs using containers"""

__version__ = "0.0.1"

import os
from typing import Optional

from typer import Argument, Option, Typer, echo

from ddenv.managers.core import get_manager

app = Typer()


@app.command()
def run(
    command: list[str] = Argument(...),
    manager: str = Option(..., "--manager", "-m"),
    version: Optional[str] = Option(None, "--version", "-v"),
):
    echo(f"ddenv {__version__}, running {manager}:{version}")
    echo(get_manager(manager, version, os.getcwd()).build_base_image())


def main():
    app()
