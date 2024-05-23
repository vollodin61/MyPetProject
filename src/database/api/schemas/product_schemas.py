from os import name

from pydantic import BaseModel


class PydCreateProduct(BaseModel):
    name: str = ""
    product_type: str = ""
    price: int = 0
    status: str = ""
