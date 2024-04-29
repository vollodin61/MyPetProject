import logging
import os
from aiogram import Router, Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from emoji import emojize
from environs import Env
from typing import Dict

from bots.data.common_data import format_text_html as fth

logging.basicConfig(level=logging.INFO)

env = Env()
env.read_env()
bot_token = env("TOKEN")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token=bot_token, parse_mode="HTML")
rt = Router()
dp.include_router(rt)
st1 = ['1', '2', '3']


def get_result(data: Dict):
	m_k = ''
	m_v = 0
	flag = False
	for k, v in data.items():
		if v > m_v:
			m_k = k
			m_v = v
			flag = False
		elif v == m_v:
			flag = True

	if flag:
		return 5
	else:
		return m_k


def get_file_docker(number: int = None, ):
	return Files.docker_dct[str(number)]


class AvailableState(StatesGroup):
	Q0 = State()
	Q1 = State()
	Q2 = State()
	Q3 = State()
	Q4 = State()
	Q5 = State()
	Q6 = State()
	Q7 = State()



class Emo:
	# коды эмодзи можно взять тут https://emojio.ru/smileys-emotion.html
	# или тут https://apps.timwhitlock.info/emoji/tables/unicode

	@staticmethod
	def emoj(smile):
		return emojize(smile, variant="emoji_type")

	ruble = emoj("₽")
	big_smile = emoj(":grinning_face_with_big_eyes:")
	hugs = emoj(":smiling_face_with_open_hands:")
	hand_over_mouth = emoj(":face_with_hand_over_mouth:")
	hundred = emoj(":hundred_points:")
	quiet = emoj(":shushing_face:")
	heart = emoj("❤️")
	omg_cat_face = emoj("🙀")
	red_exclamation = emoj("❗️")
	nerd_face = emoj(":nerd_face:")
	sunglasses = emoj("😎")
	explosive_head = emoj("🤯")
	hi = emoj("👋")
	just_smile = emoj("🙂")
	zero = emoj("0️⃣")
	one = emoj("1️⃣")
	two = emoj("2️⃣")
	three = emoj("3️⃣")
	four = emoj("4️⃣")
	five = emoj("5️⃣")
	six = emoj("6️⃣")
	seven = emoj("7️⃣")
	eight = emoj("8️⃣")
	nine = emoj("9️⃣")
	ten = emoj("🔟")
	hz = emoj("🤷‍♂️")
	please_eyes = emoj("🥺")
	plese = emoj("🙏")
	arrow_left = emoj("⬅️")
	arrow_right = emoj("➡️️")
	arrow_up = emoj("⬆️")
	arrow_down = emoj("⬇️")
	write = emoj('✍️')

	nums_for_quests = [one, two, three, four]


