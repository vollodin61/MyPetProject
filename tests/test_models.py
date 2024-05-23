from datetime import datetime
from sqlalchemy import func, FetchedValue, BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    __tablename_ = "base"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(server_onupdate=FetchedValue(), nullable=True)

    repr_cols_num = 4  # количество колонок в выводе в принт
    repr_cols = tuple()  # Всё это можно переопределить для подчинённого класса

    def __repr__(self):  # Модифицируем вывод в принт, когда запросы делаем
        """Relationship() не используются в repr. тк могут привести к неожиданным подгрузкам"""
        cols = [f"{col}={getattr(self, col)}" for idx, col in enumerate(self.__table__.columns.keys()) if
                col in self.repr_cols or idx < self.repr_cols_num]

        return f"<{self.__class__.__name__} | {', '.join(cols)} >"


class Users(Base):
    __tablename__ = "users"
    tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None]
    status: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    total_spent: Mapped[int | None]
    phone: Mapped[str | None]
