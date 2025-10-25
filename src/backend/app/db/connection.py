from app.utils.singleton import SingletonMeta

class DBConnection(metaclass=SingletonMeta):
    """Simula una conexión a base de datos (en memoria)."""
    def __init__(self):
        self.connected = False

    def connect(self):
        if not self.connected:
            self.connected = True
            print("DB: conexión establecida (in-memory).")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print("DB: conexión cerrada.")