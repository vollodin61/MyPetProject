from abc import ABC, abstractmethod
from typing import Type

from src.database.sql.config.db_config import Settings
from src.database.api.repositories.repos import UsersRepository, ProductsRepository, UserProductsRepository

async_session_factory = Settings.async_session_factory


class IUnitOfWork(ABC):
    users: Type[UsersRepository]
    products: Type[ProductsRepository]
    user_products: Type[UserProductsRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...

    @abstractmethod
    async def flush(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.products = ProductsRepository(self.session)
        self.user_products = UserProductsRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def flush(self):
        await self.session.flush()