from typing import Any

from koroche.user.model import UserLocale
from pydantic import BaseModel


class CreateUser(BaseModel):
    """CreateUser validate model"""

    name: str
    email: str
    password: str
    locale: UserLocale


class UpdateUser(BaseModel):
    """UpdateUser validate model"""

    uid: str
    update: dict[str, Any]


class DeleteUser(BaseModel):
    """DeleteUser validate model"""

    uid: str
