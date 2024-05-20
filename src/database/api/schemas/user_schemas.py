from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict

from pydantic import BaseModel


class ETypes(Enum):
    first = "first_name"
    last = "last_name"


class PydNames(BaseModel):
    id: int
    name: str
    type: ETypes


class PydUser(BaseModel):
    id: int
    role: str
    name: List[PydNames] = []


class PydCreateUser(BaseModel):
    tg_id: int
    username: str = ""
    status: str = "active"
    first_name: str = ""
    last_name: str = ""
    total_cost: Optional[int] = None
    phone: str = ""
    description: str = ""


class PydDeleteUser(BaseModel):
    tg_id: int


class PydUpdateUser(BaseModel):
    tg_id: int
    values: Dict
