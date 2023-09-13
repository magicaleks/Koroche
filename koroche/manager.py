# %% Import dependencies
from abc import ABC
from datetime import datetime
from typing import Any, Generic, Iterable, Optional, Type, TypeVar

from koroche.applogger import AppLogger
from koroche.config import ConfigManager
from koroche.model import MongoModel
from koroche.utils import make_uuid
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

T = TypeVar("T", bound=MongoModel)


# %% Manager
class MongoManager(Generic[T], ABC):
    """Base manager for MongoModels"""

    _model: Type[T]
    _client: MongoClient
    _db: Database
    _collection: Collection
    _logger: AppLogger

    @classmethod
    def init(cls, logger: AppLogger, model: Type[T]) -> None:
        """Init MongoManager"""

        cls._model = model

        cls._client = MongoClient(host=ConfigManager.mongo.uri)
        cls._db = cls._client.get_database(name=ConfigManager.mongo.database)
        cls._collection = cls._db.get_collection(cls._model._collection_name)
        cls._logger = logger

        cls._logger.info(f"{model.__name__} manager successfull started")

    @classmethod
    def _create(cls, **kwargs) -> T:
        """Create model"""

        kwargs["_id"] = make_uuid()
        kwargs["created_at"] = datetime.utcnow()

        model = cls._model(**kwargs)

        cls._collection.insert_one(model.to_dict())

        cls._logger.info(f'Created {cls._model.__name__} model with uid "{model.uid}"')

        return model

    @classmethod
    def _get_many(cls, filt: dict[str, Any], limit: int = 0) -> Iterable[T]:
        """Find models"""

        res: list[T] = []
        for doc in cls._collection.find(filt, limit=limit):
            res.append(cls._model(**doc))
        return res

    @classmethod
    def _get_one(cls, filt: dict[str, Any]) -> Optional[T]:
        """Find model"""
        res = cls._collection.find_one(filt)

        return cls._model(**res) if res else None

    @classmethod
    def _update(cls, filt: dict[str, Any], update: dict[str, Any]) -> None:
        """Update models"""
        cls._collection.update_many(filt, update)

    @classmethod
    def _delete(cls, filt: dict[str, Any]) -> None:
        """Delete models"""
        cls._collection.delete_many(filt)

        cls._logger.info(f'Deleted {cls._model.__name__} model(s) with filters "{str(filt)}"')
