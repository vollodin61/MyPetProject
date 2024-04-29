from .antispam_middleware import Antispam
from .scheduler_middleware import SchedulerMiddleware

from bots.sarbot.bot.data.bot_cfg import red_storage, scheduler


def set_middleware(dp):
	# dp.update.outer_middleware.register(CheckRoleMiddleware(6558982323))
	dp.update.middleware.register(SchedulerMiddleware(scheduler=scheduler))
	dp.message.middleware.register(Antispam(storage=red_storage))
