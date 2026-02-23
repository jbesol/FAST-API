from fastapi import APIRouter, HTTPException
from controllers.tipodocumento_controller import *
from models.tipodocumento_model import TipoDocumento

router = APIRouter()

nuevo_tipodocumento = TipoDocumentoController()


@router.post("/create_tipodocumento")
async def create_tipodocumento(tipodocumento: TipoDocumento):
    rpta = nuevo_tipodocumento.create_tipodocumento(tipodocumento)
    return rpta


@router.get("/get_tipodocumento/{tipodocumento_id}",response_model=TipoDocumento)
async def get_tipodocumento(tipodocumento_id: int):
    rpta = nuevo_tipodocumento.get_tipodocumento(tipodocumento_id)
    return rpta

@router.get("/get_tipodocumentos/")
async def get_tipodocumentos():
    rpta = nuevo_tipodocumento.get_tipodocumentos()
    return rpta