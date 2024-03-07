from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.orm import sessionmaker, Session
from jinja2 import Environment

from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot.utils.data import MiddlewareData


class InitMiddleware(BaseMiddleware):
    def __init__(
        self,
        pool: sessionmaker[Session],
        jinja: Environment
    ) -> None:
        self.pool = pool
        self.jinja = jinja

    async def __call__(  # type: ignore[override]
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: MiddlewareData,
    ) -> Any:
        with self.pool() as session:
            holder_dao = HolderDao(session)
            data["dao"] = holder_dao
        data["jinja"] = self.jinja
        result = await handler(event, data)
        del data["dao"]
        with self.pool() as session:
            session.close()
        return result
