from app.db.config import SessionLocal
from app.db.models.libro_model import LibroModel

class LibroRepository:
    """Repositorio SQLAlchemy para la tabla 'libros'."""

    def __init__(self):
        self.db = SessionLocal()

    def add(self, libro: LibroModel):
        """Agrega un nuevo libro."""
        self.db.add(libro)
        self.db.commit()
        self.db.refresh(libro)
        return libro

    def get(self, isbn: str):
        """Busca un libro por su ISBN."""
        return self.db.query(LibroModel).filter(LibroModel.isbn == isbn).first()

    def all(self):
        """Devuelve todos los libros."""
        return self.db.query(LibroModel).all()

    def remove(self, isbn: str):
        """Elimina un libro por su ISBN."""
        libro = self.get(isbn)
        if libro:
            self.db.delete(libro)
            self.db.commit()