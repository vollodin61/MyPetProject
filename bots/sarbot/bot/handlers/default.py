from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bots.sarbot.bot.data.bot_cfg import AvailableState as Avs, bot, admins
from bots.sarbot.bot.data.texts import Texts as Txt
from bots.db.requests.async_requests_db_postgres import AsyncORM
from bots.db.requests.sync_requests_db_postgres import SyncORM
from bots.db.data.db_cfg import UserStatus as Us

def_router = Router()


@def_router.message(Command('start'))
async def cmd_start(msg: Message, state: FSMContext, bot: bot):  # /// comment попробовать сделать start в default handler через match-case вместо if else
	# logging.basicConfig(level=logging.DEBUG)
	try:
		await AsyncORM.insert_user_from_bot(msg)
	except Exception as err:
		print(f"\n\n\n{err.__repr__() = }\n\n\n")
	# await state.clear()  # /// comment Это тут для тестирования /// comment testing
	user = await AsyncORM.select_user_by_tg_id(msg.from_user.id)
	user_products = await AsyncORM.get_user_products(tg_id=msg.from_user.id)
	# Проверить есть ли у него Сарафанка в продуктах
	# if user_products is not None:
	if user_products == None:  # /// comment testing
		# st = await state.get_state()
		# await msg.answer(f"state = {st =}")
		await msg.answer(text=Txt.unknown_user)
		await bot.send_message(chat_id=admins[0],
							   text=f"У этого нет Сарафанки в базе {'@' + msg.from_user.username, msg.from_user.id}")
		return

	if user.status not in Us.all_bad:
		st = await state.get_state()
		if ("Сарафанка" in user_products) and (user.status != "deactivated"):
			await state.set_state(Avs.can_start)
			await msg.answer(text=Txt.student_greeting)
			await msg.answer(text=Txt.pre_fst)

		elif st in [Avs.fst_lesson, Avs.fst_homework, Avs.snd_lesson, Avs.snd_homework]:
			await msg.answer("Нужно подождать, я присылаю видео-уроки 1 раз в 3 дня")
		elif st == Avs.trd_lesson:
			await msg.answer(text=Txt.done_text)
			await state.set_state(Avs.done)
	elif user.status == 'ask_to_delete':
		await msg.answer(Us.text_to_status[user.status])
		await bot.send_message(chat_id=admins[2], text=f"{Us.ask_to_delete_text_to_admin}\n"
													   f"username = @{msg.from_user.username}")
	else:
		await msg.answer(Us.text_to_status[user.status])


@def_router.message(Command('help'))
async def cmd_help(msg: Message):
	try:
		await msg.answer(text=Txt.help_text)
	except Exception as exc:
		print(exc)


@def_router.message()
async def echo(msg: Message, state: FSMContext, bot: bot):
	if msg.from_user.id == admins[1]:  # это я по идее могу боту сарафанки отправить какой-то текст другого пользователя и добавить его бд
		try:
			newbie_data = SyncORM.sync_re_msg_text_to_list(msg.text)
			SyncORM.sync_create_user_from_ifill_bot(newbie_data)
		except: pass
		try:
			SyncORM.sync_insert_course_to_user(tg_id=newbie_data[0], product=newbie_data[4])
			return
		except Exception:
			return
	try:
		st = await state.get_state()
		if st in (Avs.fst_homework, Avs.snd_homework, Avs.done):
			txt = (f'Домашка по {await state.get_state()}\n\n'
				   f'от id={msg.from_user.id} username={msg.from_user.username}\n\n'
				   f'Непосредственно текст:\n{msg.text}\n\n'
				   f'{msg.audio = }\n\n'
				   f'{msg.document = }\n\n'
				   f'{msg.photo = }')
			await bot.send_message(chat_id=admins[0], text=txt)
			# await bot.send_message(chat_id=admins[1], text=txt)

	except Exception as err:
		await msg.answer(Txt.poll_echo_text)
		text = (f"Ошибка - {err}\n\n"
				f"Произлошла у id={msg.from_user.id} username={msg.from_user.username}")
		await bot.send_message(chat_id=admins[0], text=text)
