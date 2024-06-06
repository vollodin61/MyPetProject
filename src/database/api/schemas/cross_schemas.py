from pydantic import BaseModel


class PydUserProducts(BaseModel):
    user_id: int
    product: str

    class Config:
        from_attributes = True
