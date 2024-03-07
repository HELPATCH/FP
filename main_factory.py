from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder, RedisEventIsolation
from sqlalchemy.orm import sessionmaker, Session
from jinja2 import Environment

from app.common.config.models.paths import Paths
from app.infrastructure.db.config.models.storage import StorageConfig, StorageType
from app.infrastructure.db.factory import (
    create_redis,
)
from app.tgbot.config.models.main import TgBotConfig
from app.tgbot.filters import setup_filters
from app.tgbot.handlers import setup_handlers
from app.tgbot.middlewares import setup_middlewares
from app.tgbot.dialogs import setup_dialogs


def create_bot(config: TgBotConfig) -> Bot:
    return Bot(
        token=config.bot.token,
        parse_mode=ParseMode.HTML,
    )


def create_dispatcher(
    config: TgBotConfig,
    pool: sessionmaker[Session],
    jinja: Environment
) -> Dispatcher:
    dp = create_only_dispatcher(config)
    setup_filters(dp)
    setup_middlewares(
        dp=dp,
        pool=pool,
        jinja=jinja,
    )
    setup_handlers(dp)
    setup_dialogs(dp)
    return dp


def create_only_dispatcher(config: TgBotConfig):
    dp = Dispatcher(
        storage=create_storage(config.storage),
        events_isolation=create_event_isolation(config.storage),
    )
    return dp


def create_storage(config: StorageConfig) -> BaseStorage:
    match config.type_:
        case StorageType.memory:
            return MemoryStorage()
        case StorageType.redis:
            if config.redis is None:
                raise ValueError("you have to specify redis config for use redis storage")
            return RedisStorage(
                create_redis(config.redis), key_builder=DefaultKeyBuilder(with_destiny=True)
            )
        case _:
            raise NotImplementedError



def create_event_isolation(config: StorageConfig):
    match config.type_:
        case StorageType.memory:
            return SimpleEventIsolation()
        case StorageType.redis:
            if config.redis is None:
                raise ValueError("you have to specify redis config for use redis storage")
            return RedisEventIsolation(config.redis)
        case _:
            raise NotImplementedError
