from sqlalchemy import BigInteger, ForeignKey, MetaData, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

from base_model import Base


class Users(Base):
    __tablename__ = "users"
    tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None]
    status: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]


class Clients(Users):
    __tablename__ = "clients"

# 	products: Mapped[list["Products"]] = relationship(back_populates="users", secondary="user_products")
# 	orders: Mapped[list["Orders"]] = relationship(back_populates="user_orders", secondary="user_orders")
# 	admins: Mapped[list["Admins"]] = relationship(back_populates="user_admin", secondary="admins")
#
#
# class Employee(Users):
# 	__tablename__ = "employees"
# 	name: Mapped[str]
# 	role: Mapped[bool] = mapped_column(default=False)
# 	phone: Mapped[int]
# 	email: Mapped[str] = mapped_column(unique=True)
