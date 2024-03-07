from typing import TypedDict, Any

from aiogram import types, Bot, Router
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import BaseStorage

from app.core.models import dto
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot.config.models.bot import BotConfig


class AiogramMiddlewareData(TypedDict, total=False):
    event_from_user: types.User
    event_chat: types.Chat
    bot: Bot
    fsm_storage: BaseStorage
    state: FSMContext
    raw_state: Any
    handler: HandlerObject
    event_update: types.Update
    event_router: Router


class MiddlewareData(AiogramMiddlewareData, total=False):
    config: BotConfig
    dao: HolderDao
    user: dto.User | None
    chat: dto.Chat | None