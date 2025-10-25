from dataclasses import dataclass

@dataclass
class Ejemplar:
    id_ejemplar: int
    libro_isbn: str
    disponible: bool = True