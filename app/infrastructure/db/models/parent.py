from sqlalchemy import Text, Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import dto
from app.infrastructure.db.models.base import Base


class Parent(Base):
    __tablename__ = "parents"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    catalog_id: Mapped[int] = mapped_column(Integer, ForeignKey("catalogs.id"))
    name: Mapped[str] = mapped_column(Text, nullable=True)
    num: Mapped[str] = mapped_column(Text, nullable=True)
    
    def to_dto(self) -> dto.Parent:
        return dto.Parent(
            id=self.id,
            catalog_id=self.catalog_id,
            name=self.name,
            num=self.num
        )