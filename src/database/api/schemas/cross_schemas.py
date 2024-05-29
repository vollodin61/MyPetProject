from pydantic import BaseModel


class PydUserProducts(BaseModel):
    user_id: int
    product: str
