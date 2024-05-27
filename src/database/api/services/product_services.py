from src.database.api.schemas.product_schemas import PydCreateProduct
from src.database.api.utils.repository import AbstractRepository  # noqa
from src.database.api.utils.unitofwork import IUnitOfWork


class ProductsService:
    async def add_product(self, uow: IUnitOfWork, product: PydCreateProduct):
        products_dict = product.model_dump()
        async with uow:
            product_id = await uow.products.add_one(products_dict)
            await uow.commit()
            return product_id

    async def get_products(self, uow: IUnitOfWork):
        async with uow:
            products = await uow.products.find_all()
            return products

    async def get_product(self, uow: IUnitOfWork, product_id: int):
        async with uow:
            product = await uow.products.find_one(id=product_id)
            return product

    async def get_several_products(self, uow: IUnitOfWork, filter_by: dict):
        async with uow:
            products = await uow.products.find_several(filter_by)
            return products

    async def edit_product(self, uow: IUnitOfWork, product_id: int, product: PydCreateProduct):
        products_dict = product.model_dump()
        async with uow:
            await uow.products.edit_one(product_id, products_dict)

            # curr_product = await uow.products.find_one(id=product_id)
            # product_history_log = productHistorySchemaAdd(
            #     product_id=product_id,
            #     previous_assignee_id=curr_product.assignee_id,
            #     new_assignee_id=product.assignee_id
            # )
            # product_history_log = product_history_log.model_dump()
            # await uow.product_history.add_one(product_history_log)
            await uow.commit()

    # async def get_product_history(self, uow: IUnitOfWork):
    #     async with uow:
    #         history = await uow.product_history.find_all()
    #         return history
