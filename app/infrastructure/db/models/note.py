from sqlalchemy import Integer, Text, ForeignKey, sql
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import dto
from app.infrastructure.db.models.base import Base


class Note(Base):
    __tablename__ = "notes"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=True)

    def to_dto(self) -> dto.Note:
        return dto.Note(
            id=self.id,
            name=self.name,
            comment=self.comment,
        )