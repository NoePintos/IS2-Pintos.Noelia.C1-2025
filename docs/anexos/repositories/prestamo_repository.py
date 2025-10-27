from app.db.config import SessionLocal
from app.db.models.prestamo_model import PrestamoModel
from datetime import date

class PrestamoRepository:
    """Repositorio SQLAlchemy para la tabla 'prestamos'."""

    def __init__(self):
        self.db = SessionLocal()

    def add(self, prestamo: PrestamoModel):
        self.db.add(prestamo)
        self.db.commit()
        self.db.refresh(prestamo)
        return prestamo

    def get(self, id_prestamo: int):
        return self.db.query(PrestamoModel).filter(PrestamoModel.id_prestamo == id_prestamo).first()

    def all(self):
        return self.db.query(PrestamoModel).all()

    def marcar_devolucion(self, id_prestamo: int):
        """Marca un préstamo como devuelto."""
        prestamo = self.get(id_prestamo)
        if prestamo:
            prestamo.fecha_devolucion = date.today()
            self.db.commit()
            self.db.refresh(prestamo)
            return prestamo
        return None
