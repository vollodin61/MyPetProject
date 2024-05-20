from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message


class CheckRoleMiddleware(BaseMiddleware):

	async def __call__(self,
						handler: Callable[[Message, Dict[str, Any]],
						Awaitable[Any]],
						event: Message,
						data: Dict[str, Any]) -> Any:
		if event.from_user.id == 6558982323:
			data["is_admin"] = True
		return await handler(event, data)
