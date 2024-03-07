from app.infrastructure.db.dao.rdb import ParentDao


def get_parents(dao: ParentDao):
    return dao.get_parents()


def get_parent(dao: ParentDao, id: int):
    return dao._get_by_id(id)


def get_catalog_parents(dao: ParentDao, catalog_id: int):
    return dao.get_catalog_parents(catalog_id)


def upsert_parent(dao: ParentDao, catalog_id: int, name: str, num: float, id: int | None = None):
    saved = dao.upsert(catalog_id, name, num, id)
    dao.commit()
    return saved


def delete_parent(dao: ParentDao, id: int):
    dao.delete(id)
    dao.commit()