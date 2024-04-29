from datetime import datetime
from sqlalchemy import func, MetaData, BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# from database.sql.config.engines import Engines


metadata_obj = MetaData()


class Base(AsyncAttrs, DeclarativeBase):
	id: Mapped[int] = mapped_column(primary_key=True)
	description: Mapped[str | None]
	created_at: Mapped[datetime] = mapped_column(server_default=func.now())
	updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())

	repr_cols_num = 4	  # количество колонок в выводе в принт
	repr_cols = tuple()  # Всё это можно переопределить для подчинённого класса

	def __repr__(self):  # Модифицируем вывод в принт, когда запросы делаем
		"""relationship() не используются в repr. тк могут привести к неожиданным подгрузкам"""
		cols = [f"{col}={getattr(self, col)}" for idx, col in enumerate(self.__table__.columns.keys()) if
				col in self.repr_cols or idx < self.repr_cols_num]

		return f"<{self.__class__.__name__} | {', '.join(cols)} >"


class Products(Base):
	__tablename__ = "products"
	name: Mapped[str| None] = mapped_column(unique=True)
	short_description: Mapped[str | None]


# Base.metadata.create_all(Engines.sync_engine)
# Base.metadata.drop_all(Engines.sync_engine)

# TODO Добавить сюда базовую модель	 "Users", которая будет наследоваться от Base
#  и будет родителем для моделей Clients и Employees
