from tempfile import TemporaryDirectory
from typing import Final

from ddenv.managers.core import BaseManager
from ddenv.managers.util import copy_files, dockerfile_path

DEFAULT_VERSION: Final[str] = "lts"


class Manager(BaseManager):
    @property
    def version(self) -> str:
        if self._version is None:
            return DEFAULT_VERSION
        return self._version

    def build_base_image(self):
        with TemporaryDirectory() as tempdir:
            copy_files(
                dockerfile_path(__file__),
                self.workdir_file("package.json"),
                self.workdir_file("yarn.lock"),
                dst=tempdir,
            )

            self.docker_client.images.build(
                path=tempdir, rm=True, buildargs={"VERSION": self.version}
            )
