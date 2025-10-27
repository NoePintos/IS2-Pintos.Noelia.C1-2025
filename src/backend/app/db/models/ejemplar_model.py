from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.config import Base

class EjemplarModel(Base):
    __tablename__ = "ejemplares"

    id_ejemplar = Column(Integer, primary_key=True, index=True)
    libro_isbn = Column(String, ForeignKey("libros.isbn"), nullable=False)
    disponible = Column(Boolean, default=True)