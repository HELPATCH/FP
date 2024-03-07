from app.core.models import dto
from app.infrastructure.db.dao.rdb import ChatDao


def upsert_chat(dao: ChatDao, chat: dto.Chat) -> dto.Chat:
    saved_chat = dao.upsert_chat(chat)
    dao.commit()
    return saved_chat


def update_chat_id(dao: ChatDao, chat: dto.Chat, new_tg_id: int):
    dao.update_chat_id(chat, new_tg_id)
    dao.commit()
