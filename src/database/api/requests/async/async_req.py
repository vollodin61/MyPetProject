from src.database.sql.models.base_model import Base
from src.database.sql.config.db_config import Engines


class AsyncORM:
	@staticmethod
	async def drop_models():
		async with Engines.async_engine.begin() as conn:
			await conn.run_sync(Base.metadata.drop_all)

	@staticmethod
	async def create_models():
		async with Engines.async_engine.begin() as conn:
			await conn.run_sync(Base.metadata.create_all)
