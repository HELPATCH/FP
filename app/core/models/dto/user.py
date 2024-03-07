from dataclasses import dataclass
from datetime import datetime

from aiogram import types as tg

from app.core.models.enums.user_role import UserRole


@dataclass
class User:
    tg_id: int
    id: int | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_bot: bool | None = None
    role: UserRole | None = None
    at: datetime | None = None

    @property
    def fullname(self) -> str:
        if self.first_name is None:
            return ""
        if self.last_name is not None:
            return " ".join((self.first_name, self.last_name))
        return self.first_name

    @property
    def name_mention(self) -> str:
        return self.fullname or self.username or str(self.tg_id) or str(self.db_id) or "unknown"

    @classmethod
    def from_aiogram(cls, user: tg.User) -> "User":
        return cls(
            tg_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            is_bot=user.is_bot,
        )
