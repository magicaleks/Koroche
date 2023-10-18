# %% Import Dependencies
from typing import Any, Optional, Type

from koroche.applogger import AppLogger
from koroche.exceptions import MissingRequiredArgument
from koroche.manager import BaseManager
from koroche.user.model import User, UserLocale


# %% Manager
class UserManager(BaseManager[User]):
    """User mongodb manager"""

    @classmethod
    def init(cls, logger: AppLogger, model: Type[User]) -> None:
        super().init(logger, model)

    @classmethod
    def create(cls, name: str, email: str, password: str, locale: UserLocale) -> User:
        """Create User model"""

    @classmethod
    def get(cls, *, uid: str = None, email: str = None) -> Optional[User]:
        """Get user model"""

    @classmethod
    def update(cls, uid: str, update: dict[str, Any]) -> None:
        """Get user model"""

    @classmethod
    def delete(cls, uid: str) -> None:
        """Delete user model"""
