from aiogram.types import BotCommand


async def set_commands(bot):
	await bot.set_my_commands([
		BotCommand(command="start", description="Пройти опрос"),
		BotCommand(command="help", description="Помощь"),
		BotCommand(command="site", description="Перейти на сайт fillatova.ru"),
	])
