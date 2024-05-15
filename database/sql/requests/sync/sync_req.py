import re

from aiogram.types import Message
from typing import List
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from database.sql.config.db_config import settings, Engines
from database.sql.models.user_models import Users
from database.sql.models.product_models import Products
from database.sql.models.base_model import Base
from logs.my_logger import MyLogger as Ml

ice = Ml.ice
logger = Ml.log_debug
sync_session_factory = Engines.sync_session_factory


class SyncORM:
    @staticmethod
    def create_models():
        Base.metadata.create_all(Engines.sync_engine)

    @staticmethod
    def drop_models():
        Base.metadata.drop_all(Engines.sync_engine)

    class UsersCRUD:
        @staticmethod
        def re_msg_text_to_list(msg_text: str) -> List:
            return re.findall(pattern=r"(?<=: ).+", string=msg_text)

        @staticmethod
        def get_user_by_tg_id(tg_id: int) -> Users | None:
            with sync_session_factory() as sess:
                try:
                    kurwa_bobre: Users | None = sess.query(Users).filter(Users.tg_id == tg_id).one()
                    return kurwa_bobre
                except Exception as err:
                    print(f'{"!" * 88}\nОШИПКА!\n{err}\n{"!" * 88}')
                return None

        @staticmethod
        def get_user_by_username(username: str) -> Users | None:
            ...

        @staticmethod
        def insert_user(tg_id: int, msg: Message | None = None):
            ...

        @staticmethod
        def insert_user_from_poll(tg_id: int, msg: Message | None = None):
            ...

        @staticmethod
        def update_user(tg_id: int, msg: Message | None = None):
            ...

        @staticmethod
        def delete_user(tg_id: int, msg: Message | None = None):
            ...

        @staticmethod
        def insert_user_product(tg_id: int, msg: Message | None = None):
            ...

        @staticmethod
        def insert_user_poll(tg_id: int, msg: Message | None = None):
            ...

        # @staticmethod
        # def get_user_by_(table_name, column_name, value) -> Users | None:
        #     with sync_session_factory() as sess:
        #         try:
        #             kurwa_bobre: Users | None = sess.query(table_name=table_name).filter(
        #                 table_name.column_name == value).one()
        #             kurwa_bobre: Users | None = sess.query("Users").filter()
        #             return kurwa_bobre
        #         except Exception as err:
        #             print(f'{"!" * 88}\nОШИПКА!\n{err}\n{"!" * 88}')
        #         return None
        # #
        # # @staticmethod
        # # def get_user_by_(**kwargs: int | str) -> Users | None:
        #     k_list = list(kwargs.keys())
        #     k_vals = kwargs.values()
        #     with sync_session_factory() as sess:
        #         try:
        #             kurwa_bobre: Users | None = sess.query(Users).filter(
        #                 Users.__getattribute__(k_list[0]) == k_vals[0]).one()
        #             return kurwa_bobre
        #         except Exception as err:
        #             ice(err)
        #         return None

    class UsersCRUD:
        ...

    class ProductsCRUD:
        ...

    class OrdersCRUD:
        ...

    class WorkersCRUD:
        ...

    class LessonsCRUD:
        ...

    class VideosCRUD:
        ...

    class HomeworksCRUD:
        ...

    class MaterialsCRUD:
        ...

    class PollsCRUD:
        ...

    class QuestionsCRUD:
        ...

    class AnswersCRUD:
        ...

    class ResultsCRUD:
        ...

    class OtzDonationsCRUD:
        ...

# SyncORM.drop_models()
# SyncORM.create_models()
