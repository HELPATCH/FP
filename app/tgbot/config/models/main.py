from __future__ import annotations

from dataclasses import dataclass

from app.common.config.models.main import Config
from app.infrastructure.db.config.models.storage import StorageConfig
from app.tgbot.config.models.bot import BotConfig


@dataclass
class TgBotConfig(Config):
    bot: BotConfig
    storage: StorageConfig

    @classmethod
    def from_base(
        cls,
        base: Config,
        bot: BotConfig,
        storage: StorageConfig,
    ):
        return cls(
            paths=base.paths,
            db=base.db,
            bot=bot,
            storage=storage,
        )
