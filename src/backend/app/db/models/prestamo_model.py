from sqlalchemy import Column, Integer, Date, ForeignKey
from app.db.config import Base

class PrestamoModel(Base):
    __tablename__ = "prestamos"

    id_prestamo = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey("socios.id_socio"), nullable=False)
    ejemplar_id = Column(Integer, ForeignKey("ejemplares.id_ejemplar"), nullable=False)
    fecha_prestamo = Column(Date, nullable=False)
    fecha_devolucion = Column(Date, nullable=True)