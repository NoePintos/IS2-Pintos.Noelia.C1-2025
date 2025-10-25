from sqlalchemy import Column, String, Integer
from app.db.config import Base

class LibroModel(Base):
    __tablename__ = "libros"

    isbn = Column(String, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(120), nullable=False)