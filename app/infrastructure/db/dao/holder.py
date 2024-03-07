from sqlalchemy.orm import Session

from .rdb import (
    ChatDao,
    UserDao,
    CatalogDao,
    ParentDao,
    ChildDao,
    NoteDao
)


class HolderDao:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.user = UserDao(self.session)
        self.chat = ChatDao(self.session)
        self.catalog = CatalogDao(self.session)
        self.parent = ParentDao(self.session)
        self.child = ChildDao(self.session)
        self.note = NoteDao(self.session)