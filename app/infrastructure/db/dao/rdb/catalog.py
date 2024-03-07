from sqlalchemy import select, delete, ScalarResult, Integer, Text, func
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.core.models import dto, enums
from app.infrastructure.db.models import Catalog
from app.infrastructure.db import models
from .base import BaseDAO


class CatalogDao(BaseDAO[Catalog]):
    def __init__(self, session: Session) -> None:
        super().__init__(Catalog, session)

    def get_catalogs(self):
        result: ScalarResult[Catalog] = self.session.scalars(
            select(Catalog)
            .order_by(func.cast(func.substr(Catalog.name, 2), Integer))
        )
        return result.all()

    def upsert(self, name: str, id: int | None = None):
        kwargs = dict(
            name=name,
            id=id,
        )
        saved = self.session.execute(
            insert(Catalog)
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(Catalog.id,), set_=kwargs, where=Catalog.id == id
            )
            .returning(Catalog)
        )
        return saved.scalar_one().to_dto()
    
    def delete(self, id: int):
        self.session.execute(
            delete(models.Child)
            .where(models.Child.parent_id.in_(
                select(models.Parent.id)
                .where(models.Parent.catalog_id==id)
            ))
        )
        self.session.execute(
            delete(models.Parent)
            .where(models.Parent.catalog_id==id)
        )
        self.session.execute(
            delete(Catalog)
            .where(Catalog.id==id)
        )
        

    def get_name(self, name: str):
        result: ScalarResult[Catalog] = self.session.scalars(
            select(Catalog)
            .where(Catalog.name == name)
        )
        return result.one_or_none()