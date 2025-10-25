from app.db.connection import DBConnection
from app.repositories.libro_repository import LibroRepository
from app.domain.libro import Libro

class RegistrarLibroService:
    def __init__(self, db: DBConnection, libro_repo: LibroRepository):
        self.db = db
        self.libro_repo = libro_repo

    def ejecutar(self, isbn: str, titulo: str, autor: str) -> Libro:
        self.db.connect()
        if self.libro_repo.get(isbn):
            raise ValueError(f"Ya existe el libro {isbn}")
        libro = Libro(isbn, titulo, autor)
        self.libro_repo.add(isbn, libro)
        return libro