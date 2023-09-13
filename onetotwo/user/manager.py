# %% Import Dependencies
from typing import Any, Optional, Type

from onetotwo.applogger import AppLogger
from onetotwo.exceptions import MissingRequiredArgument
from onetotwo.manager import MongoManager
from onetotwo.user.model import User, UserLocale


# %% Manager
class UserManager(MongoManager[User]):
    """User mongodb manager"""

    @classmethod
    def init(cls, logger: AppLogger, model: Type[User]) -> None:
        super().init(logger, model)

    @classmethod
    def create(cls, name: str, email: str, password: str, locale: UserLocale) -> User:
        """Create User model"""
        return cls._create(name=name, email=email, password=password, locale=locale, is_active=True)

    @classmethod
    def get(cls, *, uid: str = None, email: str = None) -> Optional[User]:
        """Get user model"""
        filt = {}

        if uid:
            filt = {"_id": uid}

        elif email:
            filt = {"email": email}

        else:
            raise MissingRequiredArgument()

        return cls._get_one(filt)

    @classmethod
    def update(cls, uid: str, update: dict[str, Any]) -> None:
        """Get user model"""
        cls._update({"_id": uid}, update)

    @classmethod
    def delete(cls, uid: str) -> None:
        """Delete user model"""
        cls._delete({"_id": uid})
