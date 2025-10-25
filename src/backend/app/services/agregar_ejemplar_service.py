from app.db.connection import DBConnection
from app.repositories.libro_repository import LibroRepository
from app.repositories.ejemplar_repository import EjemplarRepository
from app.domain.ejemplar import Ejemplar

class AgregarEjemplarService:
    def __init__(self, db: DBConnection, libro_repo: LibroRepository, ejemplar_repo: EjemplarRepository):
        self.db = db
        self.libro_repo = libro_repo
        self.ejemplar_repo = ejemplar_repo

    def ejecutar(self, id_ejemplar: int, isbn: str) -> Ejemplar:
        self.db.connect()
        libro = self.libro_repo.get(isbn)
        if not libro:
            raise ValueError("Libro inexistente")
        if self.ejemplar_repo.get(id_ejemplar):
            raise ValueError("Id de ejemplar ya existe")
        ej = Ejemplar(id_ejemplar, isbn, True)
        self.ejemplar_repo.add(id_ejemplar, ej)
        libro.ejemplares.append(ej)
        return ej