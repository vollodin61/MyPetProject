from functools import wraps

from bot.config.my_logger import MyLogger


def exception_handler(func):
	log_debug = MyLogger.log_debug
	ice = MyLogger.ice

	@wraps(func)
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Exception as err:
			log_debug(err)
			ice(func.__name__)

		return wrapper
