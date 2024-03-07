from app.infrastructure.db.dao.rdb import CatalogDao


def get_catalogs(dao: CatalogDao):
    return dao.get_catalogs()


def get_catalog(dao: CatalogDao, id: int):
    return dao._get_by_id(id)


def upsert_catalog(dao: CatalogDao, name: str, id: int | None = None):
    saved = dao.upsert(name, id)
    dao.commit()
    return saved


def delete_catalog(dao: CatalogDao, id: int):
    dao.delete(id)
    dao.commit()