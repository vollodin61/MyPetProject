from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

admin_router = Router()


@admin_router.message(F.text == "ban@" and F.from_user.id == 6558982323)
async def ban(msg: Message, state: FSMContext):
	# давайте tg_id кого забанить
	# if msg.from_user.id == 6558982323:
	await msg.answer(text="tg_id кого баним?")
	# await state.set_data(Avs.st_ban)
	# SyncORM.sync_change_status(tg_id=, "ban")
