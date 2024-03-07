import os
from pathlib import Path

from app.common.config.models.paths import Paths


def get_paths() -> Paths:
    return common_get_paths("/")


def common_get_paths(env_var: str) -> Paths:
    if path := os.getenv(env_var):
        return Paths(Path(path))
    return Paths(Path(__file__).parent.parent.parent.parent.parent)
