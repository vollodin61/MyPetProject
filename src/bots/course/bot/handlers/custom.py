from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from datetime import datetime, timedelta

from src.bots.common_data.smiles import Emo
from src.bots.sarbot.bot.data.texts import Texts as Txt
from src.bots.sarbot.bot.data.bot_cfg import bot, admins, AvailableState as Avs, scheduler
from src.bots.sarbot.bot.scheduler.apsched import send_message_3_days

cust_router = Router()


@cust_router.message(Command('site'))
async def go_to_site(msg: Message):
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text="Жмяк", url="https://fillatova.ru"))
	await msg.answer(text=f"Ссылка на сайт {Emo.arrow_down}", reply_markup=builder.as_markup())

@cust_router.message(Command('fst_lesson'))
async def fst_lesson_start(msg: Message, state: FSMContext):
	st = await state.get_state()
	if (st == None) or (st in Avs.bad_states):
		await msg.answer("Вы не можете начать практикум\nПомощь по кнопке /help")
		return
	try:
		if st == Avs.can_start:
			await msg.answer(text=Txt.fst_lesson)
			await state.set_state(Avs.fst_lesson)
			scheduler.add_job(send_message_3_days, trigger="date",
							  run_date=datetime.now() + timedelta(seconds=86400 * 3), # await sleep(86400 * 3)  # /// заменить количество секунд
							  kwargs={"tg_id": msg.from_user.id, "txt": Txt.snd_lesson, "bot": bot, "state": state})
			scheduler.add_job(send_message_3_days, trigger="date",
							  run_date=datetime.now() + timedelta(seconds=86400 * 6), # await sleep(86400 * 6)
							  kwargs={"tg_id": msg.from_user.id, "txt": Txt.trd_lesson, "bot": bot, "state": state})
			scheduler.add_job(send_message_3_days, trigger="date",
							  run_date=datetime.now() + timedelta(seconds=86400 * 7), # await sleep(86400 * 7)
							  kwargs={"tg_id": msg.from_user.id, "txt": Txt.done_text, "bot": bot, "state": state})

		else:
			await msg.answer(text="Вы уже начали курс, уроки будут присылаться автоматически")
	except Exception as err:
		text = (f"Ошибка - {err}\n\n"
				f"Произлошла у id={msg.from_user.id} username={msg.from_user.username}")
		await bot.send_message(chat_id=admins[0], text=text)
		await msg.answer("Что-то пошло не так, возникла ошибка. Я отправил её админу @good_cat_admim\n"
						 "Попробуйте ещё раз. Если опять увидите это сообщение, то можете подождать пока админ разберётся\n"
						 "Или можете написать ему {}".format(Emo.just_smile))


@cust_router.message(Command('send_homework'))
async def send_homework_cmd(msg: Message, state: FSMContext, bot: bot):
	try:
		st = await state.get_state()
		if st == Avs.fst_lesson:
			await msg.answer(text="Готов получить домашку первого урока")
			await state.set_state(Avs.fst_homework)
		elif st == Avs.snd_lesson:
			await msg.answer(text="Готов получить домашку второго урока")
			await state.set_state(Avs.snd_homework)
		elif st == Avs.trd_lesson:
			await msg.answer(text="Готов получить домашку третьего урока")
			await state.set_state(Avs.done)
		else:
			await msg.answer(text="Вы ещё не приступили к урокам")
	except Exception as err:
		txt = (f"Ошибка - {err}\n\n"
				f"Произлошла у id={msg.from_user.id} username={msg.from_user.username}")
		await bot.send_message(chat_id=admins[0], text=txt)
