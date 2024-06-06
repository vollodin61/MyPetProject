from dataclasses import dataclass
from typing import Tuple

from bot.data.smiles import Emo


@dataclass
class MessageTextAttributes:
	webinar: str = '700 RUB'
	club: str = '2000 RUB'
	course: str = '7000 RUB'
	course_again: str = '3500 RUB'
	survey: str = 'Клиенты_для_тебя'
	otz: str = 'otz'
	sarafanka: str = '2200 RUB'
	master: str = '50000 RUB'
	master_10: str = '45000 RUB'
	bad_words_tuple: Tuple = ("Request", "Name", "Additional", "Transaction", "Block", "https", "Textarea: ",)


@dataclass
class Titles:
	course: str = "Кошка"
	course_again: str = "Кошка повтор"
	webinar: str = "Вебинары"
	club: str = "Клуб"
	survey: str = "Опросы"
	otz: str = "Отзывы"
	sarafanka: str = "Сарафанка"
	master: str = "Мастер-группа"


@dataclass
class Statuses:
	is_first: bool = False
	new_member: str = "Вступил"
	webinar: str = "Вебинар"
	master: str = "just_status"


@dataclass
class Urls:
	club_url: str = ''
	kowka_url: str = 'https://fillatova.ru/'
	kowka_order_url: str = 'https://fillatova.ru/course'
	sarafanka_url: str = 'https://fillatova.ru/sarafanka'
	sarafanka_order_url: str = 'https://fillatova.ru/sarafanka_order'
	webinars_url: str = 'https://fillatova.ru/webinars'
	webinars_order_url: str = 'https://fillatova.ru/webinars_order'


@dataclass
class Texts:
	club_url: str = Urls.club_url

	if_master: str = (f'Привет! Спасибо, что присоеденился, доверие, и выбор!\n'
				 f'Мне очень приятно! {Emo.hugs}\n\n'
				 f'Начало по набору группы, пока точной даты нет')
	if_survey: str = (f'Здравствуйте! Я Филатова Ирина, автор курса "Доброе слово для кошки"\n'
				 f'Спасибо, что прошли опрос! {Emo.just_smile}\n\n'
				 f'Удалось ли прочитать рекомендации для себя? Что думаете, насколько узнали себя?)\n'
				 f'Буду рада, если поделитесь впечатлением {Emo.just_smile}')
	if_club: str = f'Привет! Добро пожаловать в клуб!\n\nПрисоединяйся!)\n{club_url}'
	if_club_again: str = (f'Привет! Спасибо за продление участия в Клубе!)\n\n'
					 f'Присоединяйся!)\n{club_url}')
	if_course: str = (f'Здравствуйте! Я Филатова Ирина, автор курса "Доброе слово для кошки"\n'
				 f'Спасибо за проявленный интерес и доверие! {Emo.just_smile} Оплата прошла успешно.\n\n'
				 f'Присоединяйтесь к группе в чате https://t.me/+DYdesZ1aa9EyZTMy {Emo.big_smile}')
	if_course_again: str = (f'Привет! \n'
					   f'Спасибо за доверие и желание! Добро пожаловать на повторное прохождение курса!\n'
					   f'Ссылка на чат придёт сюда за 2 дня до старта.\n\n'
					   f'Иногда алгоритмы телеграма дают сбои. Если ссылка не пришла вовремя, то напишите мне {Emo.write}')
	if_webinar: str = (f'Здравствуйте!\n'
				  f'Спасибо за проявленный интерес и доверие!\n\n'
				  f'Приятного просмотра <a href="https://youtu.be/yjD15zozpik">{Emo.just_smile}</a>')
	if_sarafanka: str = (f'Здравствуйте! Я Филатова Ирина, автор практикума "Сарафанка"\n'
				 f'Спасибо за проявленный интерес и доверие! Оплата прошла успешно.\n\n'
				 f'@FilatovaSarafankaBot - приятного прохождения практикума! {Emo.hugs}\n\n')
	day_remind_text: str = (f'Здравствуйте!\n'
					   f'Вы получили гайд? Почерпнули что-то полезное для себя?'
					   f'Буду благодарна обратной связи {Emo.just_smile}')
	newbie: str = "newbie\nid"
	standard: str = ('Order #1824954494'
				'1. Практикум по продвижению через Сарафанное радио: 2200 (1 x 2200))\n'
				'The order is paid for.\n'
				'Payment Amount: 2200 RUB\n'
				'Payment ID: Tinkoff Payment: 4104749035\n'
				'\n'
				'Purchaser information:\n'
				'Name: Пися Камушкин\n'
				'Email: df@dff.crr\n'
				'Phone: +1234567890\n'
				'Ссылка_на_Телеграм: @Ihdjjd\n'
				'Checkbox: yes\n'
				'Checkbox_2: yes\n'
				'\n'
				'Additional information:\n'
				'Transaction ID: 5368059:5978896451\n'
				'Block ID: rec700920676\n'
				'Form Name: Cart\n'
				'https://fillatova.ru/sarafanka_order\n'
				'-----')
