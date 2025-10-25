from app.db.connection import DBConnection
from app.repositories.socio_repository import SocioRepository
from app.domain.socio import Socio

class RegistrarSocioService:
    def __init__(self, db: DBConnection, socio_repo: SocioRepository):
        self.db = db
        self.socio_repo = socio_repo

    def ejecutar(self, id_socio: int, nombre: str, email: str) -> Socio:
        self.db.connect()
        if self.socio_repo.get(id_socio):
            raise ValueError(f"Ya existe el socio {id_socio}")
        socio = Socio(id_socio, nombre, email)
        self.socio_repo.add(id_socio, socio)
        return socio