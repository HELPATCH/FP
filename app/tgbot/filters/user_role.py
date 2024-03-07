from aiogram.filters import Filter

from app.core.models import enums


class UserRoleFilter(Filter):
    def __init__(
        self, 
        user_role: enums.UserRole | None = None
    ) -> None:
        self.user_role = user_role

    async def __call__(self, update, user_role: enums.UserRole) -> bool:
        return (self.user_role == user_role)