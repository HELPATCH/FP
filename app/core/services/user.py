from app.core.models import dto, enums
from app.infrastructure.db.dao.rdb import UserDao


def upsert_user(dao: UserDao, user: dto.User) -> dto.User:
    saved_user = dao.upsert_user(user)
    dao.commit()
    return saved_user


def set_role(dao: UserDao, user_id: int, role: enums.UserRole):
    dao.set_role(user_id, role)
    dao.commit()