from textwrap import dedent

from aiogram import F

from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.text import (
    Const,
    Jinja,
)
from aiogram_dialog.widgets.kbd import (
    Row,
    Button,
    SwitchTo,
    Back,
    Start,
    Cancel,
)
from aiogram_dialog.widgets.input import TextInput

from app.tgbot import states
from app.tgbot.dialogs.handlers import set_edit_state, process_name, process_comment
from .handlers import on_start_note_edit, save_note


create = Dialog(
    Window(
        Const("Отправьте название заметки:"),
        TextInput(id="name", on_success=process_name),
        Row(
            Start(
                Const("Главное меню"), 
                id="main_menu", 
                state=states.MainMenuSG.main,
                mode=StartMode.RESET_STACK
            ),
            SwitchTo(
                Const("« Назад"),
                id="note_edit",
                state=states.NoteCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Cancel(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.NoteCreateSG.name
    ),
    Window(
        Const("Отправьте комментарий заметки:"),
        TextInput(id="comment", on_success=process_comment),
        Row(
            Start(
                Const("Главное меню"), 
                id="main_menu", 
                state=states.MainMenuSG.main,
                mode=StartMode.RESET_STACK
            ),
            SwitchTo(
                Const("« Назад"),
                id="note_edit",
                state=states.NoteCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Back(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.NoteCreateSG.comment
    ),
    Window(
        Jinja(
            dedent(
                """
                <b>{{dialog_data.name}}</b>

                {{dialog_data.comment}}
                """
            )
        ),
        Row(
            SwitchTo(
                Const("Название"), 
                id="name", 
                on_click=set_edit_state, 
                state=states.NoteCreateSG.name
            ),
            SwitchTo(
                Const("Комментарий"), 
                id="comment", 
                on_click=set_edit_state, 
                state=states.NoteCreateSG.comment
            ),
        ),
        Button(
            Const("Сохранить"),
            id="save_note",
            on_click=save_note,
        ),
        Row(
            Start(
                Const("Главное меню"), 
                id="main_menu", 
                state=states.MainMenuSG.main,
                mode=StartMode.RESET_STACK
            ),
            Cancel(Const("« Отменить")),
        ),
        state=states.NoteCreateSG.edit
    ),
    on_start=on_start_note_edit
)