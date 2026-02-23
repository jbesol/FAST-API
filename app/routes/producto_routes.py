from fastapi import APIRouter, HTTPException
from controllers.producto_controller import *
from models.producto_model import Producto

router = APIRouter()

nuevo_producto = ProductoController()


@router.post("/create_producto")
async def create_producto(producto: Producto):
    rpta = nuevo_producto.create_producto(producto)
    return rpta


@router.get("/get_producto/{producto_id}",response_model=Producto)
async def get_producto(producto_id: int):
    rpta = nuevo_producto.get_producto(producto_id)
    return rpta

@router.get("/get_productos/")
async def get_productos():
    rpta = nuevo_producto.get_productos()
    return rpta