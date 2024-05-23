from enum import Enum
from pydantic import BaseModel


class Statuses(Enum):
    active = "active"
    not_active = "not_active"
    banned = "BANNED"
    deleted = "DELETED"
    support = "support"
    admin = "admin"
    employer = "employer"
    godlike = "godlike"
    # god = "god"


class PydCreateUser(BaseModel):
    tg_id: int
    username: str = ""
    status: str = ""
    first_name: str = ""
    last_name: str = ""
    total_spent: int | None
    phone: str = ""
    description: str = ""

    class Config:
        from_attributes = True


class PydDeleteUser(BaseModel):
    tg_id: int


class PydSomeDict(BaseModel):
    some_dict: dict
