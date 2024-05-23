from aiogram.types import Message

from src.database.api.config.api_config import app
from src.database.sql.config.db_config import Settings
from src.database.sql.models.user_models import Users

from src.logs.my_logger import MyLogger


sync_session_factory = Settings.sync_session_factory
ice = MyLogger.ice
# logger = MyLogger.log_debug


class UsersCRUD:
    @staticmethod
    @app.get("/users")
    def get_users(tg_id: int) -> Users | None:
        with sync_session_factory as sess:
            try:
                kurwa_bobre: Users | None = sess.query(Users).filter(Users.tg_id == tg_id).one()
                return kurwa_bobre
            except Exception as err:
                ice(err)
                return None


@app.post("/users")
def create_user(msg: Message, total_cost: int = 0) -> None:
    with sync_session_factory as sess:
        try:
            new_user = Users(tg_id=msg.from_user.id,
                             username=msg.from_user.username,
                             status="active",
                             first_name=msg.from_user.first_name,
                             last_name=msg.from_user.last_name,
                             total_cost=total_cost)  # Тут должен быть ещё update total_cost
            sess.add(new_user)
            sess.commit()
        except Exception as err:
            logger(err)
        sess.commit()


