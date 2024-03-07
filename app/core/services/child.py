from app.infrastructure.db.dao.rdb import ChildDao


def get_child(dao: ChildDao, child_id: int):
    return dao.get_child(child_id)


def get_parent_childs(dao: ChildDao, parent_id: int):
    return dao.get_parent_childs(parent_id)


def upsert_child(dao: ChildDao, parent_id: int, name: str, image_url: str, id: int | None = None):
    saved = dao.upsert(parent_id, name, image_url, id)
    dao.commit()
    return saved


def delete_child(dao: ChildDao, id: int):
    dao.delete(id)
    dao.commit()