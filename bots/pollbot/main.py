import asyncio

from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from time import sleep
# sleep(180)

from bots.pollbot.bot.data.bot_cfg import bot, dp,Texts as txt, get_result, Files, Emo, get_file_docker
from bots.pollbot.bot.utils.bot_commands import set_commands
from bots.db.requests.async_requests_db_postgres import AsyncORM
from bots.db.requests.sync_requests_db_postgres import SyncORM


pollname = "Опрос Гайд-сарафанка"

@dp.message(Command('site'))
async def go_to_site(msg: Message):
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text="Жмяк", url="https://fillatova.ru"))
	await msg.answer(text=f"Ссылка на сайт {Emo.arrow_down}", reply_markup=builder.as_markup())


@dp.message(Command('help'))
async def help_message(msg: Message, state: FSMContext):
	await msg.answer(text=txt.help_text)
	await state.clear()


@dp.message(Command("start"))
async def start_message(msg: Message, state: FSMContext):
	try:
		await AsyncORM.insert_user_from_bot(msg)
		SyncORM.sync_insert_course_to_user(msg.from_user.id, pollname)
	except Exception as err:
		bot.send_message(590018906, f"\n\n\n{err.__repr__() = }\n\n\n")
	await state.clear()
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text='1', callback_data='1 1'))
	builder.add(InlineKeyboardButton(text='2', callback_data='1 2'))
	builder.add(InlineKeyboardButton(text='3', callback_data='1 3'))
	builder.add(InlineKeyboardButton(text='4', callback_data='1 4'))
	await msg.answer(f'Приветствую! '
						 f'<code>{msg.from_user.username if msg.from_user.username else msg.from_user.first_name}</code>\n'
						 f'Давай сразу начнём!{Emo.just_smile}\n\n'
						 f'{txt.q1}', reply_markup=builder.as_markup())
	dct = {'1': 0, '2': 0, '3': 0, '4': 0}
	await state.set_data(dct)
	username = msg.from_user.username
	firstname = msg.from_user.first_name
	user_id = msg.from_user.id
	msg_text = (f'title: Клиенты для тебя\n'
				f'survey_name: Gaid from pollbot\n'
				f'firstname: {firstname}\n'
				f'tg_username: {username if username else user_id}\n')
	# await bot.send_message(5431925010, text=msg_text)


@dp.callback_query(F.data[0] == '1')
async def q1_1(callback: CallbackQuery, state: FSMContext):
	await callback.msg.edit_reply_markup()
	user_data = await state.get_data()
	user_data[f'{callback.data[2]}'] += 1  # тут мы увеличиваем на 1 нужный элемент словаря
	await state.update_data(data=user_data)

	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text='1', callback_data='2 1'))
	builder.add(InlineKeyboardButton(text='2', callback_data='2 2'))
	builder.add(InlineKeyboardButton(text='3', callback_data='2 3'))
	builder.add(InlineKeyboardButton(text='4', callback_data='2 4'))
	await callback.msg.answer(text=txt.q2, reply_markup=builder.as_markup())


@dp.callback_query(F.data[0] == '2')
async def q2_2(callback: CallbackQuery, state: FSMContext):
	await callback.msg.edit_reply_markup()
	user_data = await state.get_data()
	user_data[f'{callback.data[2]}'] += 1
	await state.update_data(data=user_data)

	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text='1', callback_data='3 1'))
	builder.add(InlineKeyboardButton(text='2', callback_data='3 2'))
	builder.add(InlineKeyboardButton(text='3', callback_data='3 3'))
	builder.add(InlineKeyboardButton(text='4', callback_data='3 4'))
	await callback.msg.answer(text=txt.q3, reply_markup=builder.as_markup())


