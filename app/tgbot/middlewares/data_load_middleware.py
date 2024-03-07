from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from app.core.models import dto
from app.core.services.chat import upsert_chat
from app.core.services.user import upsert_user
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot.utils.data import MiddlewareData


class LoadDataMiddleware(BaseMiddleware):
    async def __call__(  # type: ignore
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: MiddlewareData,
    ) -> Any:
        dao = data["dao"]
        if isinstance(event, Message):
            if user_tg := data.get("event_from_user", None):
                user = dao.user.get_by_tg_id(user_tg.id)
            else:
                user = None
            if chat_tg := data.get("event_chat", None):
                chat = dao.chat.get_by_tg_id(chat_tg.id)
            else:
                chat = None
        else:
            user = save_user(dao, data)
            chat = save_chat(dao, data)
        data["user"] = user
        data["chat"] = chat
        result = await handler(event, data)
        return result


def save_user(dao: HolderDao, data: MiddlewareData) -> dto.User | None:
    user = data.get("event_from_user", None)
    if not user:
        return None
    return upsert_user(dao.user, dto.User.from_aiogram(user))


def save_chat(dao: HolderDao, data: MiddlewareData) -> dto.Chat | None:
    chat = data.get("event_chat", None)
    if not chat:
        return None
    return upsert_chat(dao.chat, dto.Chat.from_aiogram(chat))
