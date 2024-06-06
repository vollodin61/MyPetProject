from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.bots.course.bot.data.bot_cfg import env, AvailableState
from src.database.api.requests.sync.sync_req import SyncORM

admin_router = Router()

admin = env("ADMIN")


@admin_router.message(F.text == "ban@" and F.from_user.id == admin)
async def ban(msg: Message, state: FSMContext):
	await msg.answer(text="tg_id кого баним?")
	# получить id из сообщения
	# изменить в бд статус на banned
