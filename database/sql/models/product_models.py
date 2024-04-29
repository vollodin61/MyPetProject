from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, MetaData, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

from base_model import Base, Product

