from aiogram import Dispatcher

from .dialogs import catalogs


def setup(dp: Dispatcher):
    dp.include_router(catalogs)