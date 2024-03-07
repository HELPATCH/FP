from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from app.infrastructure.db.config.models.db import DBConfig, RedisConfig
from .paths import Paths


@dataclass
class Config:
    paths: Paths
    db: DBConfig

    @property
    def app_dir(self) -> Path:
        return self.paths.app_dir

    @property
    def config_path(self) -> Path:
        return self.paths.config_path
