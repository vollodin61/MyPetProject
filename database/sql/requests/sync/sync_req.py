from aiogram.types import Message
from typing import List
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from database.sql.config.db_config import settings
from database.sql.models.base_model import Base
from logs.my_logger import MyLogger as Ml


class SyncORM:
	@staticmethod
	def create_models():
		Base.metadata.create_all(settings.sync_engine)

	@staticmethod
	def drop_models():
		Base.metadata.drop_all(settings.sync_engine)


# SyncORM.create_models()
SyncORM.drop_models()