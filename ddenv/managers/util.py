from pathlib import Path
from shutil import copy


def dockerfile_path(file_path: str) -> Path:
    return Path(file_path).parent / "Dockerfile"


def copy_files(*srcs: Path | str, dst: str):
    for src in srcs:
        copy(src, dst)
