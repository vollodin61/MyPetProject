from redis.asyncio.client import Redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError

from src.database.sql.config.db_config import Settings

RETRY = 3
TIMEOUT = 2


class Singleton:
	_instance = None

	@staticmethod
	def get_connection(host: str):
		if not Singleton._instance:
			Singleton._instance = Redis(host=host, port=int(Settings.REDIS_PORT), socket_timeout=TIMEOUT,  # здесь тоже порты прокидывать из вирт округи
										retry=Retry(ExponentialBackoff(), RETRY),
										retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError])
		return Singleton._instance
