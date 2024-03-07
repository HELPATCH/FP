from aiogram import F
from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.text import Const, Jinja
from aiogram_dialog.widgets.kbd import Group, Row, ScrollingGroup, Button, SwitchTo, Back, Start, Cancel, Select, Radio

from app.core.models import enums

from app.tgbot import states
from app.tgbot.dialogs.widgets import CustomMedia
from app.tgbot.dialogs.handlers import (
    start_parent, 
    show_create_parent,
    select_child, 
    show_create_child, 
    delete_parent_handler, 
    delete_child_handler,
    delete_catalog_handler,
)
from app.tgbot.dialogs.getters import getter_catalog_parents, getter_catalog, getter_parent, getter_parent_childs, getter_child
from .handlers import show_edit_catalog, show_edit_parent, show_edit_child


parents = Dialog(
    Window(
        Jinja("Каталог: {{catalog.name}}"),
        ScrollingGroup(
            Select(
                Jinja("{{item.name}} {{item.num|default('', True)}}"),
                id="parents",
                item_id_getter=lambda x: x.id,
                items="parents",
                on_click=start_parent
            ),
            id="parents_sg",
            width=2,
            height=8,
            hide_on_single_page=True
        ),
        Group(
            Button(
                Const("Удалить каталог"),
                id="delete_catalog",
                on_click=delete_catalog_handler,
            ),
            Button(
                Const("Изменить каталог"),
                id="edit_catalog",
                on_click=show_edit_catalog,
            ),
            Button(
                Const("+ Добавить модель"),
                id="create_parent",
                on_click=show_create_parent
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
        state=states.ParentsSG.parents,
        getter=(getter_catalog_parents, getter_catalog)
    )
)


parent = Dialog(
    Window(
        Jinja("<b>Модель: </b>{{parent.name}} {{parent.num|default('', True)}}"),
        Jinja(
            "<b>Цвет:</b> {{child.name}}",
            when=F["child"]
        ),
        Group(
            Button(
                Const("Удалить модель"),
                id="delete_parent",
                on_click=delete_parent_handler,
            ),
            Button(
                Const("Изменить модель"),
                id="edit_parent",
                on_click=show_edit_parent,
            ),
            Group(
                Button(
                    Const("Удалить цвет"),
                    id="delete_child",
                    on_click=delete_child_handler,
                ),
                Button(
                    Const("Изменить цвет"),
                    id="edit_child",
                    on_click=show_edit_child,
                ),
                when=F["child"]
            ),
            Button(
                Const("+ Добавить цвет"),
                id="create_child",
                on_click=show_create_child
            ),
            when=F["middleware_data"]["user"].role == enums.UserRole.ADMIN
        ),
        CustomMedia(item="child", type=ContentType.PHOTO, file_id="image_url", when=F["child"]),
        ScrollingGroup(
            Radio(
                # Jinja("{{item.name}}"),
                checked_text=Jinja("[{{item.name}}]"),
                unchecked_text=Jinja("{{item.name}}"),
                id="childs",
                item_id_getter=lambda x: x.id,
                items="parent_childs",
                on_click=select_child
            ),
            id="childs_sg",
            width=2,
            height=8,
            hide_on_single_page=True
        ),
        Row(
            Start(
                Const("Главное меню"),
                id="main_menu",
                state=states.MainMenuSG.main
            ),
            Cancel(Const("« Назад"),),
        ),
        state=states.ParentSG.parent,
        getter=(getter_parent, getter_parent_childs, getter_child)
    )
)