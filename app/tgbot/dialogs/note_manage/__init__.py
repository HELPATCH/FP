from aiogram import Dispatcher

from .dialogs import notes, note


def setup(dp: Dispatcher):
    dp.include_router(notes)
    dp.include_router(note)