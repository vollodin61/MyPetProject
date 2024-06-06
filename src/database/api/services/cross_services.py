from src.database.api.schemas.cross_schemas import PydUserProducts
from src.database.api.schemas.user_schemas import PydCreateUser
from src.database.api.utils.repository import AbstractRepository  # noqa
from src.database.api.utils.unitofwork import IUnitOfWork


class UserProductsService:
    async def add_user_products(self, uow: IUnitOfWork, user_products: dict, user_id: int):
        async with uow:
            user_products_id = await uow.user_products.add_user_product(user_products, user_id)
            await uow.commit()
            return user_products_id
