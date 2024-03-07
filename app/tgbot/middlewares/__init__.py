from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker, Session
from jinja2 import Environment

from .data_load_middleware import LoadDataMiddleware
from .init_middleware import InitMiddleware
from .user_role_middleware import UserRoleMiddleware


def setup_middlewares(
    dp: Dispatcher,
    pool: sessionmaker[Session],
    jinja: Environment,
):
    dp.update.middleware(InitMiddleware(pool=pool, jinja=jinja))
    dp.update.middleware(LoadDataMiddleware())
    dp.update.middleware(UserRoleMiddleware())
    dp.errors.middleware(InitMiddleware(pool=pool, jinja=jinja))
    dp.errors.middleware(LoadDataMiddleware())
    dp.errors.middleware(UserRoleMiddleware())