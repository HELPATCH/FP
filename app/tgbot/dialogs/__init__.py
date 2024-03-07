from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs as set_dialogs

from app.tgbot.dialogs import (
    main_menu,
    catalog_manage,
    catalog_scn,
    parent_manage,
    parent_scn,
    child_scn,
    note_manage,
    note_scn
)


def setup_dialogs(dp: Dispatcher):
    main_menu.setup(dp)
    catalog_manage.setup(dp)
    catalog_scn.setup(dp)
    parent_manage.setup(dp)
    parent_scn.setup(dp)
    child_scn.setup(dp)
    note_manage.setup(dp)
    note_scn.setup(dp)
    set_dialogs(dp)