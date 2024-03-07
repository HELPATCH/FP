from redis.asyncio import Redis
from sqlalchemy.engine import make_url
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from app.infrastructure.db.config.models.db import DBConfig, RedisConfig


def create_pool(db_config: DBConfig) -> sessionmaker[Session]:
    engine = create_engine_db(db_config)
    return create_sessionmaker(engine)


def create_engine_db(db_config: DBConfig) -> Engine:
    return create_engine(url=make_url(db_config.uri), echo=db_config.echo, pool_size=0)


def create_sessionmaker(engine: Engine) -> sessionmaker[Session]:
    pool: sessionmaker[Session] = sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False
    )
    return pool


def create_redis(config: RedisConfig) -> Redis:
    return Redis(host=config.url, port=config.port, db=config.db)