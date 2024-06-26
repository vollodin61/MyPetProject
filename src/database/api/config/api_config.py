from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.database.sql.config.db_config import Settings
from src.database.api.chat.chat_routers import chat_router
from src.database.api.requests.crud.products_crud import product_router
# from src.database.api.jinja.pages.jinja_routers import jinja_router
from src.database.api.requests.crud.users_crud import user_router

app = FastAPI(title="Kowka API")
all_routers = (
    user_router,
    chat_router,
    product_router,
    # jinja_router,
)

for router in all_routers:
    app.include_router(router)

app.mount("/static", StaticFiles(directory="src/database/api/jinja/static"), name="static")


# Благодаря этой функции клиент видит ошибки, происходящие на сервере, вместо "Internal server error"
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()}),
#     )


REDIS_HOST = Settings.REDIS_HOST
REDIS_PORT = Settings.REDIS_PORT

# @app.on_event("startup")
# async def startup_event():
#     redis = Singleton.get_connection(host=REDIS_HOST)
#     # redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
