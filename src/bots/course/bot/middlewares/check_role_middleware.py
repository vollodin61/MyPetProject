from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

from src.bots.course.bot.data.bot_cfg import admins


class CheckRoleMiddleware(BaseMiddleware):

	async def __call__(self,
						handler: Callable[[Message, Dict[str, Any]],
						Awaitable[Any]],
						event: Message,
						data: Dict[str, Any]) -> Any:
		if event.from_user.id in admins:
			data["is_admin"] = True
		return await handler(event, data)
