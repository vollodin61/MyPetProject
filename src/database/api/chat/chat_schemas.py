from pydantic import BaseModel


class MessagesModel(BaseModel):
    id: int
    message: str

    class Config:
        # orm_mode = True
        from_attributes = True
