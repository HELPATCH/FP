from aiogram import Bot
from aiogram_dialog.widgets.text import setup_jinja as setup_jinja_internal


def setup_jinja(bot: Bot):
    return setup_jinja_internal(
        bot,
    )