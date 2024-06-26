import re

from aiogram.types import Message
from typing import List

from src.database.sql.config.db_config import Settings
from src.database.sql.models.user_models import UsersModel
# from database.sql.models.product_models import Products
from src.database.sql.models.base_model import Base
from src.logs.my_logger import MyLogger as Ml

ice = Ml.ice
# logger = Ml.log_debug
sync_session_factory = Settings.sync_session_factory


def sync_get_user_by_tg_id(tg_id: int):  # -> Users | None
    with sync_session_factory() as sess:
        try:
            kurwa_bobre: UsersModel | None = sess.query(UsersModel).filter(UsersModel.tg_id == tg_id).one()
            return ice(kurwa_bobre)
        except Exception as err:
            ice(err)
            return None


class SyncORM:
    @staticmethod
    def create_models():
        Base.metadata.create_all(Settings.sync_engine)

    @staticmethod
    def drop_models():
        Base.metadata.drop_all(Settings.sync_engine)

    class UsersCRUD:
        @staticmethod
        def re_msg_text_to_list(msg_text: str) -> List:
            return re.findall(pattern=r"(?<=: ).+", string=msg_text)

        @staticmethod
        def get_user_by_tg_id(tg_id: int) -> UsersModel | None:
            with sync_session_factory() as sess:
                try:
                    kurwa_bobre: UsersModel | None = sess.query(UsersModel).filter(UsersModel.tg_id == tg_id).one()
                    return kurwa_bobre
                except Exception as err:
                    ice(err)
                return None

        @staticmethod
        def get_user_by_username(username: str) -> UsersModel | None:
            with sync_session_factory() as sess:
                try:
                    kurwa_bobre: UsersModel | None = sess.query(UsersModel).filter(UsersModel.username == username).one()
                    return kurwa_bobre
                except Exception as err:
                    ice(err)
                return None

        @staticmethod
        def insert_user(msg: Message | None = None, total_cost: int = 0):
            with sync_session_factory() as sess:
                try:
                    new_user = UsersModel(tg_id=msg.from_user.id,
                                          username=msg.from_user.username,
                                          status="active",
                                          first_name=msg.from_user.first_name,
                                          last_name=msg.from_user.last_name, )  # Тут должен быть ещё update total_cost
                    sess.add(new_user)
                    sess.commit()
                except Exception as err:
                    ice(err)
                sess.commit()

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
