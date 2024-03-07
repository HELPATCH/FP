from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class UserRoleMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict,
    ) -> Any:
        user = data["user"]
        data["user_role"] = user.role if user else None
        result = await handler(event, data)
        return result