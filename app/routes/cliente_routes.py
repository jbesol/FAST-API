from fastapi import APIRouter, HTTPException
from controllers.cliente_controller import *
from models.cliente_model import Cliente

router = APIRouter()

nuevo_cliente = ClienteController()


@router.post("/create_cliente")
async def create_cliente(cliente: Cliente):
    rpta = nuevo_cliente.create_cliente(cliente)
    return rpta


@router.get("/get_cliente/{cliente_id}",response_model=Cliente)
async def get_cliente(cliente_id: int):
    rpta = nuevo_cliente.get_cliente(cliente_id)
    return rpta

@router.get("/get_clientes/")
async def get_clientes():
    rpta = nuevo_cliente.get_clientes()
    return rpta