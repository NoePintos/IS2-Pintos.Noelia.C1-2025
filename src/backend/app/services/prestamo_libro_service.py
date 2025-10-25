from datetime import date
from app.db.connection import DBConnection
from app.repositories.socio_repository import SocioRepository
from app.repositories.ejemplar_repository import EjemplarRepository
from app.repositories.prestamo_repository import PrestamoRepository
from app.domain.prestamo import Prestamo

class PrestamoLibroService:
    def __init__(self, db: DBConnection, socio_repo: SocioRepository,
                 ejemplar_repo: EjemplarRepository, prestamo_repo: PrestamoRepository):
        self.db = db
        self.socio_repo = socio_repo
        self.ejemplar_repo = ejemplar_repo
        self.prestamo_repo = prestamo_repo
        self._seq = 1  # contador simple para IDs de préstamo

    def ejecutar(self, socio_id: int, ejemplar_id: int) -> Prestamo:
        self.db.connect()
        socio = self.socio_repo.get(socio_id)
        ej = self.ejemplar_repo.get(ejemplar_id)
        if not socio:
            raise ValueError("Socio inexistente")
        if not ej:
            raise ValueError("Ejemplar inexistente")
        if not ej.disponible:
            raise ValueError("Ejemplar no disponible")

        prestamo = Prestamo(self._seq, socio_id, ejemplar_id, date.today())
        self._seq += 1

        ej.disponible = False
        socio.prestamos.append(prestamo)
        self.prestamo_repo.add(prestamo.id_prestamo, prestamo)
        return prestamo