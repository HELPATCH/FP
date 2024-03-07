from typing import Optional, Union

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Const, Text
from aiogram_dialog.widgets.media import Media
from aiogram_dialog.widgets.media.dynamic import MediaSelector

from aiogram.enums import ContentType


class UrlMedia(Media):
    def __init__(
        self,
        item: str,
        field: str,
        content_type: ContentType,
        when: WhenCondition = None,
    ):
        super().__init__(when)
        self.item = item
        self.field = field
        self.content_type = content_type

    async def _render_media(
            self, data: dict, manager: DialogManager,
    ) -> Optional[MediaAttachment]:
        media: Optional[MediaAttachment] = MediaAttachment(
            self.content_type, 
            url=getattr(data.get(self.item), self.field)
        )
        return media
    

class CustomMedia(Media):
    def __init__(
        self,
        type: ContentType,
        item: str | None = None,
        path: Union[str, None] = None,
        url: Union[str, None] = None,
        file_id: Union[str, None] = None,
        when: WhenCondition = None,
    ):
        super().__init__(when)
        self.item = item
        self.type = type
        if not url and not path and not file_id:
            raise ValueError("Neither url, path nor file_id are provided")
        self.path = path
        self.url = url
        self.file_id = file_id

    async def _render_media(
            self, data: dict, manager: DialogManager,
    ) -> Optional[MediaAttachment]:
        dialog_data = manager.dialog_data
        if self.url:
            url = getattr(data.get(self.item), self.url) if self.item else dialog_data.get(self.url)
        else:
            url = None
        if self.path:
            path = getattr(data.get(self.item), self.path) if self.item else dialog_data.get(self.path)
        else:
            path = None
        if self.file_id:
            file_id = getattr(data.get(self.item), self.file_id) if self.item else dialog_data.get(self.file_id)
            if isinstance(file_id, str):
                file_id = MediaId(file_id=file_id)
        else:
            file_id = None
        media: Optional[MediaAttachment] = MediaAttachment(
            self.type, 
            url=url,
            path=path,
            file_id=file_id,
        )
        return media