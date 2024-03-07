from textwrap import dedent

from aiogram import F
from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.text import Const, Jinja
from aiogram_dialog.widgets.kbd import Row, ScrollingGroup, Button, SwitchTo, Back, Start, Cancel, Select

from app.tgbot import states
from app.core.models import enums
from app.tgbot.dialogs.getters import getter_notes
from app.tgbot.dialogs.handlers import start_note, start_note_create


main_menu = Dialog(
    Window(
        Const("<b>Главное меню</b>"),
        Start(Const("Каталог"), id="catalogs", state=states.CatalogsSG.catalogs),
        ScrollingGroup(
            Select(
                Jinja("{{item.name}}"),
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
        Button(
            Const("+ Добавить заметку"),
            id="note_create",
            on_click=start_note_create,
            when=F["middleware_data"]["user"].role == enums.UserRole.ADMIN
        ),
        state=states.MainMenuSG.main,
        getter=getter_notes
    ),
)