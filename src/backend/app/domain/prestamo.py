from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Prestamo:
    id_prestamo: int
    socio_id: int
    ejemplar_id: int
    fecha_prestamo: date
    fecha_devolucion: Optional[date] = None

    def devolver(self):
        from datetime import date as _date
        self.fecha_devolucion = _date.today()
