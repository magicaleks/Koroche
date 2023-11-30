# %% Import dependencies
from abc import ABC
from typing import Any, Dict

from koroche.applogger import AppLogger
from koroche.data import AppHttpClient


# %% Manager
class BaseApiManager(ABC):
    """Base api manager"""

    _http_client: AppHttpClient
    _base_url: str
    _logger: AppLogger

    @classmethod
    def init(cls, logger: AppLogger, client: AppHttpClient, base_url: str) -> None:
        """Init ApiManager"""

        cls._http_client = client
        cls._base_url = base_url
        cls._logger = logger

        cls._logger.info(f"{cls.__name__} api manager successfull started")

    @classmethod
    def _get(cls, path: str, params: Dict[str, Any] = {}, headers: Dict[str, str] = {}) -> Dict[Any, Any]:
        """Get request wrapping"""

        response = cls._http_client.get(cls._base_url + path, params, headers)

        return response

    @classmethod
    def _post(
        cls, path: str, data: Dict[str, Any] = {}, params: Dict[str, Any] = {}, headers: Dict[str, str] = {}
    ) -> Dict[Any, Any]:
        """Post request wrapping"""

        response = cls._http_client.post(cls._base_url + path, data, params, headers)

        return response
