from aiogram import F
from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.text import Const, Jinja
from aiogram_dialog.widgets.kbd import Group, Row, ScrollingGroup, Button, SwitchTo, Back, Start, Cancel, Select

from app.core.models import enums

from app.tgbot import states
from app.tgbot.dialogs.handlers import start_catalog_parents
from app.tgbot.dialogs.getters import getter_catalogs

catalogs = Dialog(
    Window(
        Const("Каталог"),
        ScrollingGroup(
            Select(
                Jinja("{{item.name}}"),
                id="catalogs",
                item_id_getter=lambda x: x.id,
                items="catalogs",
                on_click=start_catalog_parents
            ),
            id="catalogs_sg",
            width=2,
            height=8,
            hide_on_single_page=True
        ),
        Row(
            Start(
                Const("+ Добавить каталог"),
                id="create_catalog",
                state=states.CatalogCreateSG.name
            ),
            when=F["middleware_data"]["user"].role == enums.UserRole.ADMIN
        ),
        Row(
            Start(
                Const("Главное меню"),
                id="main_menu",
                state=states.MainMenuSG.main
            ),
            Cancel(Const("« Назад"),),
        ),
        state=states.CatalogsSG.catalogs,
        getter=(getter_catalogs,)
    )
)