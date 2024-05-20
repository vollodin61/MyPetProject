from aiogram import Dispatcher

# from bot.data.cfg import dp
from .default import def_router
from .custom import cust_router
from .admins import admin_router


def set_routers(dp: Dispatcher):
	# dp.include_router(admin_router)  # TODO включить, когда будут готовы админские команды
	dp.include_router(cust_router)
	dp.include_router(def_router)
