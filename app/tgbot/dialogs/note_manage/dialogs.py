from textwrap import dedent

from aiogram import F

from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.text import (
    Const,
    Format,
    Jinja,
)
from aiogram_dialog.widgets.kbd import (
    Row,
    Group,
    Button,
    Start,
    Cancel,
    Select,
    ScrollingGroup
)

from app.core.models import enums
from app.tgbot import states
from app.tgbot.dialogs.getters import ( getter_notes, getter_note )
from app.tgbot.dialogs.handlers import start_note, start_note_create
from .handlers import show_edit_note, delete_note_handler


notes = Dialog(
    Window(
        Const("Каталог заметок"),
        ScrollingGroup(
            Select(
                Format("{item.name}"),
                id="notes",
                item_id_getter=lambda x: x.id,
                items="notes",
                on_click=start_note
            ),
            id="notes_sg",
            width=1,
            height=10,
            hide_on_single_page=True
        ),
        Group(
            Row(
                Button(
                    Const("+ Добавить заметку"),
                    id="note_create",
                    on_click=start_note_create,
                ),
            ),
            when=F["middleware_data"]["user"].role == enums.UserRole.ADMIN
        ),
        Row(
            Start(
                Const("Главное меню"), 
                id="main_menu", 
                state=states.MainMenuSG.main,
                mode=StartMode.RESET_STACK
            ),
            Cancel(Const("« Назад")),
        ),
        state=states.NotesSG.notes,
        getter=getter_notes
    )
)


note = Dialog(
    Window(
        Jinja(
            dedent(
                """
                <b>{{note.name}}</b>

                {{note.comment}}
                """
            )
        ),
        Group(
            Row(
                Button(
                    Const("Удалить"),
                    id="delete",
                    on_click=delete_note_handler
                ),
                Button(
                    Const("✑ Реадактировать"),
                    id="edit",
                    on_click=show_edit_note,
                ),
            ),
            when=F["middleware_data"]["user"].role == enums.UserRole.ADMIN
        ),
        Row(
            Start(
                Const("Главное меню"), 
                id="main_menu", 
                state=states.MainMenuSG.main,
                mode=StartMode.RESET_STACK
            ),
            Cancel(Const("« Назад")),
        ),
        state=states.NoteSG.note,
        getter=getter_note
    )
)