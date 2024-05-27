from src.database.api.schemas.user_schemas import PydCreateUser, \
    PydDeleteUser  # TaskHistorySchemaAdd, TaskSchemaAdd, TaskSchemaEdit
from src.database.api.utils.repository import AbstractRepository
from src.database.api.utils.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: PydCreateUser):
        users_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(users_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    async def get_user(self, uow: IUnitOfWork, user_id: int):
        async with uow:
            user = await uow.users.find_one(id=user_id)
            return user

    async def get_several_users(self, uow: IUnitOfWork, filter_by: dict):
        async with uow:
            users = await uow.users.find_several(filter_by)
            return users

    async def edit_user(self, uow: IUnitOfWork, user_id: int, user: PydCreateUser):
        users_dict = user.model_dump()
        async with uow:
            await uow.users.edit_one(user_id, users_dict)

            # curr_user = await uow.users.find_one(id=user_id)
            # user_history_log = UserHistorySchemaAdd(
            #     user_id=user_id,
            #     previous_assignee_id=curr_user.assignee_id,
            #     new_assignee_id=user.assignee_id
            # )
            # user_history_log = user_history_log.model_dump()
            # await uow.user_history.add_one(user_history_log)
            await uow.commit()

    # async def get_user_history(self, uow: IUnitOfWork):
    #     async with uow:
    #         history = await uow.user_history.find_all()
    #         return history
