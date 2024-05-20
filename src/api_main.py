from enum import Enum
from typing import List

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

from src.database.api.routers import user_router
from src.database.sql.config.db_config import Engines

# from src.logs.my_logger import MyLogger

sync_session_factory = Engines.sync_session_factory
# ice = MyLogger.ice
# logger = MyLogger.log_debug

app = FastAPI(title="Kowka API")
app.include_router(user_router)

fake_users = [
    {"id": 232, "role": "232_motherfucker"},
    {"id": 11, "role": ["11_motherfucker"]},
    {"id": 12, "role": "12_motherfucker", "name": [{"id": 1, "name": "LOH", "type": "first_name"}]},
]
fake_products = [
    {"id": 22, "user_id": 232, "name": "Кошка", "price": 7000},
    {"id": 44, "user_id": 232, "name": "Сарафанка", "price": 2200},
]


# Благодаря этой функции клиент видит ошибки, происходящие на сервере, вместо "Internal server error"
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # return PlainTextResponse(str(exc), status_code=400)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/products/")
async def get_user_products(limit: int = 1, offset: int = 0):
    return fake_products[offset:][:limit]


fake_users2 = [
    {"id": 1100, "role": "bad motherfucker"}
]


@app.post("/users/{user_id}")
async def change_user(user_id: int, new_role: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user["role"] = new_role
    return {"status": 200, "data": current_user}


class PydUserProducts(BaseModel):
    id: int
    user_id: int
    name: str
    price: float


@app.post("/products/")
async def add_products(products: List[PydUserProducts]):
    fake_products.extend(*products)  # may be not extract by *
    return {"status": 200, "data": fake_products}
