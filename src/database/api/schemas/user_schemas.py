from enum import Enum
from pydantic import BaseModel


class PydStatuses(BaseModel):
    active: str | None = "active"
    not_active: str | None = "not_active"
    banned: str | None = "banned"
    deleted: str | None = "deleted"
    support: str | None = "support"
    admin: str | None = "admin"
    employer: str | None = "employer"
    godlike: str | None = "godlike"
    god: str | None = "god"


class PydCreateUser(BaseModel):
    id: int = None
    tg_id: int | None = None
    username: str = None
    status: str = None
    first_name: str = None
    last_name: str = None
    total_spent: int = 0
    phone: str = None
    email: str = None
    description: str = None

    class Config:
        from_attributes = True
