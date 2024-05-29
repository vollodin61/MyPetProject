from src.database.api.schemas.user_schemas import PydCreateUser
from src.database.api.utils.repository import AbstractRepository  # noqa
from src.database.api.utils.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: PydCreateUser):
        users_dict = user.model_dump(exclude_unset=True)
        async with uow:
            user_id = await uow.users.add_one(users_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    async def get_user_by_id(self, uow: IUnitOfWork, user_id: int):
        async with uow:
            user = await uow.users.find_one_by_id(id=user_id)
            return user

    async def get_user_by_any(self, uow: IUnitOfWork, filter_by: dict):
        async with uow:
            user = await uow.users.find_one_by_any(filter_by)
            return user

    async def get_several_users(self, uow: IUnitOfWork, filter_by: dict):
        async with uow:
            users = await uow.users.find_several(filter_by)
            return users

    async def edit_user(self, uow: IUnitOfWork, user: PydCreateUser, user_id: int):
        users_dict = user.model_dump(exclude_unset=True)
        async with uow:
            result = await uow.users.edit_one(user_id, users_dict)
            await uow.commit()
        return result

    # async def add_user_products(self, uow: IUnitOfWork, products: dict):
    #     product_names = [product.get("name") for product in products for _ in range(product.get("quantity"))]
    #     async with uow:

    # async def from_tilda(self, uow: IUnitOfWork, tilda_dict: dict):
    #     # user_id = None
    #     user, order = tilda_parser(some_dict=tilda_dict)  # распарсить входящий json?
    #     async with uow:
    #         check_user = await uow.users.find_one_by_id(username=user.username)
    #     if not check_user:
    #         users_dict = user.model_dump(exclude_unset=True)
    #         async with uow:
    #             user_id = await uow.users.add_one(users_dict)
    #             await uow.flush()
    #             # await uow.commit()
    #     async with uow:
    #         user_products = await uow.user_products.add_user_product(products=products)
    #     user_id = 1101011
    #     result = {
    #         "user_id": user_id,
    #         "products": user_products
    #     }
    #     await uow.commit()
    #     # обработать отправить создание пользователя в бд
    #     # отправить человеку ссылку на бот из Ириного юзер-бота
    #     # тут return должен мне отправлять оповещение, что пользователь добавлен. Или записывать куда-то это в лог
    #     return result
