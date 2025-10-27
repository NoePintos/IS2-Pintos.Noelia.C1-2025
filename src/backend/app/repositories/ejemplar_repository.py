from app.db.config import SessionLocal
from app.db.models.ejemplar_model import EjemplarModel

class EjemplarRepository:
    """Repositorio SQLAlchemy para la tabla 'ejemplares'."""

    def __init__(self):
        self.db = SessionLocal()

    def add(self, ejemplar: EjemplarModel):
        self.db.add(ejemplar)
        self.db.commit()
        self.db.refresh(ejemplar)
        return ejemplar

    def get(self, id_ejemplar: int):
        return self.db.query(EjemplarModel).filter(EjemplarModel.id_ejemplar == id_ejemplar).first()

    def all(self):
        return self.db.query(EjemplarModel).all()

    def remove(self, id_ejemplar: int):
        ejemplar = self.get(id_ejemplar)
        if ejemplar:
            self.db.delete(ejemplar)
            self.db.commit()
