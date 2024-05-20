# from sqlalchemy import BigInteger, ForeignKey, MetaData, UniqueConstraint
# from sqlalchemy.orm import Mapped, relationship, mapped_column
#
# from base_model import Base
#
#
# metadata_obj = MetaData()
#
#
# class Clients(Base):
# 	__tablename__ = "users"
#
# 	tg_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
# 	username: Mapped[str | None]
# 	first_name: Mapped[str | None]
# 	last_name: Mapped[str | None]
# 	status: Mapped[str | None]
# 	products: Mapped[list["Products"]] = relationship(back_populates="users", secondary="user_products")
# 	orders: Mapped[list["Orders"]] = relationship(back_populates="user_orders", secondary="user_orders")
# 	admins: Mapped[list["Employees"]] = relationship(back_populates="user_admin", secondary="admins")
#
#
# class Employees(Base):
# 	__tablename__ = "employees"
# 	name: Mapped[str]
# 	role: Mapped[bool] = mapped_column(default=False)
# 	email: Mapped[str] = mapped_column(unique=True)
#
#
# class Products(Base):
# 	# __table_args__ = {"extend_existing": True}  # не помню для чего это, вроде бы указание, что уже существует
# 	__tablename__ = "products"
# 	name: Mapped[str] = mapped_column(unique=True)
# 	short_description: Mapped[str]
# 	users: Mapped[list["Clients"]] = relationship(back_populates="products", secondary="user_products")
# 	stages: Mapped[list["Stages"]] = relationship(back_populates="products", secondary="stages")
# 	orders: Mapped[list["Orders"]] = relationship(back_populates="products")
# 	videos: Mapped[list["Videos"]] = relationship(back_populates="products", secondary="product_videos")
#
#
# class UserProducts(Base):
# 	__tablename__ = "user_products"
# 	user_id: Mapped[BigInteger] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
# 	product_name: Mapped[str] = mapped_column(ForeignKey("products.name", ondelete="RESTRICT"))
# 	stage: Mapped[list["Stages"]] = relationship(back_populates="user_products")
# 	UniqueConstraint("user_id", name="idx_user_products")
#
#
# class MyPoll(Base):
# 	__tablename__ = "my_poll"
# 	name: Mapped[str] = mapped_column(unique=True)
# 	questions: Mapped[list["MyPollQuestions"]] = relationship(back_populates="my_poll", secondary="my_poll_questions")
# 	answers: Mapped[list["MyPollAnswers"]] = relationship(back_populates="my_poll")
#
#
# class MyPollQuestions(Base):
# 	__tablename__ = "my_poll_questions"
# 	name: Mapped[str] = mapped_column(unique=True)
# 	poll_id: Mapped[int] = mapped_column(ForeignKey(column="my_poll.id"))
#
#
# class MyPollAnswers(Base):
# 	__tablename__ = "my_poll_answers"
# 	name: Mapped[str] = mapped_column(unique=True)
# 	poll_id: Mapped[int] = mapped_column(ForeignKey(column="my_poll.id"))
#
# class MyPollResults(Base):
# 	__tablename__ = "my_poll_results"
# 	user_id: Mapped[BigInteger] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
# 	poll_id: Mapped[int] = mapped_column(ForeignKey("poll.id", ondelete="RESTRICT"))
# 	results: Mapped[str]
#
#
#
# class Stages(Base):
# 	__tablename__ = "stages"
# 	name: Mapped[str]
# 	product_id: Mapped[int] = mapped_column(ForeignKey(column="products.id"))
#
#
# class Otzs(Base):
# 	__tablename__ = "otzs"
# 	text: Mapped[str]
# 	_from_: Mapped[str]
#
#
# class Orders(Base):
# 	__tablename__ = "orders"
# 	user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
# 	summ: Mapped[int]
# 	products: Mapped[str] = mapped_column(ForeignKey(column="products.id", ondelete="RESTRICT"))
# 	"""
# 	вроде бы так должно быть
# 	или может быть где-то должно быть relationship на users
# 	"""
#
#
# class UserOrders(Base):
# 	__tablename__ = "user_orders"
# 	user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
# 	orders_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="RESTRICT"))
#
#
# class Donations(Base):
# 	__tablename__ = "donations"
# 	_from_: Mapped[str]
# 	summ: Mapped[int]
# 	text: Mapped[str]
#
#
# class Videos(Base):
# 	__tablename__ = "videos"
# 	name: Mapped[str]
# 	product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="RESTRICT"))
#
#
# class ProductVideos(Base):
# 	__tablename__ = "product_videos"
# 	videos_id: Mapped[int] = mapped_column(ForeignKey("videos.id", ondelete="RESTRICT"))
# 	product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="RESTRICT"))
