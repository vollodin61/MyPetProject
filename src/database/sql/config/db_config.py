from datetime import datetime
from typing import AsyncGenerator

from environs import Env
from icecream import ic
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Settings:
    my_ice = ic
    my_ice.configureOutput(includeContext=True, prefix=datetime.now().strftime('%Y-%m-%d %H:%M:%S '))

    env = Env()
    env.read_env()

    REDIS_HOST: str = env("REDIS_HOST")
    REDIS_PORT: str = env("REDIS_PORT")

    POSTGRES_HOST: str = env("POSTGRES_HOST")
    POSTGRES_PORT: int = env("POSTGRES_PORT")
    POSTGRES_USER: str = env("POSTGRES_USER")
    POSTGRES_PASSWORD: str = env("POSTGRES_PASSWORD")
    DB_NAME: str = env("DB_NAME")

    asyncpg_url: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}"
    psycopg2_url: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}"

    async_engine = create_async_engine(url=asyncpg_url, max_overflow=10)  # echo=True,
    async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

    sync_engine = create_engine(url=psycopg2_url, max_overflow=10)  # echo=True,
    sync_session_factory = sessionmaker(sync_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with Settings.async_session_factory() as session:
        yield session
