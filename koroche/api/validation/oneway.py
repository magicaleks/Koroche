from typing import Optional

from koroche.oneway.model import WayLifetime
from pydantic import BaseModel
from typing_extensions import deprecated


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


@deprecated("Delete method temporary deprecated")
class DeleteOneWay(BaseModel):
    """DeleteOneWay validate model"""

    uid: str
