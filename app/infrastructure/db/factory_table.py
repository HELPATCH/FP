from sqlalchemy import Engine

from .models.base import Base


def create_all_tabel(engine: Engine):
    Base.metadata.create_all(engine)