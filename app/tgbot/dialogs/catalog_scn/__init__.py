from aiogram import Dispatcher

from .dialogs import create


def setup(dp: Dispatcher):
    dp.include_router(create)