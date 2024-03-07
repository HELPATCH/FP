from aiogram_dialog import DialogManager

from app.core.services.catalog import get_catalogs, get_catalog
from app.core.services.parent import get_parents, get_parent, get_catalog_parents
from app.core.services.child import get_parent_childs, get_child
from app.core.services.note import get_notes, get_note
from app.infrastructure.db.dao.holder import HolderDao


async def getter_catalogs(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    return {
        "catalogs": get_catalogs(dao.catalog)
    }


async def getter_catalog(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    catalog_id = dialog_manager.dialog_data.get("catalog_id") or dialog_manager.start_data["catalog_id"]
    return {
        "catalog": get_catalog(dao.catalog, catalog_id)
    }


async def getter_parents(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    return {
        "parents": get_parents(dao.parent)
    }


async def getter_catalog_parents(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    catalog_id = dialog_manager.dialog_data.get("catalog_id") or dialog_manager.start_data["catalog_id"]
    return {
        "parents": get_catalog_parents(dao.parent, catalog_id)
    }


async def getter_parent(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    parent_id = dialog_manager.dialog_data.get("parent_id") or dialog_manager.start_data["parent_id"]
    return {
        "parent": get_parent(dao.parent, parent_id)
    }


async def getter_parent_childs(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    parent_id = dialog_manager.dialog_data.get("parent_id") or dialog_manager.start_data["parent_id"]
    return {
        "parent_childs": get_parent_childs(dao.child, parent_id)
    }


async def getter_child(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    child_id = dialog_manager.dialog_data.get("child_id") or dialog_manager.start_data.get("child_id")
    child = get_child(dao.child, child_id)
    return {
        "child": child,
    }


async def getter_notes(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    return {
        "notes": get_notes(dao.note)
    }


async def getter_note(
    dialog_manager: DialogManager,
    **_
):
    dao: HolderDao = dialog_manager.middleware_data["dao"]
    note_id = dialog_manager.dialog_data.get("note_id") or dialog_manager.start_data["note_id"]
    return {
        "note": get_note(dao.note, note_id)
    }