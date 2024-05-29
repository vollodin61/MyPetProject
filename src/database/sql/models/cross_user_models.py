from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.database.api.schemas.cross_schemas import PydUserProducts
from src.database.sql.models.base_model import Base


class UsersProductsModel(Base):
    __tablename__ = "users_products"
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    product: Mapped[str | None] = mapped_column(ForeignKey("products.name", ondelete="RESTRICT"))
    UniqueConstraint("user_id", name="idx_users_products")

    def to_read_model(self) -> PydUserProducts:
        return PydUserProducts(
            user_id=self.user_id,
            product=self.product
        )
