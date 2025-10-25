from app.db.connection import DBConnection
from app.repositories.socio_repository import SocioRepository
from app.repositories.libro_repository import LibroRepository
from app.repositories.ejemplar_repository import EjemplarRepository
from app.repositories.prestamo_repository import PrestamoRepository

from app.services.registrar_socio_service import RegistrarSocioService
from app.services.registrar_libro_service import RegistrarLibroService
from app.services.agregar_ejemplar_service import AgregarEjemplarService
from app.services.prestamo_libro_service import PrestamoLibroService
from app.services.devolucion_service import DevolucionService

def demo():
    db = DBConnection()
    sr = SocioRepository(); lr = LibroRepository(); er = EjemplarRepository(); pr = PrestamoRepository()

    reg_socio = RegistrarSocioService(db, sr)
    reg_libro = RegistrarLibroService(db, lr)
    add_ejemplar = AgregarEjemplarService(db, lr, er)
    prestar = PrestamoLibroService(db, sr, er, pr)
    devolver = DevolucionService(db, sr, er, pr)

    socio = reg_socio.ejecutar(1, "Ana Pérez", "ana@ejemplo.com")
    libro = reg_libro.ejecutar("9788437604947", "Cien años de soledad", "G. G. Márquez")
    ej1 = add_ejemplar.ejecutar(100, libro.isbn)

    p = prestar.ejecutar(socio.id_socio, ej1.id_ejemplar)
    print("Prestado:", p)

    devolver.ejecutar(p.id_prestamo)
    print("Devuelto:", pr.get(p.id_prestamo))

if __name__ == "__main__":
    demo()
