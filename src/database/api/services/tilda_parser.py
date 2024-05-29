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


def get_tg_id_by_username(username: str):
    cl = "get_users"  # from userbot.config.ubot_cfg import client
    return 21


def tilda_parser(some_dict: dict) -> tuple:
    user = PydCreateUser(
        tg_id=get_tg_id_by_username(username=some_dict.get("username")),
        username=some_dict.get("username"),
        status="active",
        first_name=some_dict.get("name"),
        email=some_dict.get("email"),
        total_spent=some_dict.get("payment").get("amount"),
        phone=some_dict.get("phone"),
    )

    products_list = some_dict.get("payment").get("products")
    order = dict()
    order["payment"] = some_dict.get("payment")
    order["formid"] = some_dict.get("formid")
    order["formname"] = some_dict.get("formname")

    return user, order


a, b = tilda_parser(test_purchase)
ice(b)
