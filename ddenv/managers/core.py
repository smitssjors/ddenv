from abc import ABC, abstractmethod
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Optional, Type

from docker import from_env


class BaseManager(ABC):
    def __init__(self, version: Optional[str], workdir: str):
        self._version = version
        self._workdir = workdir
        self.docker_client = from_env()

    @property
    def version(self) -> str:
        """Returns the version"""
        return self._version

    @property
    def workdir(self) -> str:
        """Return the current workdir"""
        return self._workdir

    def workdir_file(self, file: str) -> Path:
        """Get the path to a file in the current workdir"""
        return Path(self.workdir, file)

    @abstractmethod
    def build_base_image(self):
        """
        Build the base image used for running commands.
        Should include all dependencies.
        """


class ManagerNotFoundError(Exception):
    pass


def find_manager_mod(name: str) -> ModuleType:
    try:
        return import_module(f"ddenv.managers.{name}.manager")
    except ModuleNotFoundError:
        raise ValueError(f"Manager {name} not found")


def find_manager(name: str) -> Type[BaseManager]:
    manager_mod = find_manager_mod(name)

    try:
        return manager_mod.__dict__["Manager"]
    except KeyError:
        raise ManagerNotFoundError(
            f"`Manager(BaseManager)` class not found in {manager_mod.__name__}"
        )


def get_manager(name: str, version: str, workdir: str) -> BaseManager:
    return find_manager(name)(version, workdir)
