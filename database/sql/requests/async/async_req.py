import asyncio

from aiogram.types import Message
from typing import List
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from database.sql.models.base_model import Base
from database.sql.config.db_config import Engines

from logs.my_logger import MyLogger as Ml


class AsyncORM:
	@staticmethod
	async def drop_models():
		async with Engines.async_engine.begin() as conn:
			await conn.run_sync(Base.metadata.drop_all)

	@staticmethod
	async def create_models():
		async with Engines.async_engine.begin() as conn:
			await conn.run_sync(Base.metadata.create_all)
