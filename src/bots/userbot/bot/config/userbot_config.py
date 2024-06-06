import os
from dataclasses import dataclass
from typing import Tuple

import environs
from environs import Env
from google.oauth2.service_account import Credentials
from gspread_asyncio import AsyncioGspreadClientManager
from pyrogram import Client
from pyrogram.enums import ParseMode


@dataclass
class GlobalConfig:
	@staticmethod
	def get_scoped_credentials(credentials, scopes):
		def prepare_credentials():
			return credentials.with_scopes(scopes)

		return prepare_credentials

	env: environs.Env = Env()
	env.read_env()

	admins_ids: Tuple = tuple(map(lambda x: int(x), env("admins_ids").split(", ")))
	admins_names: Tuple = tuple(map(lambda x: x, env("admins_names").split(", ")))
	admins: Tuple = tuple(map(lambda x: x, env("admins").split(", ")))

	add = {int(tg_id): tg_name for tg_id, tg_name in zip(admins_ids, admins_names)}
	admins_dct = {name: value for name, value in zip(admins, add.items())}

	# huper_dct = {name: value for name, value in zip(tuple(map(lambda x: x, env("admins").split(", "))),
	# 												{int(tg_id): tg_name for tg_id, tg_name in
	# 		ЭТО ПРОСТО ТУТ ТАК ДЛЯ КРАСОТЫ))))		 zip(tuple(map(lambda x: int(x), env("admins_ids").split(", "))),
	# 													 tuple(map(lambda x: x,
	# 															   env("admins_names").split(", "))))}.items())}
	# ic(huper_dct)
	# ic(type(add))

	ifill_bot: Client = Client(name="ifill_bot", api_id=env("ifill_id"), api_hash=env("ifill_hash"),
							   parse_mode=ParseMode.HTML)
	my_admin_bot: Client = Client(name="my_admin_bot", api_id=env("my_admin_id"), api_hash=env("my_admin_hash"),
								  parse_mode=ParseMode.HTML)
	ira_bot: Client = Client(name="ira_bot", api_id=env("ira_id"), api_hash=env("ira_hash"), parse_mode=ParseMode.HTML)
	my_bot: Client = Client(name="my_acc", api_id=env("my_id"), api_hash=env("my_hash"), parse_mode=ParseMode.HTML)

	scopes = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
			  "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
	# google_credentials = Credentials.from_service_account_file(os.path.abspath(".pyroecho.json"))  # DOCKER
	google_credentials = Credentials.from_service_account_file("/home/i/MyPros/FBotFactory/src/bots/userbot/bot/config/.pyroecho.json")  # DOCKER
	scoped_credentials = get_scoped_credentials(google_credentials, scopes)
	google_client_manager = AsyncioGspreadClientManager(scoped_credentials)

	cat_key = '1LeT6zkDbdS99Mx7w-jN8f4IFihf8lhFbQMx34NyS7hc'
