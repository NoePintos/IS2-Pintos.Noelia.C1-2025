from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class Libro:
    isbn: str
    titulo: str
    autor: str
    ejemplares: List["Ejemplar"] = field(default_factory=list)