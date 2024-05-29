import logging

from icecream import ic
from fastapi import APIRouter
from loguru import logger
from src.database.api.config.dependencies import UOWDep
from src.database.api.schemas.user_schemas import PydCreateUser
from src.database.api.services.cross_services import UserProductsService
from src.database.api.services.tilda_parser import tilda_parser
from src.database.api.services.user_services import UsersService

from src.logs.my_ice import ice

logging.basicConfig(level=logging.DEBUG)
user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@user_router.get("/one/{user_id}")
async def get_user_by_id(uow: UOWDep, user_id: int):
    user = await UsersService().get_user_by_id(uow=uow, user_id=user_id)
    return user


@user_router.get("/get_several")
async def get_several_users(uow: UOWDep, tg_id: int = None, username: str = None,
                            status: str = None, total_spent: int = None, first_name: str = None,
                            last_name: str = None, phone: str = None, description: str = None):
    pre_dict = dict(tg_id=tg_id, username=username,
                    status=status, total_spent=total_spent, first_name=first_name,
                    last_name=last_name, phone=phone, description=description)
    dct = {key: value for key, value in pre_dict.items() if value}

    users = await UsersService().get_several_users(uow=uow, filter_by=dct)
    return users


@user_router.get("/get_all")
async def get_users(uow: UOWDep):
    users = await UsersService().get_users(uow)
    return users


@user_router.post("/create_user")
async def create_user(uow: UOWDep, user: PydCreateUser):
    user_id = await UsersService().add_user(uow=uow, user=user)
    return {"status": "ok", "user_id": user_id, "details": "users successfully created!)!)"}


@user_router.post("/from_tilda")
async def post_from_tilda(uow: UOWDep, tilda_dict: dict):
    user, order = tilda_parser(some_dict=tilda_dict)  # распарсить входящий json?
    # check_user = await UsersService().check_user(uow=uow, username=user.username)
    user_dict = {"username": user.username}
    try:
        user_id = await UsersService().add_user(uow=uow, user=user)
        add_products = await UserProductsService().add_user_products(uow, order)
    except:
        user_id = await UsersService().get_user_by_any(uow=uow, filter_by=user_dict)
        # add_products = await UsersService().add_user_products(uow, order)
    # user_id = await UsersService().from_tilda(uow=uow, tilda_dict=tilda_dict)
    return {"status": "ok", "user_id": user_id, "details": "users successfully created!)!)"}


@user_router.patch("/update_user_{id}")
async def update_user(uow: UOWDep, user: PydCreateUser, id: int):
    user_id = await UsersService().edit_user(uow=uow, user=user, user_id=id)
    return {"status": "ok", "user_id": user_id, "details": "users successfully created!)!)"}