class Texts:
	q1 = ('Первый вопрос:\n'
		  '{}\n\n'
		  '{} Дилетант\n'
		  '{} Неразумный\n'
		  '{} Задача или проблема\n'
		  '{} Дорогой гость\n'.format(fth.bold("Клиент для тебя кто?"), *Emo.nums_for_quests))

	q2 = ('Второй вопрос:\n'
		  '{}\n\n'
		  '{} Эксперт\n'
		  '{} Бабушка с пирожками\n'
		  '{} Безликий персонал\n'
		  '{} Любящее сердце\n'.format(fth.bold("Кто ты для клиента?"), *Emo.nums_for_quests))

	q3 = ('Третий вопрос:\n\n'
		  '{}\n\n'
		  '{} Дал денег и больше не виделись\n'
		  '{} Благодарный, не в деньгах счастье\n'
		  '{} Регулярный, хоть и не дорогой\n'
		  '{} Вовлечённый единомышленник\n'.format(fth.bold("Как для тебя выглядит идеальный клиент?"), *Emo.nums_for_quests))

	q4 = ('Четвертый вопрос:\n\n'
		  '{}\n\n'
		  '{} Я дожму всех на отзывы\n'
		  '{} Собираю для себя/для души\n'
		  '{} Не люблю собирать отзывы\n'
		  '{} Собираю, ведь надо, чтоб как у всех\n'.format(fth.bold("Как для тебя выглядит работа с отзывами?"), *Emo.nums_for_quests))

	q5 = ('Четвертый вопрос:\n\n'
		  '{}\n\n'
		  '{} Не буду доказывать, сам же пришёл\n'
		  '{} Пусть спросит у того, кто прислал\n'
		  '{} Отвечаешь, но всё неохотнее\n'
		  '{} Извиняясь отвечаешь, сделаешь скидку\n'.format(fth.bold("Если клиент, пришедший по рекомендации, начинает задавать вопросы по поводу твоей компетенции/конечного результата"), *Emo.nums_for_quests))

	q6 = ('Пятый вопрос:\n\n'
		  '{}\n\n'
		  '{} Ко мне всегда возвращаются\n'
		  '{} Пошутить что ж он раньше не пришел\n'
		  '{} Ничего не скажу\n'
		  '{} Смутившись поблагодарить\n'.format(fth.bold("Если к вам пришёл клиент по рекомендации другого вашего клиента, вы скажете:"), *Emo.nums_for_quests))

	q7 = ('Шестой вопрос:\n\n'
		  '{}\n\n'
		  '{} Сообщить, что повысилась стоимость\n'
		  '{} Это и бесплатно не сложно сделать\n'
		  '{} Предложишь общие условия\n'
		  '{} Сделаете подешевле, как постоянному\n'.format(fth.bold("Если к вам повторно обращается клиент:"), *Emo.nums_for_quests))

	echo_text = f'Такое я не знаю{Emo.hz}\nНа всякий случай сброшу всё до начального уровня\nНажми /start, чтобы пройти опрос'
	help_text = (f'Вот что я знаю {Emo.nerd_face}:\n\n'
				 f'Опрос можно пройти только от начала до конца\nВопросов всего семь\n\n'
				 f'Если Вы прервались/забыли/передумали, то нажмите /start {Emo.arrow_left} и начните сначала\n\n'
				 f'Если у Вас другие вопросы, то можете {Emo.write} написать:\n'
				 f'моему админу Илье @good_cat_admin\n'
				 f'непосредственно Ирине Филатовой @ifillatovacoach\n\n'
				 f'А ещё можно посмотреть на сайте https://fillatova.ru/, что у нас есть вкусненького {Emo.big_smile}')
	result = fth.monospace(f"Спасибо, что прошёл опрос!!{Emo.hugs}\n\nСейчас пришлю результаты {Emo.big_smile}")
	after_result = (f'Понравился гайд? Можешь поделиться впечатлением, дать обратную связь? @fillatovacoach {Emo.please_eyes}\n\n'
					f'Зайди посмотреть, вот просто одним глазком {Emo.big_smile} https://fillatova.ru\n\n'
					f'А вот тут есть запись вебинара о том, как комплименты работают в соблазнении https://fillatova.ru/komplimenty\n\n'
					f'А здесь мини-практикум для специалистов и экспертов https://fillatova.ru/sarafanka')

	poll_name = 'Gaid from pollbot'
	firstname = 'message.from_user.firstname'
	msg_to_send = ''

class Files:
	lc_dct = {
		'1': os.path.abspath("expert_about.jpg")
	}

	docker_dct = {
		'1': {'about': os.path.abspath("expert_about.jpg"),
			  'gaid': os.path.abspath("expert_gaid.jpg")},
		'2': {'about': os.path.abspath("grandma_about.jpg"),
			  'gaid': os.path.abspath("grandma_gaid.jpg")},
		'3': {'about': os.path.abspath("unface_about.jpg"),
			  'gaid': os.path.abspath("unface_gaid.jpg")},
		'4': {'about': os.path.abspath("heartless_about.jpg"),
			  'gaid': os.path.abspath("heartless_gaid.jpg")},
		'5': {'about': os.path.abspath("vinaigrette_about.jpg"),
			  'gaid': os.path.abspath("vinaigrette_gaid.jpg")},
		'gaid_sarafanka': os.path.abspath("gaid_sarafanka.pdf")}
