from app.common.config.models.paths import Paths
from app.common.config.parser.config_file_reader import read_config
from app.common.config.parser.main import load_config as load_common_config
from app.infrastructure.db.config.parser.storage import load_storage_config
from app.tgbot.config.models.main import TgBotConfig
from app.tgbot.config.parser.bot import load_bot_config


def load_config(paths: Paths) -> TgBotConfig:
    config_dct = read_config(paths)

    return TgBotConfig.from_base(
        base=load_common_config(config_dct, paths),
        bot=load_bot_config(config_dct["bot"]),
        storage=load_storage_config(config_dct["storage"]),
    )
