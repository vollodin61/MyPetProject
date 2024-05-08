from aiogram.types import Message
from typing import List
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from database.sql.config.db_config import settings, Engines
from database.sql.models.user_models import Users  # noqa
from database.sql.models.product_models import Products  # noqa
from database.sql.models.base_model import Base
from logs.my_logger import MyLogger as Ml


class SyncORM:
	@staticmethod
	def create_models():
		Base.metadata.create_all(Engines.sync_engine)

	@staticmethod
	def drop_models():
		Base.metadata.drop_all(Engines.sync_engine)


# SyncORM.drop_models()
SyncORM.create_models()
