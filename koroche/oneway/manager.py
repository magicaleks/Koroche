# %% Import Dependencies
from typing import List, Optional

from koroche.applogger import AppLogger
from koroche.config import ConfigManager
from koroche.data import AppHttpClient
from koroche.manager import BaseApiManager
from koroche.oneway.model import OneWay, Redirect, WayLifetime


# %% Managers
class RedirectManager(BaseApiManager):
    """Redirect api manager"""

    @classmethod
    def init(cls, logger: AppLogger) -> None:
        NotImplemented()

    @classmethod
    def create(cls, ip: str, oneway_uid: str) -> Redirect:
        NotImplemented()

    @classmethod
    def get(cls, uid: str) -> Optional[Redirect]:
        NotImplemented()

    @classmethod
    def get_redirects(cls, oneway_uid: str) -> List[Redirect]:
        NotImplemented()

    @classmethod
    def delete_redirects(cls, oneway_uid: str) -> None:
        NotImplemented()


class OneWayManager(BaseApiManager):
    """OneWay api manager"""

    _redirect = RedirectManager

    @classmethod
    def init(cls, logger: AppLogger, client: AppHttpClient) -> None:
        base_url = f"{ConfigManager.api.base_api_url}/api/{ConfigManager.api.version}/oneways"
        super().init(logger, client, base_url)

    @classmethod
    def create(
        cls,
        target: str,
        is_temporary: bool,
        lifetime: WayLifetime,
        user_uid: Optional[str] = None,
        only_numbers: bool = False,
    ) -> OneWay:
        """Create OneWay model"""
        response = cls._post(
            "/create",
            data={
                "target": target,
                "is_temporary": is_temporary,
                "lifetime": lifetime,
                "user_uid": user_uid,
                "only_numbers": only_numbers,
            },
        )

        return OneWay.model_validate(response)

    @classmethod
    def update(
        cls,
        uid: str,
        alias: Optional[str],
    ) -> None:
        """Update OneWay model"""
        cls._post(
            "/update",
            data={
                "uid": uid,
                "update": {"alias": alias},
            },
        )

    @classmethod
    def delete(cls, uid: str) -> None:
        """Delete OneWay model"""
        cls._delete({"_id": uid})

        cls._redirect.delete_redirects(uid)
