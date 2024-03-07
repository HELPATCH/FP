from app.tgbot.config.models.bot import BotConfig


def load_bot_config(dct: dict) -> BotConfig:
    return BotConfig(
        token=dct["token"],
    )