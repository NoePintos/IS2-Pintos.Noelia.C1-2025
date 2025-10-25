from typing import Dict
import threading

class SingletonMeta(type):
    """
    Metaclase Singleton:
    Asegura que cada clase que la use solo tenga una instancia en memoria.
    Por ejemplo, se usa para la conexión a la base de datos o repositorios únicos.
    """
    _instances: Dict[type, object] = {}
    _lock: threading.Lock = threading.Lock()  # Bloqueo para uso seguro en entornos con hilos

    def __call__(cls, *args, **kwargs):
        # Si la clase aún no tiene una instancia, la crea
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        # Retorna siempre la misma instancia
        return cls._instances[cls]