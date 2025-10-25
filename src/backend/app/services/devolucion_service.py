from app.db.connection import DBConnection
from app.repositories.socio_repository import SocioRepository
from app.repositories.ejemplar_repository import EjemplarRepository
from app.repositories.prestamo_repository import PrestamoRepository

class DevolucionService:
    def __init__(self, db: DBConnection, socio_repo: SocioRepository,
                 ejemplar_repo: EjemplarRepository, prestamo_repo: PrestamoRepository):
        self.db = db
        self.socio_repo = socio_repo
        self.ejemplar_repo = ejemplar_repo
        self.prestamo_repo = prestamo_repo

    def ejecutar(self, id_prestamo: int):
        self.db.connect()
        prestamo = self.prestamo_repo.get(id_prestamo)
        if not prestamo:
            raise ValueError("Préstamo inexistente")

        ej = self.ejemplar_repo.get(prestamo.ejemplar_id)
        socio = self.socio_repo.get(prestamo.socio_id)
        if not ej or not socio:
            raise RuntimeError("Datos inconsistentes")

        if prestamo.fecha_devolucion:
            raise ValueError("El préstamo ya fue devuelto")

        prestamo.devolver()
        ej.disponible = True
        return prestamo
