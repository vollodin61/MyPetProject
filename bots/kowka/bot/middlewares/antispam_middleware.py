from random import randint
from time import sleep
from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.types.base import TelegramObject
from aiogram.fsm.storage.redis import RedisStorage
from asyncio import sleep as asy_sleep


class Antispam(BaseMiddleware):

	def __init__(self, storage: RedisStorage):
		# super().__init__()
		self._storage = storage

	async def __call__(self,
						handler: Callable[[TelegramObject, Dict[str, Any]],
						Awaitable[Any]],
						event: Message,
						data: Dict[str, Any]) -> Any:
		kurwa = f"user{event.from_user.id}"
		check_kurwa = await self._storage.redis.get(name=kurwa)
		if check_kurwa:
			if int(check_kurwa.decode()) == 1:
				wait = randint(5, 7)
				await self._storage.redis.set(name=kurwa, value=0, ex=wait)
				await event.answer(text=f"Помедленее, я записую... Подождите {wait} секунд")
				await asy_sleep(wait)
				return event.answer(text="Пишите, но не торопясь, я ж записую")
			return
		await self._storage.redis.set(name=kurwa, value=1, ex=5)

		return await handler(event, data)
