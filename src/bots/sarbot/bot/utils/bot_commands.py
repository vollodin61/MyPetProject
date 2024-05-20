from aiogram.types import BotCommand, BotCommandScopeAllChatAdministrators


async def set_commands(bot):
	await bot.set_my_commands([
		BotCommand(command="start", description="Начать практикум"),
		BotCommand(command="help", description="Помощь"),
		BotCommand(command="fst_lesson", description="Перейти к первому уроку"),
		# BotCommand(command="snd_lesson", description="Перейти ко второму уроку"),
		# BotCommand(command="trd_lesson", description="Перейти ко третьему уроку"),
		BotCommand(command="send_homework", description="Отправить домашку на проверку"),
		# BotCommand(command="sche", description="Scheduler"),
		BotCommand(command="site", description="Перейти на сайт fillatova.ru"),
		# BotCommand(command="test_states", description="тестим машину состояний"),
	])


async def set_admin_commands(bot):
	await bot.set_my_commands(
			[
				BotCommand(command="add_user_product", description="Добавить пользователю продукт"),
				BotCommand(command="add_user", description="Добавить пользователя"),
				BotCommand(command="ban_user", description="Забанить пользователя"),
				BotCommand(command="permban_user", description="Забанить пользователя навсегда"),
				BotCommand(command="deactive_status", description="Деактив статус"),
				BotCommand(command="ask_to_delete", description="Запросил удалиться"),
				BotCommand(command="change_status", description="Поменять статус пользователя"),
			],
			scope=BotCommandScopeAllChatAdministrators()
	)