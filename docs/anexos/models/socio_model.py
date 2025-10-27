from sqlalchemy import Column, Integer, String
from app.db.config import Base

class SocioModel(Base):
    __tablename__ = "socios"

    id_socio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)