from typing import Any, Dict

import backoff
import httpx
from koroche.applogger import AppLogger
from koroche.config import ConfigManager
from koroche.exceptions import RetryPolicyException


class AppCache:
    """For the future"""


class AppHttpClient:
    """Http client"""

    def __init__(self, logger: AppLogger) -> None:
        self._logger = logger

    def get(self, url: str, params: Dict[str, Any] = {}, headers: Dict[str, str] = {}) -> Dict[Any, Any]:
        """Get request method"""

        self._logger.info(f"Requesting GET url: {url}")

        @backoff.on_exception(
            exception=RetryPolicyException, wait_gen=backoff.expo, max_tries=ConfigManager.net.backoff.max_tries_n
        )
        def _get(
            url,
            params,
            headers,
        ):
            response = httpx.get(url, params=params, headers=headers)

            if response.status_code in ConfigManager.net.backoff.code_forcelist:
                raise RetryPolicyException(url, response.status_code)

            if response.is_error:
                self._logger.warning(f"Response content: {response.json()}")
                response.raise_for_status()

            return response.json()

        return _get(url, params, headers)

    def post(
        self, url: str, data: Dict[str, Any] = {}, params: Dict[str, Any] = {}, headers: Dict[str, str] = {}
    ) -> Dict[Any, Any]:
        """Post request method"""

        self._logger.info(f"Requesting GET url: {url}")

        @backoff.on_exception(
            exception=RetryPolicyException, wait_gen=backoff.expo, max_tries=ConfigManager.net.backoff.max_tries_n
        )
        def _post(url, data, params, headers):
            response = httpx.post(url, json=data, params=params, headers=headers)

            if response.status_code in ConfigManager.net.backoff.code_forcelist:
                raise RetryPolicyException(url, response.status_code)

            if response.is_error:
                self._logger.warning(f"Response content: {response.json()}")
                response.raise_for_status()

            return response.json()

        return _post(url, data, params, headers)
