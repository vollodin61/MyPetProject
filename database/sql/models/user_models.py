import enum

from sqlalchemy import BigInteger, ForeignKey, MetaData, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

from database.sql.models.base_model import Base


class Users(Base):
    __tablename__ = "users"
    tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None]
    status: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    total_cost: Mapped[float | None]
    products: Mapped[list["Products"]] = relationship(back_populates="user", secondary="users_products")
    orders: Mapped[list["Orders"]] = relationship(back_populates="user", secondary="users_orders")
#  Также надо найти, где я видел include_colum (вроде бы), попробовать с этой фигней
#  Вроде бы через polymorphic можно сделать и должны будут отображаться колонки.


class UsersProducts(Base):
    __tablename__ = "users_products"
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    product: Mapped[str | None] = mapped_column(ForeignKey("products.name", ondelete="CASCADE"))
    UniqueConstraint("user_id", name="idx_users_products")


class UserOrders(Base):
    __tablename__ = "users_orders"
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    order: Mapped[int | None] = mapped_column(ForeignKey("orders.id"))
    UniqueConstraint("user_id", name="idx_users_orders")


class Roles(enum.Enum):
    god = "god"
    admin = "admin"
    manager = "manager"
    moderator = "moderator"
    promoter = "promoter"
    family = "family"
    untouchable = "untouchable"


class Workers(Base):
    __tablename__ = "workers"
    tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None]
    status: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    role: Mapped[Roles | None]
    phone: Mapped[str | None]
    email: Mapped[str | None]
    salary: Mapped[str | None]
