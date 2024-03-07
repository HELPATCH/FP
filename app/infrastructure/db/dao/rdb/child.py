from sqlalchemy import select, delete, ScalarResult, Integer, func
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.core.models import dto, enums
from app.infrastructure.db.models import Child
from app.infrastructure.db import models
from .base import BaseDAO


class ChildDao(BaseDAO[Child]):
    def __init__(self, session: Session) -> None:
        super().__init__(Child, session)

    def get_child(self, id: int):
        result: ScalarResult[Child] = self.session.scalars(
            select(Child)
            .where(Child.id == id)
        )
        return result.one_or_none()

    def get_parent_childs(self, parent_id: int):
        result: ScalarResult[Child] = self.session.scalars(
            select(Child)
            .where(Child.parent_id == parent_id)
            .order_by(Child.name)
        )
        return result.all()
    
    def get_name(self, name: str, parent_id: int):
        result: ScalarResult[Child] = self.session.scalars(
            select(Child)
            .where(Child.name == name)
            .where(Child.parent_id == parent_id)
        )
        return result.one_or_none()


    def upsert(self, parent_id:int, name: str, image_url: str, id: int | None = None):
        kwargs = dict(
            parent_id=parent_id,
            name=name,
            image_url=image_url,
            id=id,
        )
        saved = self.session.execute(
            insert(Child)
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(Child.id,), set_=kwargs, where=Child.id == id
            )
            .returning(Child)
        )
        return saved.scalar_one().to_dto()

    def delete(self, id: int):
        self.session.execute(
            delete(Child)
            .where(Child.id==id)
        )