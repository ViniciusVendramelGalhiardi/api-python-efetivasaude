
from fastapi import APIRouter, FastAPI, HTTPException, Request, Response, Depends, status 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json   
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from app.model.formadePagamentoiugu import FormaDePagamentoIugu
from app.service.pagamentoService import CriarFormaPagamentoService, BuscarFormasPagamentoService

router_pgto = APIRouter(
    prefix="/pgtoIugu",
    tags=["pgtoIugu"]
)

#debito e credito a vista
@router_pgto.post("/criarformaPagamento/")
async def cadastrarCartao(formapgto: FormaDePagamentoIugu):
    response = CriarFormaPagamentoService(formapgto)
    return response


@router_pgto.get("/BuscarFormaPagto/{idUsuarioIugu}")
def BuscarFormaPagto(idUsuarioIugu: str):
    try:
      return  BuscarFormasPagamentoService(idUsuarioIugu)
    except Exception as mensagemErro: 
            return mensagemErro    