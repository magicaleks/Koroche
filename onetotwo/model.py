# %% Import dependencies
from abc import ABC
from datetime import datetime

from pydantic import BaseModel, Field


# %% Base models
class _Model(BaseModel, ABC):
    """Base Model"""

    model_config = {
        "extra": "ignore",
        "ignored_types": (
            str,
            int,
        ),
    }


class MongoModel(_Model, ABC):
    """Model for storing in Mongo"""

    _collection_name: str

    uid: str = Field(alias="_id")
    created_at: datetime

    def to_dict(self) -> dict:
        """Return dict representation of model"""
        return self.model_dump(mode="json", by_alias=True)


class ObjectModel(_Model, ABC):
    """Model for object field in Mongo"""

    pass


class ConfigModel(_Model, ABC):
    """Base config model"""

    _name: str
