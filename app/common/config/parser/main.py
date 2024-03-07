from app.common.config.models.main import Config
from app.common.config.models.paths import Paths
from app.infrastructure.db.config.parser.db import load_db_config, load_redis_config


def load_config(config_dct: dict, paths: Paths) -> Config:
    return Config(
        paths=paths,
        db=load_db_config(config_dct["db"]),
    )