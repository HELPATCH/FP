from app.infrastructure.db.dao import NoteDao
from app.core.models import dto


def upsert_note(dao: NoteDao, name: str, comment: str, note_id: int):
    saved = dao.upsert_note(name, comment, note_id)
    dao.commit()
    return saved


def delete_note(dao: NoteDao, note_id: int):
    deleted = dao.delete_note(note_id)
    dao.commit()
    return deleted


def get_notes(dao: NoteDao):
    return dao._get_all()


def get_note(dao: NoteDao, note_id: int):
    return dao._get_by_id(note_id)