@dp.callback_query(F.data[0] == '3')  # меняй тут
async def q3_3(callback: CallbackQuery, state: FSMContext):
	await callback.msg.edit_reply_markup()
	user_data = await state.get_data()
	user_data[f'{callback.data[2]}'] += 1
	await state.update_data(data=user_data)

	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text='1', callback_data='4 1'))  # и тут
	builder.add(InlineKeyboardButton(text='2', callback_data='4 2'))  # и тут
	builder.add(InlineKeyboardButton(text='3', callback_data='4 3'))  # и тут
	builder.add(InlineKeyboardButton(text='4', callback_data='4 4'))  # и тут
	await callback.msg.answer(text=txt.q4, reply_markup=builder.as_markup())  # и тут


# @dp.callback_query(F.data[0] == '4')  # меняй тут
# async def q4_4(callback: CallbackQuery, state: FSMContext):  # и тут
# 	await callback.msg.edit_reply_markup()
# 	user_data = await state.get_data()
# 	user_data[f'{callback.data[2]}'] += 1
# 	await state.update_data(data=user_data)
# 	builder = InlineKeyboardBuilder()
# 	builder.add(InlineKeyboardButton(text='1', callback_data='5 1'))  # и тут
# 	builder.add(InlineKeyboardButton(text='2', callback_data='5 2'))  # и тут
# 	builder.add(InlineKeyboardButton(text='3', callback_data='5 3'))  # и тут
# 	builder.add(InlineKeyboardButton(text='4', callback_data='5 4'))  # и тут
# 	await callback.msg.answer(text=txt.q5, reply_markup=builder.as_markup())  # и тут


@dp.callback_query(F.data[0] == '4')  # меняй тут
async def q5_5(callback: CallbackQuery, state: FSMContext):  # и тут
	await callback.msg.edit_reply_markup()
	user_data = await state.get_data()
	user_data[f'{callback.data[2]}'] += 1
	await state.update_data(data=user_data)

	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text='1', callback_data='6 1'))  # и тут
	builder.add(InlineKeyboardButton(text='2', callback_data='6 2'))  # и тут
	builder.add(InlineKeyboardButton(text='3', callback_data='6 3'))  # и тут
	builder.add(InlineKeyboardButton(text='4', callback_data='6 4'))  # и тут
	await callback.msg.answer(text=txt.q6, reply_markup=builder.as_markup())  # и тут


@dp.callback_query(F.data[0] == '6')  # меняй тут
async def q6_6(callback: CallbackQuery, state: FSMContext):  # и тут
	await callback.msg.edit_reply_markup()
	user_data = await state.get_data()
	user_data[f'{callback.data[2]}'] += 1
	await state.update_data(data=user_data)

	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text='1', callback_data='7 1'))  # и тут
	builder.add(InlineKeyboardButton(text='2', callback_data='7 2'))  # и тут
	builder.add(InlineKeyboardButton(text='3', callback_data='7 3'))  # и тут
	builder.add(InlineKeyboardButton(text='4', callback_data='7 4'))  # и тут
	await callback.msg.answer(text=txt.q7, reply_markup=builder.as_markup())  # и тут


@dp.callback_query(F.data[0] == '7')  # Это последний хендлер, когда все ответы есть.
async def result(callback: CallbackQuery, state: FSMContext):
	await callback.msg.edit_reply_markup()
	user_data = await state.get_data()
	user_data[f'{callback.data[2]}'] += 1

	await state.clear()
	await callback.msg.answer(text=txt.result)
	await asyncio.sleep(3)
	await callback.msg.answer_document(FSInputFile(get_file_docker(get_result(user_data))['about']))
	await callback.msg.answer_document(FSInputFile(get_file_docker(get_result(user_data))['gaid']))
	await asyncio.sleep(60)  # TODO при деплое на сервак сделать здесь 3 минуты задержку
	await callback.msg.answer_document(FSInputFile(Files.docker_dct['gaid_sarafanka']))
	await asyncio.sleep(30)  # TODO при деплое на сервак сделать здесь 30 sec задержку
	await callback.msg.answer(text=txt.after_result)
	# todo добавить тут функцию update_user_data, где в бд будет добавляться результат опроса

@dp.message()
async def any_message(msg: Message, state: FSMContext):
	try:
		await msg.answer(txt.echo_text)
		await state.clear()
	except Exception as e:
		print(e)


async def main():
	await set_commands(bot)
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())
