import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from environs import Env

from src.database.api.config.api_config import app
from src.database.api.routers.user_routers import session_local
# from src.database.sql.models.order_models import Orders
# # from src.database.sql.models.otz_donation_models import Otzs, Donations
# # from src.database.sql.models.poll_models import Polls
# from src.database.sql.models.product_models import Products
# from src.database.sql.models.user_models import Users
from tests import test_models


env = Env()
env.read_env()
DB_USER_TEST = env("DB_USER_TEST")
DB_PASS_TEST = env("DB_PASS_TEST")
DB_HOST_TEST = env("DB_HOST_TEST")
DB_PORT_TEST = env("DB_PORT_TEST")
DB_NAME_TEST = env("DB_NAME_TEST")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
test_models.Base.metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as sess:
        yield sess


app.dependency_overrides[session_local] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(test_models.Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(test_models.Base.metadata.drop_all)


# SETUP
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
