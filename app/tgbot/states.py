from aiogram.fsm.state import StatesGroup, State


class AppSG(StatesGroup):
    app = State()


class MainMenuSG(StatesGroup):
    main = State()
    about = State()


class CatalogsSG(StatesGroup):
    catalogs = State()


class CatalogSG(StatesGroup):
    catalog = State()


class CatalogCreateSG(StatesGroup):
    name = State()
    edit = State()


class ParentsSG(StatesGroup):
    parents = State()


class ParentSG(StatesGroup):
    parent = State()


class ParentCreateSG(StatesGroup):
    name = State()
    num = State()
    edit = State()


class ChildCreateSG(StatesGroup):
    name = State()
    image = State()
    edit = State()


class NotesSG(StatesGroup):
    notes = State()


class NoteSG(StatesGroup):
    note = State()


class NoteCreateSG(StatesGroup):
    name = State()
    comment = State()
    edit = State()