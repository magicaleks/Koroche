from typing import Optional

from koroche.oneway.model import WayLifetime
from pydantic import BaseModel


class CreateOneWay(BaseModel):
    """CreateOneWay validate model"""

    target: str
    is_temporary: bool
    lifetime: WayLifetime
    user_uid: Optional[str]
    only_numbers: bool


class UpdateOneWay(BaseModel):
    """UpdateOneWay validate model"""

    uid: str
    alias: Optional[str]


class DeleteOneWay(BaseModel):
    """DeleteOneWay validate model"""

    uid: str
