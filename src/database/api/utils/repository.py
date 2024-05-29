from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine.result import ChunkedIteratorResult
from src.logs.my_ice import ice


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        # try:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()
        # except:
        #     stmt = select(self.model).where(self.model.username == data["username"]).returning(self.model.id)
        #     res = await self.session.execute(stmt)
        #     return res.scalar_one()

    async def edit_one(self, id: int, data: dict) -> int:
        if data.get("total_spent") and data.get("total_spent") > 0:
            pre_stmt = select(self.model).filter_by(id=id)
            res = await self.session.execute(pre_stmt)
            r = res.scalar_one().total_spent
            ice(r)
            data["total_spent"] += r
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        # ice(res.scalar_one())
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one_by_id(self, **filter_by):
        try:
            stmt = select(self.model).filter_by(**filter_by)
            res = await self.session.execute(stmt)
            res = res.scalar_one().to_read_model()
            return res
        except Exception as err:
            return err.__repr__()

    async def find_one_by_any(self, filter_by):
        try:
            stmt = select(self.model).filter_by(**filter_by)
            res = await self.session.execute(stmt)
            res = res.scalar_one().to_read_model().id
            # res = [row[0].to_read_model() for row in res.all()][0]
            return res
        except Exception as err:
            return err.__repr__()

    async def find_several(self, filter_by):
        # ice(filter_by)
        stmt = select(self.model).filter_by(**filter_by)
        # ice(stmt.__str__())
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        # ice(res)
        return res

    async def add_user_product(self, products: list):
        products_names = []
        for product in products:
            stmt = insert(self.model).values(user_id=1, product=product.get("name")).returning(self.model.product)
            res = await self.session.execute(stmt)
            products_names.append(res.scalar_one())
        return products_names

    async def add_user_order(self):
        pass
