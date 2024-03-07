from typing import Any

from aiogram.types import Message, CallbackQuery

from aiogram_dialog import (
    DialogManager, ShowMode 
)

from app.core.services.catalog import delete_catalog
from app.core.services.parent import delete_parent
from app.core.services.child import delete_child
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot import states


async def start_catalog(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    item_id: int,
    **_
):
    await callback_query.answer()
    await dialog_manager.start(
        state=states.ParentSG.parent,
        data={"parent_id": item_id}
    )


async def start_catalog_parents(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    item_id: int,
    **_
):
    await callback_query.answer()
    await dialog_manager.start(
        state=states.ParentsSG.parents,
        data={"catalog_id": item_id}
    )


async def start_parent(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    item_id: int,
    **_
):
    await callback_query.answer()
    await dialog_manager.start(
        state=states.ParentSG.parent,
        data={"parent_id": item_id}
    )


async def show_create_parent(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    catalog_id = dialog_manager.dialog_data.get("catalog_id") or dialog_manager.start_data["catalog_id"]
    await dialog_manager.start(
        state=states.ParentCreateSG.name,
        data={"catalog_id": catalog_id}
    )


async def show_create_child(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    parent_id = dialog_manager.dialog_data.get("parent_id") or dialog_manager.start_data["parent_id"]
    await dialog_manager.start(
        state=states.ChildCreateSG.name,
        data={"parent_id": parent_id}
    )


async def select_child(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    item_id: int,
    **_
):
    await callback_query.answer()
    dialog_manager.dialog_data["child_id"] = item_id


async def process_name(
    message: Message, 
    widget: Any, 
    dialog_manager: DialogManager, 
    value: str
):
    dialog_manager.show_mode = ShowMode.EDIT
    await message.delete()
    dialog_manager.dialog_data["name"] = value
    if edit_state := dialog_manager.dialog_data.get("edit"):
        return await dialog_manager.switch_to(state=edit_state)
    await dialog_manager.next()


async def process_num(
    message: Message, 
    widget: Any, 
    dialog_manager: DialogManager, 
    value: str
):
    dialog_manager.show_mode = ShowMode.EDIT
    await message.delete()
    dialog_manager.dialog_data["num"] = value
    if edit_state := dialog_manager.dialog_data.get("edit"):
        return await dialog_manager.switch_to(state=edit_state)
    await dialog_manager.next()


async def process_comment(
    message: Message, 
    widget: Any, 
    dialog_manager: DialogManager, 
    value: str
):
    dialog_manager.show_mode = ShowMode.EDIT
    await message.delete()
    dialog_manager.dialog_data["comment"] = value
    if edit_state := dialog_manager.dialog_data.get("edit"):
        return await dialog_manager.switch_to(state=edit_state)
    await dialog_manager.next()


async def process_image(
    message: Message, 
    widget: Any,
    dialog_manager: DialogManager
):
    dialog_manager.show_mode = ShowMode.EDIT
    await message.delete()
    dialog_manager.dialog_data["image"] = message.photo[-1].file_id
    if edit_state := dialog_manager.dialog_data.get("edit"):
        return await dialog_manager.switch_to(state=edit_state)
    await dialog_manager.next()


async def delete_catalog_handler(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    catalog_id: str = dialog_manager.dialog_data.get("catalog_id") or dialog_manager.start_data["catalog_id"]
    delete_catalog(dao.catalog, catalog_id)
    await dialog_manager.done()


async def delete_parent_handler(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    parent_id: str = dialog_manager.dialog_data.get("parent_id") or dialog_manager.start_data["parent_id"]
    delete_parent(dao.parent, parent_id)
    await dialog_manager.done()


async def delete_child_handler(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    child_id: str = dialog_manager.dialog_data.get("child_id") or dialog_manager.start_data["child_id"]
    delete_child(dao.child, child_id)
    await dialog_manager.done()


async def start_note(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    item_id: int,
    **_
):
    await callback_query.answer()
    await dialog_manager.start(
        state=states.NoteSG.note,
        data={"note_id": item_id}
    )


async def start_note_create(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
):
    await callback_query.answer()
    await dialog_manager.start(state=states.NoteCreateSG.name)


async def set_edit_state(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dialog_manager.dialog_data["edit"] = dialog_manager.current_context().state