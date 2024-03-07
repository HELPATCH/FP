from textwrap import dedent

from aiogram import F
from aiogram.enums import ContentType

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
from aiogram_dialog.widgets.input import TextInput, MessageInput

from app.tgbot import states
from app.tgbot.dialogs.widgets import CustomMedia
from app.tgbot.dialogs.handlers import set_edit_state, process_name, process_image
from .handlers import ( on_start_child_edit, save_child_handler )


create = Dialog(
    Window(
        Const("Отправьте название цвета"),
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
                state=states.ChildCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Cancel(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.ChildCreateSG.name,
    ),
    Window(
        Const("Отправьте изображение"),
        MessageInput(
            content_types=ContentType.PHOTO,
            func=process_image
        ),
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
                state=states.ChildCreateSG.edit, 
                when=F["dialog_data"]["edit"]
            ),
            Back(Const("« Назад"), when=~F["dialog_data"]["edit"]),
        ),
        Cancel(Const("« Отменить"), when=~F["dialog_data"]["edit"]),
        state=states.ChildCreateSG.image,
    ),
    Window(
        Jinja(
            dedent(
                """
                <b>Название цвета:</b> {{dialog_data.name}}
                """
            )
        ),
        CustomMedia(type=ContentType.PHOTO, file_id="image"),
        Row(
            SwitchTo(
                Const("Название"), 
                id="name", 
                on_click=set_edit_state, 
                state=states.ChildCreateSG.name
            ),
            SwitchTo(
                Const("Изображение"), 
                id="image", 
                on_click=set_edit_state, 
                state=states.ChildCreateSG.image
            ),
        ),
        Row(
            Button(
                Const("Сохранить"),
                id="save",
                on_click=save_child_handler,
                when=~F["dialog_data"]["id"]
            ),
            Button(
                Const("Обвноить"),
                id="save",
                on_click=save_child_handler,
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
        state=states.ChildCreateSG.edit
    ),
    on_start=on_start_child_edit
)