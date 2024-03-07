import asyncio

from app.common.config.parser.paths import get_paths
from app.infrastructure.db.factory import (
    create_sessionmaker,
    create_engine_db,
)
from app.infrastructure.db.factory_table import create_all_tabel
from app.tgbot.config.parser.main import load_config
from main_factory import (
    create_bot,
    create_dispatcher,
)
from app.tgbot.views.jinja_filters import setup_jinja


async def main():
    paths = get_paths()

    config = load_config(paths)
    engine = create_engine_db(config.db)
    create_all_tabel(engine)
    pool = create_sessionmaker(engine)
    bot = create_bot(config)
    jinja = setup_jinja(bot)

    async with (bot.context(),):
        dp = create_dispatcher(
            config=config,
            pool=pool,
            jinja=jinja
        )
        try:
            await dp.start_polling(bot)
        finally:
            engine.dispose()


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
