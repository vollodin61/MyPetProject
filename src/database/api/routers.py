from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy import update, delete

from src.database.api.schemas.user_schemas import PydUser, PydCreateUser, PydDeleteUser
from src.database.sql.config.db_config import Engines
from src.database.sql.models.user_models import Users
from src.logs.my_ice import ice

user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)

fake_users = [
    {"id": 232, "role": "232_motherfucker"},
    {"id": 11, "role": ["11_motherfucker"]},
    {"id": 12, "role": "12_motherfucker", "name": [{"id": 1, "name": "LOH", "type": "first_name"}]},
]


# @user_router.get("/{user_id}", response_model=List[PydUser])
# async def get_user(user_id: int):
#     return [user for user in fake_users if user.get("id") == user_id]

def session_local():
    with Engines.sync_session_factory() as session:
        yield session


@user_router.get("/{user_id}")
async def get_user_by_name(tg_id: int, sess=Depends(session_local)):
    try:
        kurwa_bobre: Users | None = sess.query(Users).filter(Users.tg_id == tg_id).one()
        return {
            "status": "ok",
            "data": kurwa_bobre.__repr__(),
            "details": None
        }
    except Exception as err:
        ice(err)
        logger.exception(err)
        return {
            "status": "Error",
            "data": None,
            "details": err.__repr__()
        }
    finally:
        sess.commit()


@user_router.post("/")
async def create_user(user: PydCreateUser, sess=Depends(session_local)):
    try:
        new_user = Users(**user.dict())
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
async def update_user(user: PydCreateUser, sess=Depends(session_local)):
    try:
        query = update(Users).where(Users.tg_id == user.tg_id).values(**user.dict())
        result = sess.execute(query)
        ice(result.__repr__())
        return {
            "status": "ok",
            "data": result,
            "details": "users successfully updated!)!)"
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


@user_router.delete("/{user_id}")
async def delete_user(user: PydDeleteUser, sess=Depends(session_local)):
    try:
        query = delete(Users).where(Users.tg_id == user.tg_id).returning(Users.tg_id)
        result = sess.execute(query)
        deleted_user_tg_id = result.fetchone()[0]
        return {
            "status": "ok",
            "data": f"{deleted_user_tg_id = }",
            "details": "users successfully deleted!)!)"
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
