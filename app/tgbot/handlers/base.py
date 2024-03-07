from aiogram import Dispatcher
from aiogram.filters import Command, ExceptionTypeFilter

from aiogram_dialog import ShowMode
from aiogram_dialog.api.exceptions import UnknownIntent

from app.tgbot import states
from app.tgbot.utils.router import StartDialog


def setup(dp: Dispatcher):
    main_menu = StartDialog(
        dp=dp,
        state=states.MainMenuSG.main,
        show_mode=ShowMode.SEND,
    )
    main_menu.message(Command("start"))
    main_menu.errors(ExceptionTypeFilter(UnknownIntent))