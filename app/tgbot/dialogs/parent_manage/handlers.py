from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from app.tgbot import states


async def show_edit_catalog(
   callback_query: CallbackQuery, 
    widget: Any, 
    dialog_manager: DialogManager
):
    await callback_query.answer()
    catalog_id = dialog_manager.dialog_data.get("catalog_id") or dialog_manager.start_data["catalog_id"]
    await dialog_manager.start(
        state=states.CatalogCreateSG.edit, 
        data={"catalog_id": catalog_id}
    )


async def show_edit_parent(
    callback_query: CallbackQuery, 
    widget: Any, 
    dialog_manager: DialogManager
):
    await callback_query.answer()
    parent_id = dialog_manager.dialog_data.get("parent_id") or dialog_manager.start_data["parent_id"]
    await dialog_manager.start(
        state=states.ParentCreateSG.edit, 
        data={"parent_id": parent_id}
    )


async def show_edit_child(
    callback_query: CallbackQuery,
    widget: Any, 
    dialog_manager: DialogManager
):
    await callback_query.answer()
    child_id = dialog_manager.dialog_data.get("child_id") or dialog_manager.start_data["child_id"]
    await dialog_manager.start(
        state=states.ChildCreateSG.edit, 
        data={"child_id": child_id}
    )