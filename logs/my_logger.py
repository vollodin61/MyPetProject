from dataclasses import dataclass
from datetime import datetime
from loguru import logger
from icecream import ic


@dataclass(frozen=True)
class MyLogger:
	@staticmethod
	def get_logger():
		space = f"{'-' * 100}\n"
		FILENAMELINE = 'Error path = {name}'.rstrip('abcdefghijklmnopqrstuvwxyz') + ':{function}:{line}\n'
		MESSAGE = 'MESSAGE = {message}\n'
		logger.add('../logs/test_debug.log', format=f"{space}{FILENAMELINE}{MESSAGE}",
				   rotation='500 KB', compression='gz',serialize=False,
				   retention=2, diagnose=False, backtrace=False,
				   enqueue=True, catch=True, level='DEBUG')
		# logger.configure(levels='DEBUG',)
		return logger

	log_debug = get_logger().debug
	loguru_logger = get_logger()
	ice = ic
	ice.configureOutput(includeContext=True, prefix=datetime.now().strftime('%Y-%m-%d %H:%M:%S '))
