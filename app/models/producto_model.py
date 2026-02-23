from pydantic import BaseModel

class Producto(BaseModel):
    id: int = None
    nombre: str
    codigo: str
    valor: int
    stock: int
