import enum

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.database.sql.models.base_model import Base


class ProductTypes(enum.Enum):
    course = "course"
    webinar_series = "webinar_series"
    poll = "poll"
    otz = "otz"
    club = "club"


class Status(enum.Enum):
    active = "active"
    inactive = "inactive"


class Products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str | None] = mapped_column(unique=True)
    product_type: Mapped[ProductTypes | None] = mapped_column(default=ProductTypes.course, autoincrement=True)
    price: Mapped[float | None] = mapped_column(unique=True)
    status: Mapped[Status | None]
    users: Mapped[list["Users"]] = relationship(back_populates="products", secondary="users_products")  # yep
    orders: Mapped[list["Orders"]] = relationship(back_populates="products", secondary="orders_products")  # yep
    videos: Mapped[list["Videos"]] = relationship(back_populates="products", secondary="products_videos")  # yep
    lessons: Mapped[list["Lessons"]] = relationship(back_populates="products", secondary="products_lessons")  # yep

    __mapper_args__ = {
        "polymorphic_identity": "products",
        "polymorphic_on": "product_type",
    }


class Lessons(Base):
    __tablename__ = "lessons"
    name: Mapped[str | None] = mapped_column(unique=True)
    product: Mapped[int | None] = mapped_column(ForeignKey("products.id"))
    products: Mapped[list["Products"]] = relationship(back_populates="lessons", secondary="products_lessons")  # yep
    videos: Mapped[list["Videos"]] = relationship(back_populates="lessons", secondary="lessons_videos")  # yep
    material: Mapped[list["Materials"]] = relationship(back_populates="lessons", secondary="lessons_materials")  # yep
    homework: Mapped[list["Homeworks"]] = relationship(back_populates="lessons", secondary="lessons_homeworks")  # yep

    __mapper_args__ = {
        "polymorphic_identity": "lessons",
    }


class Videos(Base):
    __tablename__ = "videos"
    name: Mapped[str | None] = mapped_column(unique=True)
    product: Mapped[Products | None] = relationship(back_populates="videos", secondary="products_videos")  # yep
    lesson: Mapped[Lessons | None] = relationship(back_populates="videos", secondary="lessons_videos")  # yep
    homework: Mapped[str | None] = relationship(back_populates="videos", secondary="homeworks_videos")
    url: Mapped[str | None]

    __mapper_args__ = {
        "polymorphic_identity": "videos",
    }


class Materials(Base):
    __tablename__ = "materials"
    name: Mapped[str | None] = mapped_column(unique=True)
    lesson: Mapped[Lessons | None] = relationship(back_populates="materials", secondary="lessons_materials")  # yep
    data: Mapped[str | None]
    homework: Mapped["Homeworks" or None] = relationship(back_populates="materials", secondary="homeworks_materials")  # yep
    url: Mapped[str | None]

    __mapper_args__ = {
        "polymorphic_identity": "materials",
    }


class Homeworks(Base):
    __tablename__ = "homeworks"
    name: Mapped[str | None] = mapped_column(unique=True)
    lesson: Mapped[Lessons | None] = relationship(back_populates="homeworks", secondary="lessons_homeworks")  # yep
    data: Mapped[str | None]
    material: Mapped[list["Materials"]] = relationship(back_populates="homeworks", secondary="homeworks_materials")  # yep
    video: Mapped[list["Videos"]] = relationship(back_populates="homeworks", secondary="homeworks_videos")  # yep
    url: Mapped[str | None]


class ProductsVideos(Base):
    __tablename__ = "products_videos"
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    video: Mapped[str | None] = mapped_column(ForeignKey("videos.name", ondelete="CASCADE"))


class ProductsLessons(Base):
    __tablename__ = "products_lessons"
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    lesson: Mapped[str | None] = mapped_column(ForeignKey("lessons.name", ondelete="CASCADE"))
    UniqueConstraint("product_id", name="idx_products_lessons")


class LessonsVideos(Base):
    __tablename__ = "lessons_videos"
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id", ondelete="CASCADE"))
    video: Mapped[str | None] = mapped_column(ForeignKey("videos.name", ondelete="CASCADE"))
    UniqueConstraint("lesson_id", name="idx_lessons_videos")


class LessonsMaterials(Base):
    __tablename__ = "lessons_materials"
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id", ondelete="CASCADE"))
    material: Mapped[str | None] = mapped_column(ForeignKey("materials.name", ondelete="CASCADE"))
    UniqueConstraint("lesson_id", name="idx_lessons_materials")


class LessonsHomeworks(Base):
    __tablename__ = "lessons_homeworks"
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id", ondelete="CASCADE"))
    homework: Mapped[str | None] = mapped_column(ForeignKey("homeworks.name", ondelete="CASCADE"))
    UniqueConstraint("lesson_id", name="idx_lessons_homeworks")


class HomeworksMaterials(Base):
    __tablename__ = "homeworks_materials"
    homework_id: Mapped[int | None] = mapped_column(ForeignKey("homeworks.id", ondelete="CASCADE"))
    material: Mapped[str | None] = mapped_column(ForeignKey("materials.name", ondelete="CASCADE"))
    UniqueConstraint("homework_id", name="idx_homeworks_materials")


class HomeworksVideos(Base):
    __tablename__ = "homeworks_videos"
    homework_id: Mapped[int | None] = mapped_column(ForeignKey("homeworks.id", ondelete="CASCADE"))
    video: Mapped[str | None] = mapped_column(ForeignKey("videos.name", ondelete="CASCADE"))
    UniqueConstraint("homework_id", name="idx_homeworks_videos")