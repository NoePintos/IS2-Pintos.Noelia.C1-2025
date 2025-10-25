from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class Socio:
    id_socio: int
    nombre: str
    email: str
    prestamos: List["Prestamo"] = field(default_factory=list)