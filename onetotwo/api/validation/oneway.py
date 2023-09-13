from typing import Any, Optional

from onetotwo.oneway.model import WayLifetime
from pydantic import BaseModel


class CreateOneWay(BaseModel):
    """CreateOneWay validate model"""

    name: str
    target: str
    is_temporary: bool
    lifetime: WayLifetime
    user_uid: Optional[str]
    only_numbers: bool


class UpdateOneWay(BaseModel):
    """UpdateOneWay validate model"""

    uid: str
    update: dict[str, Any]


class DeleteOneWay(BaseModel):
    """DeleteOneWay validate model"""

    uid: str
