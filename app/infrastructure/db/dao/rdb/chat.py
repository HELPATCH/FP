from sqlalchemy import select, ScalarResult
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.core.models import dto
from app.infrastructure.db.models import Chat
from .base import BaseDAO


class ChatDao(BaseDAO[Chat]):
    def __init__(self, session: Session) -> None:
        super().__init__(Chat, session)

    def get_by_tg_id(self, tg_id: int) -> dto.User:
        result = self._get_by_tg_id(tg_id)
        return result.to_dto() if result else result

    def _get_by_tg_id(self, tg_id: int) -> Chat:
        result: ScalarResult[Chat] = self.session.scalars(
            select(Chat).where(Chat.tg_id == tg_id)
        )
        return result.one_or_none()

    def upsert_chat(self, chat: dto.Chat) -> dto.Chat:
        kwargs = dict(tg_id=chat.tg_id, title=chat.title, username=chat.username, type=chat.type)
        saved_chat = self.session.execute(
            insert(Chat)
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(Chat.tg_id,), set_=kwargs, where=Chat.tg_id == chat.tg_id
            )
            .returning(Chat)
        )
        return saved_chat.scalar_one().to_dto()

    def update_chat_id(self, chat: dto.Chat, new_id: int):
        chat_db = self._get_by_tg_id(chat.tg_id)
        chat_db.tg_id = new_id
        self._save(chat_db)
