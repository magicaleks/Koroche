# %% Import dependency
import inspect
from typing import Any, Dict

from onetotwo.model import ConfigModel
from yaml import full_load as yaml_load


# %% Models
class AppConfig(ConfigModel):
    """Config for FastAPI app"""

    _name = "app"
    version: str
    api_version: str
    debug: bool
    host: str
    port: int


class AppLoggerConfig(ConfigModel):
    """Config for app logger"""

    _name = "applog"
    log_format: str
    handlers: Dict[str, Any]
    level: str


class CacheConfig(ConfigModel):
    """Config for app cache"""

    _name = "cache"


class MongoConfig(ConfigModel):
    """Config for connection to MongoDb"""

    _name = "mongo"
    uri: str
    database: str


# %% Manager
class ConfigManager:
    """Config manager"""

    app: AppConfig
    applog: AppLoggerConfig
    # cache_config: CacheConfig
    mongo: MongoConfig

    @classmethod
    def load_config(cls, path: str) -> None:
        with open(path, "r") as f:
            config: Dict[str, Any] = yaml_load(f)

            config_classes = inspect.get_annotations(cls)

            for k in config.keys():
                setattr(cls, k, config_classes[k](**config[k]))
