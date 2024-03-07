from sqlalchemy import Text, BigInteger, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import dto, enums
from app.infrastructure.db.models.base import Base


class Chat(Base):
    __tablename__ = "chats"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    type: Mapped[enums.ChatType] = mapped_column(Enum(enums.ChatType))
    title: Mapped[str] = mapped_column(Text, nullable=True)
    username: Mapped[str] = mapped_column(Text, nullable=True)

    def to_dto(self) -> dto.Chat:
        return dto.Chat(
            tg_id=self.tg_id,
            db_id=self.id,
            title=self.title,
            type=self.type,
        )
