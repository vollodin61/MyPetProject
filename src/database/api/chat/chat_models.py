from sqlalchemy import Column, Integer, String

from src.database.sql.models.base_model import Base


class Messages(Base):
    __tablename__ = "messages"

    message = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
