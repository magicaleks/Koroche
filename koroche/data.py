from koroche.applogger import AppLogger


class AppCache:
    """For the future"""


class AppHttpClient:
    """Http client"""

    def __init__(self, logger: AppLogger) -> None:
        self._logger = logger


class BaseApiClient:
    """Base api client"""

    def __init__(self, logger: AppLogger, http_client: AppHttpClient) -> None:
        self._logger = logger
        self._client = http_client
