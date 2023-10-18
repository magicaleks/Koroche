# %% Import dependencies
from abc import ABC
from datetime import datetime

import pydantic as pdc


# %% Base models
class _Model(pdc.BaseModel, ABC):
    """Base Model"""

    model_config = {
        "extra": "ignore",
        "ignored_types": (
            str,
            int,
        ),
    }


class BaseModel(_Model, ABC):
    """Base data model"""

    _collection_name: str

    uid: str = pdc.Field(alias="_id")
    created_at: datetime

    def to_dict(self) -> dict:
        """Return dict representation of model"""
        return self.model_dump(mode="json", by_alias=True)


class ObjectModel(_Model, ABC):
    """Field object model"""

    pass


class ConfigModel(_Model, ABC):
    """Base config model"""

    _name: str
