import logging

from icecream import ic
from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy import update

from src.database.api.config.dependencies import UOWDep
from src.database.api.schemas.user_schemas import PydCreateUser, PydSomeDict
from src.database.api.services.tilda_parser import tilda_parser
from src.database.sql.config.db_config import get_async_session  # поменять везде на асинхронные,
# тк я делаю транзакцию общей
from src.database.sql.models.user_models import Users
from src.database.api.services.user_services import UsersService

from src.logs.my_ice import ice

logging.basicConfig(level=logging.DEBUG)
user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@user_router.get("/one/{user_id}")
async def get_user_by_id(uow: UOWDep, user_id: int):
    user = await UsersService().get_user(uow=uow, user_id=user_id)
    return user


@user_router.get("/get_several")
async def get_several_users(uow: UOWDep, tg_id: int = None, username: str = None,
                            status: str = None, total_spent: int = None, first_name: str = None,
                            last_name: str = None, phone: str = None, description: str = None):
    pre_dict = dict(tg_id=tg_id, username=username,
                    status=status, total_spent=total_spent, first_name=first_name,
                    last_name=last_name, phone=phone, description=description)
    dct = {key: value for key, value in pre_dict.items() if value}

    user = await UsersService().get_several_users(uow=uow, filter_by=dct)
    return user


@user_router.get("/get_all")
async def get_users(uow: UOWDep):
    users = await UsersService().get_users(uow)
    return users


@user_router.post("/from_tilda22")
async def post_from_tilda(uow: UOWDep, tilda_dict: dict):
    user, product, order = tilda_parser(some_dict=tilda_dict)  # распарсить входящий json?
    await UsersService().add_user(uow=uow, user=user)
    # обработать отправить создание пользователя в бд
    # отправить человеку ссылку на бот из Ириного юзер-бота
    # new_dict = dict(some_dict)
    # ice(some_dict.dict())
    ic(tilda_dict)
    # ice(new_dict)

    return tilda_dict


@user_router.post("/from_tilda")
async def from_tilda(some_dict: PydSomeDict, sess=Depends(get_async_session)):
    try:
        dct = dict(some_dict)
        ice(f"{dct.get("some_dict").get("Ссылка_на_Телеграм") = }")
        data = (some_dict.dict())
        ice(data)
        return {
            "status": "ok",
            "data": some_dict,
            "details": "users successfully created!)!)"
        }
    except Exception as err:
        ice(err)
        return {
            "status": "Error",
            "data": None,
            "details": err.__repr__()
        }
    finally:
        sess.commit()


@user_router.post("/")
async def create_user(user: PydCreateUser, sess=Depends(get_async_session)):
    try:
        new_user = Users(**user.dict(exclude_unset=True))
        sess.add(new_user)
        sess.commit()
        return {
            "status": "ok",
            "data": None,
            "details": "users successfully created!)!)"
        }
    except Exception as err:
        ice(err)
        return {
            "status": "Error",
            "data": None,
            "details": err.__repr__()
        }
    finally:
        sess.commit()


@user_router.patch("{/user_id}")
async def update_user(user: PydCreateUser, sess=Depends(get_async_session)):
    try:
        if user.total_spent:
            ice(user.total_spent)
            kurwa_bobre: Users | None = sess.query(Users).filter(Users.tg_id == user.tg_id).one()
            user.total_spent += kurwa_bobre.total_spent
            logger.info(f"{user.total_spent = }")
        query = update(Users).where(Users.tg_id == user.tg_id).values(**user.dict(exclude_unset=True))
        result = sess.execute(query)
        return {
            "status": "ok",
            "data": result,
            "details": "users successfully updated!)!)"
        }
    except Exception as err:
        logger.exception(err)
        return {
            "status": "Error",
            "data": None,
            "details": err.__repr__()
        }
    finally:
        sess.commit()
