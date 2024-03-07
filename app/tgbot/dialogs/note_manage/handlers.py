from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from app.core.services.note import delete_note
from app.infrastructure.db.dao.holder import HolderDao

from app.tgbot import states


async def show_edit_note(
    callback_query: CallbackQuery, 
    widget: Any, 
    dialog_manager: DialogManager
):
    await callback_query.answer()
    note_id = dialog_manager.dialog_data.get("note_id") or dialog_manager.start_data["note_id"]
    await dialog_manager.start(
        state=states.NoteCreateSG.edit, 
        data={"note_id": note_id}
    )


async def delete_note_handler(
    callback_query: CallbackQuery, 
    widget: Any, 
    dialog_manager: DialogManager
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    note_id = dialog_manager.dialog_data.get("note_id") or dialog_manager.start_data["note_id"]
    deleted = delete_note(dao.note, note_id)
    if deleted:
        await dialog_manager.done()