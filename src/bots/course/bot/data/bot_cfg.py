from dataclasses import dataclass

from aiogram import Dispatcher, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from environs import Env
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from . redis_connection import Singleton

env = Env()
env.read_env()
bot_token = env("TOKEN")
admins = list(map(lambda x: int(x), (env('ADMINS')).split(', ')))  # превращаем строку админов в список int
# red = Singleton.get_connection(host="0.0.0.0")  # /// comment ВЫБЕРИ для докера или локально РЕДИСКУ
red = Singleton.get_connection(host='rediska')  # /// comment DOCKER
red_storage = RedisStorage(red)
storage = MemoryStorage()
dp = Dispatcher(storage=red_storage)
bot = Bot(token=bot_token, parse_mode="HTML")
scheduler = AsyncIOScheduler(timezone="UTC")


class AvailableState(StatesGroup):
	can_start = State("can_start")
	not_in_list = State("not_in_list")
	fst_lesson = State("1 lesson")
	fst_homework = State("1 homework")
	snd_lesson = State("2 lesson")
	snd_homework = State("2 homework")
	trd_lesson = State("3 lesson")
	done = State("DONE")
	st_ban = State("ready_to_ban")
	st_permban = State("ready_to_permban")
	st_ask_to_delete = State("ready_to_ask_to_delete")
	st_deactive = State("ready_to_deactive")
	bad_states = (not_in_list, st_ban, st_permban, st_ask_to_delete, st_deactive)


@dataclass
class SheetParams:
	pass


@dataclass
class VideoUrls:
	pass
