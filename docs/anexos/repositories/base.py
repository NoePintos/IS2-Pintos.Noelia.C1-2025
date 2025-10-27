from __future__ import annotations
from typing import Dict, Generic, List, Optional, TypeVar
from app.utils.singleton import SingletonMeta

T = TypeVar("T")

class Repository(Generic[T], metaclass=SingletonMeta):
    """Repo base in-memory. Cambiá métodos a DB real sin tocar servicios."""
    def __init__(self):
        self._data: Dict[object, T] = {}

    def add(self, key: object, entity: T) -> None:
        self._data[key] = entity

    def get(self, key: object) -> Optional[T]:
        return self._data.get(key)

    def remove(self, key: object) -> None:
        self._data.pop(key, None)

    def all(self) -> List[T]:
        return list(self._data.values())