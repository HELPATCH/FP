from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode

from app.core.services.child import (
    upsert_child,
    delete_child,
    get_child
)
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot import states


async def on_start_child_edit(
    start_data: dict[str, Any], 
    dialog_manager: DialogManager
):
    if not dialog_manager.current_context().state == states.ChildCreateSG.edit:
        return
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    child = get_child(dao.child, start_data["child_id"])
    dialog_manager.dialog_data["id"] = child.id
    dialog_manager.dialog_data["parent_id"] = child.parent_id
    dialog_manager.dialog_data["name"] = child.name
    dialog_manager.dialog_data["image"] = child.image_url


async def save_child_handler(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    child_id: str = dialog_manager.dialog_data.get("id")
    parent_id: int = dialog_manager.dialog_data.get("parent_id") or dialog_manager.start_data["parent_id"]
    name: str = dialog_manager.dialog_data["name"]
    image: str = dialog_manager.dialog_data["image"]
    saved = upsert_child(dao.child, parent_id, name, image, child_id)
    if saved:
        await dialog_manager.done()