from aiogram import Bot
from aiogram.fsm.context import FSMContext

from src.bots.sarbot.bot.data.bot_cfg import AvailableState as Avs


async def send_message_3_days(tg_id: int, txt: str, bot: Bot, state: FSMContext):
	await bot.send_message(tg_id, text=txt)

	if await state.get_state() == Avs.fst_lesson or await state.get_state() == Avs.fst_homework:
		await state.set_state(Avs.snd_lesson)
		# await bot.send_message(tg_id, f'{"+++" * 5}\nСейчас {await state.get_state() = }\n{"+++" * 5}')  # /// comment инфа о state
	elif await state.get_state() == Avs.snd_lesson or await state.get_state() == Avs.snd_homework:
		await state.set_state(Avs.trd_lesson)
		# await bot.send_message(tg_id, f'{"+++" * 5}\nСейчас {await state.get_state() = }\n{"+++" * 5}')  # /// comment инфа о state
	return state
