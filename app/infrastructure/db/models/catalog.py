from sqlalchemy import Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import dto
from app.infrastructure.db.models.base import Base


class Catalog(Base):
    __tablename__ = "catalogs"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    
    def to_dto(self) -> dto.Catalog:
        return dto.Catalog(
            id=self.id,
            name=self.name,
        )