# from fastapi import APIRouter, Depends
# from loguru import logger
# from sqlalchemy import update, select, text
#
# from src.database.api.schemas.user_schemas import PydCreateUser, PydDeleteUser, PydSomeDict
# from src.database.sql.config.db_config import Settings, get_async_session  # поменять везде на асинхронные, тк я делаю транзакцию общей
# from src.database.sql.models.user_models import Users
# from src.logs.my_ice import ice
#
# user_router = APIRouter(
#     prefix='/users',
#     tags=['Users']
# )
#
#
# def session_local():
#     with Settings.sync_session_factory() as session:
#         yield session
#
#
# @user_router.get("/{user_id}")
# async def get_user_by_tg_id(tg_id: int, sess=Depends(session_local)):
#     try:
#         kurwa_bobre: Users | None = sess.query(Users).filter(Users.tg_id == tg_id).one()
#         return {
#             "status": "ok",
#             "data": kurwa_bobre.__repr__(),
#             "details": None
#         }
#     except Exception as err:
#         ice(err)
#         logger.exception(err)
#         return {
#             "status": "Error",
#             "data": None,
#             "details": err.__repr__()
#         }
#     finally:
#         sess.commit()
#
#
# @user_router.post("/from_tilda")
# async def from_tilda(some_dict: PydSomeDict, sess=Depends(session_local)):
#     try:
#         dct = dict(some_dict)
#         print(f"{dct.get("some_dict").get("Ссылка_на_Телеграм") = }")
#         # data = (**some_dict.dict())
#         return {
#             "status": "ok",
#             "data": some_dict,
#             "details": "users successfully created!)!)"
#         }
#     except Exception as err:
#         ice(err)
#         return {
#             "status": "Error",
#             "data": None,
#             "details": err.__repr__()
#         }
#     finally:
#         sess.commit()
#
#
# @user_router.get("/")
# async def get_users_by_statuses(status: str, sess=Depends(session_local)):
#     try:
#         result = sess.query(Users).filter(Users.status == status).all()
#         ice(result)
#         return {
#             "status": "ok",
#             "data": result,
#             "details": None
#         }
#     except Exception as err:
#         ice(err)
#         logger.exception(err)
#         return {
#             "status": "Error",
#             "data": None,
#             "details": err.__repr__()
#         }
#     finally:
#         sess.commit()
#
#
# @user_router.post("/")
# async def create_user(user: PydCreateUser, sess=Depends(session_local)):
#     try:
#         new_user = Users(**user.dict(exclude_unset=True))
#         sess.add(new_user)
#         sess.commit()
#         return {
#             "status": "ok",
#             "data": None,
#             "details": "users successfully created!)!)"
#         }
#     except Exception as err:
#         ice(err)
#         return {
#             "status": "Error",
#             "data": None,
#             "details": err.__repr__()
#         }
#     finally:
#         sess.commit()
#
#
# @user_router.patch("{/user_id}")
# async def update_user(user: PydCreateUser, sess=Depends(session_local)):
#     try:
#         if user.total_spent:
#             ice(user.total_spent)
#             kurwa_bobre: Users | None = sess.query(Users).filter(Users.tg_id == user.tg_id).one()
#             user.total_spent += kurwa_bobre.total_spent
#             logger.info(f"{user.total_spent = }")
#         query = update(Users).where(Users.tg_id == user.tg_id).values(**user.dict(exclude_unset=True))
#         result = sess.execute(query)
#         return {
#             "status": "ok",
#             "data": result,
#             "details": "users successfully updated!)!)"
#         }
#     except Exception as err:
#         logger.exception(err)
#         return {
#             "status": "Error",
#             "data": None,
#             "details": err.__repr__()
#         }
#     finally:
#         sess.commit()
#
#
# @user_router.delete("/{user_id}")
# async def delete_user(user: PydDeleteUser, sess=Depends(session_local)):
#     dct = user.dict
#     ice(dct)
#     try:
#         query = update(Users).where(Users.tg_id == user.tg_id).values(status="DELETED").returning(Users.status)
#         result = sess.execute(query)
#         deleted_user_tg_id = f"user.status with tg_id: {user.tg_id} = {result.fetchone()[0]}"
#         return {
#             "status": "ok",
#             "data": f"{deleted_user_tg_id = }",
#             "details": "users successfully deleted!)!)"
#         }
#     except Exception as err:
#         logger.exception(err)
#         return {
#             "status": "Error",
#             "data": None,
#             "details": err.__repr__()
#         }
#     finally:
#         sess.commit()
#
