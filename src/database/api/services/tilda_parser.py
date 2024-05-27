from pyrogram import Client

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
                "name": "2нд Тест Пуршасе",
                "quantity": 3,
                "amount": 6,
                "price": "2"
            },
            {
                "name": "TEST_PURCHASE",
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


def get_tg_id_by_username(username: str):
    cl = "get_users"  # from userbot import client
    return 0


def tilda_parser(some_dict: dict):
    user = PydCreateUser(
        tg_id=get_tg_id_by_username(username=some_dict.get("username")),
        username=some_dict.get("username"),
        status="active",
        first_name=some_dict.get("name"),
        # email=some_dict.get("email"), noqa
        total_spent=some_dict.get("payment").get("amount"),
        phone=some_dict.get("phone"),

    )

    products = some_dict.get("payment").get("products")
    order = some_dict.get("payment").get("orderid")
    return user, products


a, b = tilda_parser(test_purchase)
ice(a, b)
