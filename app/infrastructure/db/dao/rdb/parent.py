from sqlalchemy import select, delete, ScalarResult, Integer, Text, func
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.core.models import dto, enums
from app.infrastructure.db.models import Parent
from app.infrastructure.db import models
from .base import BaseDAO


class ParentDao(BaseDAO[Parent]):
    def __init__(self, session: Session) -> None:
        super().__init__(Parent, session)

    def get_parents(self):
        result: ScalarResult[Parent] = self.session.scalars(
            select(Parent)
        )
        return result.all()
    
    def get_catalog_parents(self, catalog_id: int):
        result: ScalarResult[Parent] = self.session.scalars(
            select(Parent)
            .where(Parent.catalog_id==catalog_id)
            .order_by(func.cast(Parent.num, Integer))
            .order_by(Parent.name)
        )
        return result.all()

    def upsert(self, catalog_id: int, name: str, num: float, id: int | None = None):
        kwargs = dict(
            catalog_id=catalog_id,
            name=name,
            num=num,
            id=id,
        )
        saved = self.session.execute(
            insert(Parent)
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(Parent.id,), set_=kwargs, where=Parent.id == id
            )
            .returning(Parent)
        )
        return saved.scalar_one().to_dto()
    
    def delete(self, id: int):
        self.session.execute(
            delete(Parent)
            .where(Parent.id==id)
        )
        self.session.execute(
            delete(models.Child)
            .where(models.Child.parent_id==id)
        )

    def get_name(self, name: str):
        result: ScalarResult[Parent] = self.session.scalars(
            select(Parent)
            .where(Parent.name == name)
        )
        return result.one_or_none()