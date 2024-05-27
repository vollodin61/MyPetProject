import enum
from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.api.schemas.user_schemas import PydCreateUser
from src.database.sql.models.base_model import Base


class Users(Base):
    """
    Documentation
    :param: tg_id
    :type: BigInteger, unique
    """

    __tablename__ = "users"
    tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None]
    status: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    total_spent: Mapped[int | None]
    phone: Mapped[str | None]
    products: Mapped[list["Products"]] = relationship(back_populates="user", secondary="users_products")
    orders: Mapped[list["Orders"]] = relationship(back_populates="user", secondary="users_orders")

    def to_read_model(self) -> PydCreateUser:
        return PydCreateUser(
            tg_id=self.tg_id,
            username=self.username,
            status=self.status,
            first_name=self.first_name,
            last_name=self.last_name,
            total_spent=self.total_spent,
            phone=self.phone,
        )


class UsersProducts(Base):
    __tablename__ = "users_products"
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    product: Mapped[str | None] = mapped_column(ForeignKey("products.name", ondelete="RESTRICT"))
    UniqueConstraint("user_id", name="idx_users_products")


class UserOrders(Base):
    __tablename__ = "users_orders"
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    order: Mapped[int | None] = mapped_column(ForeignKey("orders.id", ondelete="RESTRICT"))
    UniqueConstraint("user_id", name="idx_users_orders")


class UserOrdersProducts(Base):
    __tablename__ = "users_orders_products"
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    order: Mapped[int | None] = mapped_column(ForeignKey("orders.id", ondelete="RESTRICT"))
    product: Mapped[str | None] = mapped_column(ForeignKey("products.name", ondelete="RESTRICT"))
    price: Mapped[float | None] = mapped_column(ForeignKey("products.price", ondelete="RESTRICT"))
    UniqueConstraint("user_id", name="idx_users_orders_products")


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
