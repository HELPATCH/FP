from aiogram import Dispatcher

from app.tgbot.filters.user_role import UserRoleFilter


def setup_filters(dp: Dispatcher):
    dp.update.filter(UserRoleFilter())