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
    Next,
    Back,
    Start,
    Cancel,
)
from aiogram_dialog.widgets.input import TextInput

from app.tgbot import states
from app.tgbot.dialogs.handlers import set_edit_state, process_name, process_num
from .handlers import ( on_start_parent_edit, save_parent_handler )


create = Dialog(
    Window(
        Const("Отправьте название модели"),
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
                id="edit",
                state=states.ParentCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Cancel(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.ParentCreateSG.name,
    ),
    Window(
        Const("Отправьте номер модели"),
        TextInput(id="num", on_success=process_num),
        Next(Const("Пропустить"), when=~F["dialog_data"]["edit"]),
        Row(
            Start(
                Const("Главное меню"), 
                id="main_menu", 
                state=states.MainMenuSG.main,
                mode=StartMode.RESET_STACK
            ),
            SwitchTo(
                Const("« Назад"),
                id="edit",
                state=states.ParentCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Back(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.ParentCreateSG.num,
    ),
    Window(
        Jinja(
            dedent(
                """
                <b>Название модели:</b> {{dialog_data.name}}
                <b>Номер модели:</b> {{dialog_data.num|default('', True)}}
                """
            )
        ),
        Row(
            SwitchTo(
                Const("Название"), 
                id="name", 
                on_click=set_edit_state, 
                state=states.ParentCreateSG.name
            ),
            SwitchTo(
                Const("Номер"), 
                id="num", 
                on_click=set_edit_state, 
                state=states.ParentCreateSG.num
            ),
        ),
        Row(
            Button(
                Const("Сохранить"),
                id="save",
                on_click=save_parent_handler,
                when=~F["dialog_data"]["id"]
            ),
            Button(
                Const("Обвноить"),
                id="save",
                on_click=save_parent_handler,
                when=F["dialog_data"]["id"]
            ),
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
        state=states.ParentCreateSG.edit
    ),
    on_start=on_start_parent_edit
)