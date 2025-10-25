from app.db.config import SessionLocal

def get_session():
    """Crea una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()