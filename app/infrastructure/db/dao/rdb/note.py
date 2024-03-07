from typing import Sequence

from sqlalchemy import select, update, delete, ScalarResult, CursorResult, not_
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.infrastructure.db import models
from .base import BaseDAO


class NoteDao(BaseDAO[models.Note]):
    def __init__(self, session: Session):
        super().__init__(models.Note, session)

    def upsert_note(
        self, 
        name: str,
        comment: int, 
        note_id: int
    ):
        kwargs = dict(
            name=name,
            comment=comment,
            id=note_id,
        )
        saved_note = self.session.execute(
            insert(models.Note)
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(models.Note.id,), 
                set_=kwargs, 
                where=models.Note.id == note_id
            )
            .returning(models.Note)
        )
        return saved_note.scalar_one().to_dto()
    
    def delete_note(self, note_id: int):
        deleted_note = self.session.execute(
            delete(models.Note)
            .where(models.Note.id==note_id)
        )
        return deleted_note