from dataclasses import dataclass
from aiogram.utils.markdown import hlink, hbold
from bots.data.common_data.smiles import Emo
from bots.sarbot.bot.data.bot_cfg import VideoUrls as vu


@dataclass
class Texts:
	student_greeting = (f'Приветствую тебя! Спасибо за проявленный интерес и доверие!\n\n'
						f'Если хочешь узнать подробно, что здесь может происходить, то жми {Emo.arrow_right} /help\n'
						f'А если готов сразу приступить, то нажимай "/fst_lesson" и начнём {Emo.just_smile}')
	fst_l = f"Первый урок {Emo.big_smile}"
	snd_l = f"Приступить к второму уроку {Emo.big_smile}"
	trd_l = f"Приступить к третьему уроку {Emo.big_smile}"

	pre_fst = (f"Напомню правила игры {Emo.big_smile}\n\n"
			   f"3 видео-урока, после каждого 3 дня на выполнение задания\n\n"
			   f"{hlink(title='Здесь', url='https://t.me/+uY4yhDwWIeQ5Y2Ey')} можно и нужно делиться впечатлениями "
			   f"и наблюдениями, задавать вопросы и получать на них ответы{Emo.hugs}\n\n"
			   f"У нас действует правило: сначала пробуем, потом спорим что так не работает "
			   f"(если есть желание поспорить {Emo.hand_over_mouth})")

	fst_homework = (f'Задание {Emo.nerd_face + Emo.arrow_down}\n\n'
					f'Создайте и пришлите инструкцию для вашего клиента.\n'
					f'Инструкция не более чем из 9 шагов.\n'
					f'Эта инструкция должна выглядеть, как инструкция в самолете {Emo.airplane}\n'
					f'С картинками и понятно, что происходит.\n'
					f'Инструкция для оплаты максимум из 3х пунктов:\n'
					f'- Заполнил\n'
					f'- Оплатил\n'
					f'- Получил ответ-инструкци и перешёл по ссылке')
	snd_homework = (f'Задание {Emo.nerd_face}{Emo.arrow_down * 2}\n\n'
					f'{hbold("Для тех, кто предоставляет материальные услуги:")}\n'
					f'{Emo.one} Создать список вопросов конкретно под себя, учитывая свою личную специфику.\n'
					f'{Emo.two} Провести коммуникацию используя прям список этих вопросов (в процессе делать записи, предупредив, '
					f'что будете делать записи). Исключением являются мастера маникюра, педикюра, парикмахеры, '
					f'визажисты ежедневного макияжа.\n'
					f'Свадебные, праздничные визажисты делают записи\n'
					f'{Emo.three} Все создают эскиз/техзадание\n\n'
					f'{Emo.red_exclamation}Список может быть в телефоне. Однако, список на бумаге вызывает большее доверие'
					f' и эффект "прозрачности" в коммуникации.\n\n\n'
					f'Для наставников:\n'
					f'{Emo.one} Создать пошаговый шаблон, что должен сделать твой клиент, когда начал с тобой работать.\n'
					f'{Emo.two} После первой встречи с клиентом создать дорожную карту обучения, '
					f'прислать её на проверку сюда в чат, или в личку мне\n'
					f'{Emo.three} Пришлите скриншот, как вы выглядите во время консультации, когда её проводите')
	trd_homework = (f'Задание{Emo.nerd_face + Emo.arrow_down * 3}\n\n'
					f'{Emo.one} Записать на диктофон коммуникацию, проведённую по алгоритму (это может быть, '
					f'как ваш подопечный, так и ваш клиент, друг, родственник и тд), в которой вы были экспетром, чему-то обучали\n'
					f'{Emo.two} Прислать @ifillatovacoach в личку на проверку')

	fst_lesson = (f"Смотри видео {hlink(title='первого урока', url=vu.video1_url)}\n"
				  f"Выполняй домашнее задание присылай на проверку с помощью команды /send_homework {Emo.hugs}\n\n"
				  f"{fst_homework}")
	snd_lesson = (
		f"Смотри {hlink(title='второй видео-урок', url=vu.video2_url)}, домашку присылай на проверку /send_homework {Emo.hugs}\n\n"
		f"А также посмотри пример одного из моих {hlink(title='рабочих мест', url=vu.work_place_url)} {Emo.just_smile}\n\n"
		f"{snd_homework}")
	trd_lesson = (f"А вот и последний {hlink(title='третий урок', url=vu.video3_url)}\n"
				  f"Всё также, выполняй и присылай домашку на проверку с помощью команды /send_homework{Emo.just_smile}\n\n"
				  f"{trd_homework}")

	sheduled_time = "Это по тайму текст"
	sheduled_cron = "Это крон текст"
	sheduled_interval = "Это интервал текст"
	poll_echo_text = (f'Такое я не знаю{Emo.hz}\nНа всякий случай сброшу всё до начального уровня\n'
					  f'Нажми /start, чтобы пройти опрос')
	help_text = (f'Вот что могу предложить в качестев помощи: {Emo.just_smile}\n\n'
				 f'У меня есть команды:\n'
				 f'/fst_lesson - начать первый урок\n'
				 f'После неё я пришлю видео-урок и задание к нему {Emo.nerd_face, Emo.write}\n'
				 f'При помощи команды /send_homework можно отправить домашку на проверку\n'
				 f'{hbold("ВАЖНО!!")} Домашкой я считаю следующее сообщение после команды /send_homework\n'
				 f'Постарайся прислать всё {hbold("одним сообщением")}\n'
				 f'В течение суток мы её проверим\n'
				 f'Через 3 дня после начала урока станет доступен слеующий урок\n\n'
				 f'Ещё могу открыть сайт Ирины Филатовой командой /site\n'
				 f'Там можно купить основной её курс "Доброе слово для кошки"{Emo.heart}\n\n'
				 f'Задать вопрос, на который не нашли ответ можете: \n'
				 f'1) моему админу и создателю - @good_cat_admin {Emo.big_smile}\n'
				 f'2) непосредственно Ирине Филатовой - @ifillatovacoach {Emo.heart}')

	known_user = (f"Приветствую! Можем начинать! {Emo.big_smile}\n\n"
				  f"Жми /fst_lesson, если хочешь приступить немедленно\n"
				  f"Или /help, если хочешь ознакомиться с информацией")
	unknown_user = (f"Не смог найти тебя в базе Сарафанки {Emo.confused}\n"
					f"Обратись, пожалуйста, к моему админу @good_cat_admin он найдёт решение\n\n"
					f"Или {Emo.arrow_right} fillatova.ru/sarafanka_order, если вы ещё не приобретали доступ\n\n"
					f"Или {Emo.arrow_right} fillatova.ru/sarafanka, если хотите ознакомиться поближе {Emo.just_smile}")
	done_text = ("Я отдал все материалы, которые у меня есть\n\n"
				 f'Могу открыть сайт Ирины Филатовой командой /site\n'
				 f'Там можно купить основной её курс "Доброе слово для кошки"{Emo.heart}\n\n'
				 f'Задать вопрос, на который не нашли ответ можете: \n'
				 f'1) моему админу и создателю - @good_cat_admin {Emo.big_smile}\n'
				 f'2) непосредственно Ирине Филатовой - @ifillatovacoach {Emo.heart}')