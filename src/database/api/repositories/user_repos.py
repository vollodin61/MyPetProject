from src.database.sql.models.user_models import Users
from src.database.api.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = Users
