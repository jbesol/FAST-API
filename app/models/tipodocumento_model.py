from pydantic import BaseModel

class TipoDocumento(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    