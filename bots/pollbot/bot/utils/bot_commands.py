from aiogram.types import BotCommand


async def set_commands(bot):
	await bot.set_my_commands([
		BotCommand(command="start", description="Пройти опрос"),
		BotCommand(command="help", description="Помощь"),
		# BotCommand(command="fst_lesson", description="Перейти к первому уроку"),
		# BotCommand(command="snd_lesson", description="Перейти ко второму уроку"),
		# BotCommand(command="trd_lesson", description="Перейти ко третьему уроку"),
		# BotCommand(command="send_homework", description="Перейти ко третьему уроку"),
		# BotCommand(command="sche", description="Scheduler"),
		BotCommand(command="site", description="Перейти на сайт fillatova.ru"),
		# BotCommand(command="test_states", description="тестим машину состояний"),
	])
