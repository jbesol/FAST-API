from pydantic import BaseModel

class Cliente(BaseModel):
    id: int = None
    nombre: str
    apellido: str
    idtipodoc: int
    documento: str
    direccion: str
    correo: str