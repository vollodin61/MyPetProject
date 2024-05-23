import asyncio

from httpx import AsyncClient
from icecream import ic
from loguru import logger
from sqlalchemy import insert, select

from conftests import client, async_session_maker, prepare_database, ac
from src.database.sql.models.user_models import Users

# asyncio.run(prepare_database())


async def test_add_user_():
    async with async_session_maker() as session:
        stmt = insert(Users).values(tg_id=11, total_spent=2, username="USERNAME")
        await session.execute(stmt)
        await session.commit()

        query = select(Users)
        result = await session.execute(query)
        logger.info(result.all())


# async def test_get_specific_operations():
#     with async_session_maker() as session:
#         query = select(Users).where(Users.tg_id == 11)
#         result = await session.execute(query)
#         ic(result.scalars().all())