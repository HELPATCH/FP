from dataclasses import dataclass
from enum import Enum

from app.infrastructure.db.config.models.db import RedisConfig


class StorageType(Enum):
    memory = "memory"
    redis = "redis"


@dataclass
class StorageConfig:
    type_: StorageType
    redis: RedisConfig | None = None
