from app.db.config import SessionLocal
from app.db.models.socio_model import SocioModel

class SocioRepository:
    """Repositorio SQLAlchemy para la tabla 'socios'."""

    def __init__(self):
        self.db = SessionLocal()

    def add(self, socio: SocioModel):
        """Agrega un nuevo socio a la base de datos."""
        self.db.add(socio)
        self.db.commit()
        self.db.refresh(socio)
        return socio

    def get(self, id_socio: int):
        """Obtiene un socio por su ID."""
        return self.db.query(SocioModel).filter(SocioModel.id_socio == id_socio).first()

    def all(self):
        """Devuelve todos los socios."""
        return self.db.query(SocioModel).all()

    def remove(self, id_socio: int):
        """Elimina un socio por su ID."""
        socio = self.get(id_socio)
        if socio:
            self.db.delete(socio)
            self.db.commit()
