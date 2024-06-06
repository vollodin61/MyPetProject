import asyncio
import re

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.sync import async_to_sync

from src.bots.userbot.bot.config.userbot_config import GlobalConfig

from src.database.api.schemas.user_schemas import PydCreateUser
from src.logs.my_ice import ice

test_purchase = {
    "name": "Книга Листаетов",
    "email": "df@dff.crr",
    "phone": "+0123456789",
    "username": "Ihdjjd",
    "checkbox_1": "yes",
    "checkbox_2": "yes",
    "payment": {
        "sys": "tinkoff",
        "systranid": "4471888162",
        "orderid": "2100966246",
        "products": [
            {
                "name": "Kowka",
                "quantity": 3,
                "amount": 6,
                "price": "2"
            },
            {
                "name": "Sarafanka",
                "quantity": 5,
                "amount": 5,
                "price": "1"
            }
        ],
        "amount": "11"
    },
    "formid": "form754184595",
    "formname": "Cart"
}


def re_get_username(input_name: str) -> str:
    """
    :param input_name: str    :rtype: str
    :return real TG username or string "invalidated username"
    """
    pattern = r"(?<=@).*"
    pattern2 = "(?<=.me/).*"
    username = "invalidated username"
    if "@" in input_name or ".me" in input_name:
        try:
            username = re.search(pattern, input_name).group()
        except:
            try:
                username = re.search(pattern2, input_name).group()
            except:
                pass
    else:
        username = input_name
    return username


def get_tg_id_by_username(username: str):
    with GlobalConfig.my_admin_bot as ubot:
        try:
            user = ubot.get_users(username)
            # ubot.stop()
            # ice(user)
            return {"tg_id": user.id}
        except Exception as err:
            return {"tg_id": None, "error": err}


async def get_(username: str):
    async with GlobalConfig.my_admin_bot as ubot:
        user = await ubot.get_users(username)
        return user


# ice((get_("ihdjjd")))


async def tilda_parser(some_dict: dict) -> tuple:
    username = re_get_username(some_dict.get("username"))
    ice(username)
    # tg_id = await get_tg_id_by_username(username=username)
    tg_id = await get_(username=username)
    ice(tg_id)
    ice(type(tg_id))
    tg_id = tg_id.id
    ice(tg_id)
    user = PydCreateUser(
        tg_id=tg_id,
        username=username,
        status="active",
        first_name=some_dict.get("name"),
        email=some_dict.get("email"),
        total_spent=some_dict.get("payment").get("amount"),
        phone=some_dict.get("phone"),
    )

    order = {
        "payment": some_dict.get("payment"),
        "formid": some_dict.get("formid"),
        "formname": some_dict.get("formname"),
    }

    return user, order

# u, o = tilda_parser(test_purchase)
# products = {
#     "products": o.get("payment").get("products"),
#     "quantity": o.get("payment").get("quantity"),
# }
# # ice(products)
# for _ in range(5):
#     get_tg_id_by_username("df")

# for _ in test_purchase.get("payment").get("products"):
#     ice(_.get("name"))
