from typing import TypeVar, Generic
from collections.abc import Sequence

from sqlalchemy import delete, func, ScalarResult
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from sqlalchemy.orm.interfaces import ORMOption

from app.infrastructure.db.models import Base

Model = TypeVar("Model", bound=Base, covariant=True, contravariant=False)


class BaseDAO(Generic[Model]):
    def __init__(self, model: type[Model], session: Session) -> None:
        self.model = model
        self.session = session

    def _get_all(self, options: Sequence[ORMOption] = ()) -> Sequence[Model]:
        result: ScalarResult[Model] = self.session.scalars(
            select(self.model).options(*options)
        )
        return result.all()

    def _get_by_id(
        self, id_: int, options: Sequence[ORMOption] | None = None, populate_existing: bool = False
    ) -> Model:
        result = self.session.get(
            self.model, id_, options=options, populate_existing=populate_existing
        )
        return result

    def _save(self, obj: Base):
        self.session.add(obj)

    def delete_all(self):
        self.session.execute(delete(self.model))

    def _delete(self, obj: Base):
        self.session.delete(obj)

    def count(self):
        result = self.session.execute(select(func.count(self.model.id)))
        return result.scalar_one()

    def commit(self):
        self.session.commit()

    def _flush(self, *objects: Base):
        self.session.flush(objects)
