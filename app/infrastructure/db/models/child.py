from sqlalchemy import Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import dto
from app.infrastructure.db.models.base import Base


class Child(Base):
    __tablename__ = "childs"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey("parents.id"))
    name: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str] = mapped_column(Text, nullable=False)
    
    def to_dto(self) -> dto.Child:
        return dto.Child(
            id=self.id,
            parent_id=self.parent_id,
            name=self.name,
            image_url=self.image_url
        )