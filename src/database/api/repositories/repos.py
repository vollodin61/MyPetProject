# from src.database.sql.models.cross_user_models import UsersProductsModel
from src.database.sql.models.cross_user_models import UsersProductsModel
from src.database.sql.models.product_models import ProductsModel
from src.database.sql.models.user_models import UsersModel
from src.database.api.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = UsersModel


class ProductsRepository(SQLAlchemyRepository):
    model = ProductsModel


class UserProductsRepository(SQLAlchemyRepository):
    model = UsersProductsModel
