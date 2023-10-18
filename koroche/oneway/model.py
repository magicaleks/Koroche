# %% Import dependencies
from enum import Enum
from typing import Dict, Optional

from koroche.model import BaseModel, ObjectModel


# %% Enums
class WayLifetime(int, Enum):
    Permanent = 0
    Day = 1
    ThreeDays = 3
    Week = 7
    Month = 30


# %% Models
class TargetUrl(ObjectModel):
    """Target url model"""

    is_secured: bool
    domain: str
    path: str
    params: Dict[str, str]

    def to_str(self) -> str:
        return self.domain + self.path + "?" + "&".join([k + "=" + v for k, v in self.params.items()])


class OneWay(BaseModel):
    """Shortened link model"""

    _collection_name = "oneways"

    name: str
    target: TargetUrl
    alias: str
    is_temporary: bool
    lifetime: WayLifetime
    user_uid: Optional[str]


class Redirect(BaseModel):
    """Redirect model"""

    _collection_name = "redirects"

    ip: Optional[str]
    oneway_uid: str
