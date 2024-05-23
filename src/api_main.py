# import aioredis
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.bots.sarbot.bot.data.redis_connection import Singleton
from src.database.api.chat.chat_routers import chat_router
from src.database.api.jinja.pages.jinja_router import jinja_router
from src.database.api.routers.user_routers import user_router

from src.database.sql.config.db_config import Settings

sync_session_factory = Settings.sync_session_factory

app = FastAPI(title="Kowka API")
all_routers = [user_router, chat_router, jinja_router]
for router in all_routers:
    app.include_router(router)

app.mount("/static", StaticFiles(directory="database/api/jinja/static"), name="static")


# Благодаря этой функции клиент видит ошибки, происходящие на сервере, вместо "Internal server error"
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.__repr__()}),
    )


REDIS_HOST = Settings.REDIS_HOST
REDIS_PORT = Settings.REDIS_PORT


# @app.on_event("startup")
# async def startup_event():
#     redis = Singleton.get_connection(host=REDIS_HOST)
#     # redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run(app="api_main:app", reload=True)
