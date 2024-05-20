import re
from dataclasses import dataclass
from datetime import timedelta, timezone, datetime
from typing import List

from pyrogram import Client
from pyrogram.types import Message

from bot.data.texts import MessageTextAttributes as mta


def tg_nik_finder(string):
	pattern1 = r'(?<=me\/).+'
	pattern2 = r'(?<=Input_2: ).+'
	pattern3 = r'(?<=Ссылка_на_Телеграм: ).+'
	pattern_list = [pattern1, pattern2, pattern3]

	for i in pattern_list:
		try:
			ans = re.search(pattern=i, string=string).group()
			return ans
		except Exception:
			pass
	return print('tg_nik_finder find HUI')


def clean_otz_text(text):
	"""ЭТО ДОЛЖНО ПРЕВРАЩАТЬ ТЕКСТ ОТЗЫВА, КОТОРЫЙ ПРИСЛАЛ ТИЛЬДА БОТ В СТРОКУ, КОТОРУЮ МОЖНО ДОБАВИТЬ В БД"""
	with open('/home/i/MyPros/F/pyro_echo/data/message_text.txt', 'w', encoding='utf-8') as f:
		f.write(text)

	with open('/home/i/MyPros/F/pyro_echo/data/message_text.txt', 'r', encoding='utf-8') as txt:
		new_text = ''
		for line in txt.readlines():
			if line.startswith('Textarea: '):
				new_text += line[10:]
			if not line.startswith(mta.bad_words_tuple):
				new_text += line
	return new_text


@dataclass
class FinderValues:
	def __init__(self):
		self.sent_datetime = None
		self.table_values = None
		self.ord_defines = ("cat_7000", "webinars", "club", "sarafanka")
		self.define = None

	def orders_val(self, message: Message, define: str) -> List:
		self.text = message.text
		self.message = message
		self.price = re.findall(r"Payment Amount: .+", self.text)[0][16:]
		self.name = re.findall(r"Name: .+", self.text)[0][6:]
		self.tg_username = tg_nik_finder(self.text)
		if define == 'Вебинар':  # TODO продумать/потом сделать паттерн, если несколько вебинаров купили. И если купили вебинар/ы и Кошку, может быть сделать просто одну отбивку для всех типа "спасибо, что выбрал нас, за доверие, давай делать мир добрее
			self.define = re.findall(r'1. .+', message.text)[0][3:]

		self.phone = re.findall(r'Phone: .+', message.text)[0][7:]
		self.email = re.findall(r"Email: .+", message.text)[0][7:]
		self.sent_datetime = datetime.now(tz=timezone(timedelta(hours=3))).strftime('%H:%M:%S %d/%m/%Y')
		self.order_id = re.findall(r'Order #.+', message.text)[0][7:]
		self.payment_id = re.findall(r'Payment ID: Tinkoff Payment: .+', message.text)[0][29:]
		self.table_values = [
			self.price, self.name, self.tg_username, self.define, self.phone,
			self.email, self.sent_datetime, self.order_id, self.payment_id
		]
		return self.table_values

	def surveys(self, message: Message):
		self.message = message
		self.ans = re.findall(r'Клиенты_для_тебя_кто', self.message.text)
		self.survey_name = ''
		if self.ans:
			self.survey_name = 'Пройди опрос - получи гайд'

		self.name = re.findall(r"Input: .+", self.message.text)[0][7:]
		self.tg_username = tg_nik_finder(message.text)
		self.email = re.findall(r"Email: .+", self.message.text)[0][7:]
		self.sent_datetime = datetime.now(tz=timezone(timedelta(hours=3))).strftime('%H:%M:%S %d/%m/%Y')
		self.table_values = [self.survey_name, self.name, self.tg_username, self.email, self.sent_datetime]
		return self.table_values


	def func_title(self, message: Message):
		return re.findall(r"title: .+", message.text)[0][7:]


	def tg_bot_polls(self, message: Message):
		self.message = message
		self.survey_name = re.findall(r"survey_name: .+", self.message.text)[0][13:]
		self.name = re.findall(r"firstname: .+", self.message.text)[0][11:]
		self.tg_username = re.findall(r'username: .+', self.message.text)[0][10:]
		self.email = ''
		self.sent_datetime = datetime.now(tz=timezone(timedelta(hours=3))).strftime('%H:%M:%S %d/%m/%Y')
		self.table_values = [self.survey_name, self.name, self.tg_username, self.email, self.sent_datetime]
		return self.table_values


	def otzs(self, message: Message):
		self.name = re.findall(r"Name: .+", message.text)[0][6:]
		self.sent_datetime = datetime.now(tz=timezone(timedelta(hours=3))).strftime('%H:%M:%S %d/%m/%Y')
		self.textarea = clean_otz_text(message.text)
		self.table_values = [self.name, self.sent_datetime, self.textarea]
		return self.table_values
