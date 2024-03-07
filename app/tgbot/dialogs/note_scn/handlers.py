from typing import Any

from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from app.core.services.note import get_note, upsert_note, delete_note
from app.infrastructure.db.dao.holder import HolderDao
from app.tgbot import states


async def on_start_note_edit(
    start_data: dict[str, Any], dialog_manager: DialogManager
):
    if not dialog_manager.current_context().state == states.NoteCreateSG.edit:
        return
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    note = get_note(dao.note, start_data["note_id"])
    dialog_manager.dialog_data["id"] = note.id
    dialog_manager.dialog_data["name"] = note.name
    dialog_manager.dialog_data["comment"] = note.comment


async def save_note(
    callback_query: CallbackQuery,
    widget: Any,
    dialog_manager: DialogManager,
    **_
):
    await callback_query.answer()
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    note_id: int = dialog_manager.dialog_data.get("id")
    name: str = dialog_manager.dialog_data["name"]
    comment: str = dialog_manager.dialog_data["comment"]
    note = upsert_note(dao.note, name, comment, note_id)
    if note:
        await dialog_manager.done()