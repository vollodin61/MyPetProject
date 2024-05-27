from enum import Enum
from pydantic import BaseModel


class PydStatuses(BaseModel):
    active: str | None = "active"
    not_active: str | None = "not_active"
    banned: str | None = "BANNED"
    deleted: str | None = "DELETED"
    support: str | None = "support"
    admin: str | None = "admin"
    employer: str | None = "employer"
    godlike: str | None = "godlike"
    god: str | None = "god"


class PydCreateUser(BaseModel):
    tg_id: int = None
    username: str = None
    status: str = None
    first_name: str = None
    last_name: str = None
    total_spent: int | None
    phone: str = None
    email: str = None
    description: str = None

    class Config:
        from_attributes = True


class PydDeleteUser(BaseModel):
    tg_id: int = None


class PydSomeDict(BaseModel):
    pass
