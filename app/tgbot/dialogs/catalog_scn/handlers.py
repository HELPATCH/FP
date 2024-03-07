from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode

from app.core.services.catalog import (
    upsert_catalog,
    get_catalog
)
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot import states


async def on_start_catalog_edit(
    start_data: dict[str, Any], 
    dialog_manager: DialogManager
):
    if not dialog_manager.current_context().state == states.CatalogCreateSG.edit:
        return
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    catalog = get_catalog(dao.catalog, start_data["catalog_id"])
    dialog_manager.dialog_data["id"] = catalog.id
    dialog_manager.dialog_data["name"] = catalog.name


async def save_catalog_handler(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    catalog_id: str = dialog_manager.dialog_data.get("id")
    name: str = dialog_manager.dialog_data["name"]
    saved = upsert_catalog(dao.catalog, name, catalog_id)
    if saved:
        await dialog_manager.done()