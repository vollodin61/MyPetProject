from datetime import datetime
from environs import Env
from icecream import ic
from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


my_ice = ic
my_ice.configureOutput(includeContext=True, prefix=datetime.now().strftime('%Y-%m-%d %H:%M:%S '))

env = Env()
env.read_env()


class Settings(BaseSettings):
	POSTGRES_HOST: str = env("POSTGRES_HOST")
	POSTGRES_PORT: int = env("POSTGRES_PORT")
	POSTGRES_USER: str = env("POSTGRES_USER")
	POSTGRES_PASSWORD: str = env("POSTGRES_PASSWORD")
	DB_NAME: str = env("DB_NAME")

	@property
	def asyncpg_url(self):
		return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.DB_NAME}"

	@property
	def psycopg2_url(self):
		return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.DB_NAME}"


settings = Settings()


class Engines:
	async_engine = create_async_engine(url=settings.asyncpg_url, echo=True, max_overflow=10)
	async_session_factory = async_sessionmaker(async_engine)

	sync_engine = create_engine(url=settings.psycopg2_url, echo=True, max_overflow=10)
	sync_session_factory = sessionmaker(sync_engine)
