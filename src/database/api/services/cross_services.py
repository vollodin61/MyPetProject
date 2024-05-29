from src.database.api.schemas.cross_schemas import PydUserProducts
from src.database.api.utils.repository import AbstractRepository  # noqa
from src.database.api.utils.unitofwork import IUnitOfWork


class UserProductsService:
    async def add_user_products(self, uow: IUnitOfWork, user_products: PydUserProducts):
        user_products_dict = user_products.model_dump()
        async with uow:
            user_products_id = await uow.user_products.add_one(user_products_dict)
            await uow.commit()
            return user_products_id
