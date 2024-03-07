from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode

from app.core.services.parent import (
    upsert_parent,
    delete_parent,
    get_parent
)
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot import states


async def on_start_parent_edit(
    start_data: dict[str, Any], 
    dialog_manager: DialogManager
):
    if not dialog_manager.current_context().state == states.ParentCreateSG.edit:
        return
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    parent = get_parent(dao.parent, start_data["parent_id"])
    dialog_manager.dialog_data["id"] = parent.id
    dialog_manager.dialog_data["catalog_id"] = parent.catalog_id
    dialog_manager.dialog_data["name"] = parent.name
    dialog_manager.dialog_data["num"] = parent.num


async def save_parent_handler(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    parent_id: str = dialog_manager.dialog_data.get("id")
    catalog_id: int = dialog_manager.dialog_data.get("catalog_id") or dialog_manager.start_data["catalog_id"]
    name: str = dialog_manager.dialog_data.get("name")
    num: str = dialog_manager.dialog_data.get("num")
    saved = upsert_parent(dao.parent, catalog_id, name, num, parent_id)
    if saved:
        await dialog_manager.done()