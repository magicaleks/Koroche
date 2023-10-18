# %% Import dependencies
from enum import Enum

from koroche.model import BaseModel


# %% Enums
class UserLocale(str, Enum):
    Rus = "ru"
    Eng = "en"


# %% Models
class User(BaseModel):
    """User model"""

    name: str
    email: str
    password: str
    locale: UserLocale
    is_active: bool
