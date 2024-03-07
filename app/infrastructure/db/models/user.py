from datetime import datetime

from sqlalchemy import Text, BigInteger, Integer, Boolean, Enum, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import dto, enums
from app.infrastructure.db.models.base import Base


class User(Base):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(Text, nullable=True)
    last_name: Mapped[str] = mapped_column(Text, nullable=True)
    username: Mapped[str] = mapped_column(Text, nullable=True)
    is_bot: Mapped[bool] = mapped_column(Boolean, default=False)
    role: Mapped[enums.UserRole] = mapped_column(
        Enum(enums.UserRole, name="user_role"),
        default=enums.UserRole.USER,
        nullable=False,
    )
    at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(),
        server_default=func.now(),
        nullable=False,
    )

    def to_dto(self) -> dto.User:
        return dto.User(
            id=self.id,
            tg_id=self.tg_id,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            is_bot=self.is_bot,
            role=self.role,
            at=self.at
        )
