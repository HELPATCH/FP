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
from app.tgbot.dialogs.handlers import set_edit_state, process_name
from .handlers import ( on_start_catalog_edit, save_catalog_handler )


create = Dialog(
    Window(
        Const("Отправьте название каталога"),
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
                state=states.CatalogCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Cancel(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.CatalogCreateSG.name,
    ),
    Window(
        Jinja(
            dedent(
                """
                <b>Название каталога:</b> {{dialog_data.name}}
                """
            )
        ),
        Row(
            SwitchTo(
                Const("Название"), 
                id="name", 
                on_click=set_edit_state, 
                state=states.CatalogCreateSG.name
            ),
        ),
        Row(
            Button(
                Const("Сохранить"),
                id="save",
                on_click=save_catalog_handler,
                when=~F["dialog_data"]["id"]
            ),
            Button(
                Const("Обвноить"),
                id="save",
                on_click=save_catalog_handler,
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
        state=states.CatalogCreateSG.edit
    ),
    on_start=on_start_catalog_edit
)