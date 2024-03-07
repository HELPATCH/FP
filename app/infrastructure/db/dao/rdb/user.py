from sqlalchemy import select, update, ScalarResult
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.core.models import dto, enums
from app.infrastructure.db.models import User
from app.infrastructure.db import models
from .base import BaseDAO


class UserDao(BaseDAO[User]):
    def __init__(self, session: Session) -> None:
        super().__init__(User, session)

    def get_by_id(self, id: int) -> dto.User:
        result = self._get_by_id(id)
        return result.to_dto() if result else result

    def get_by_tg_id(self, tg_id: int) -> dto.User:
        result = self._get_by_tg_id(tg_id)
        return result.to_dto() if result else result

    def _get_by_tg_id(self, tg_id: int) -> User:
        result: ScalarResult[User] = self.session.scalars(
            select(User).where(User.tg_id == tg_id)
        )
        return result.one_or_none()

    def set_role(self, user_id: int, role: enums.UserRole):
        self.session.execute(
            update(models.User)
            .where(models.User.id == user_id)
            .values(role=role)
        )

    def upsert_user(self, user: dto.User) -> dto.User:
        kwargs = {
            "tg_id": user.tg_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "is_bot": user.is_bot,
        }
        saved_user = self.session.execute(
            insert(User)
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(User.tg_id,), set_=kwargs, where=User.tg_id == user.tg_id
            )
            .returning(User)
        )
        return saved_user.scalar_one().to_dto()