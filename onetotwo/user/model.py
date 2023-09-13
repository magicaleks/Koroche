# %% Import dependencies
from enum import Enum

from onetotwo.model import MongoModel


# %% Enums
class UserLocale(str, Enum):
    Rus = "ru"
    Eng = "en"


# %% Models
class User(MongoModel):
    """User model"""

    _collection_name = "users"

    name: str
    email: str
    password: str
    locale: UserLocale
    is_active: bool
