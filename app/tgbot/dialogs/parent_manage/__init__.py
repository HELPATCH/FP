from aiogram import Dispatcher

from .dialogs import parents, parent


def setup(dp: Dispatcher):
    dp.include_router(parent)
    dp.include_router(parents)