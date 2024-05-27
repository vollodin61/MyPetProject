# import enum
# from sqlalchemy import ForeignKey, UniqueConstraint
# from sqlalchemy.orm import Mapped, mapped_column
#
# from src.database.sql.models.base_model import Base
#
#
# class OrderStatus(enum.Enum):
#     done = "done"
#     not_done = "not_done"
#
#
# class Orders(Base):
#     __tablename__ = "orders"
#     status: Mapped[OrderStatus]
#     product: Mapped[str | None] = mapped_column(ForeignKey("products.name"))
#     price: Mapped[float | None]
#     count: Mapped[int]
#     amount: Mapped[float | None]
#     # total: Mapped[float]  # ????
#     user_id: Mapped[str | None] = mapped_column(ForeignKey("users.id"))  # TODO Непонятно будет ли проблема
#                                                                         # , с новыми пользователями.
#                                                                         # Их нужно как-то добавлять раньше,
#                                                                         # чем создавать ордер
#     __mapper_args__ = {
#         "polymorphic_identity": "orders",
#         "polymorphic_on": "status",
#     }
#
#
# class OrdersProducts(Base):
#     __tablename__ = "orders_products"
#     order_id: Mapped[int | None] = mapped_column(ForeignKey("orders.id", ondelete="RESTRICT"))
#     product: Mapped[str | None] = mapped_column(ForeignKey("products.name", ondelete="RESTRICT"))
#     price: Mapped[float | None] = mapped_column(ForeignKey("products.price", ondelete="RESTRICT"))
#     UniqueConstraint("order_id", name="idx_orders_products")
#
