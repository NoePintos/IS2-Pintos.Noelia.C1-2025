from sqlalchemy import create_engine
from app.db.config import DATABASE_URL, SessionLocal

# Crea el engine (motor de conexión a la base de datos)
engine = create_engine(DATABASE_URL, echo=False)

def get_session():
    """Crea una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()