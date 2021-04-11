from fastapi import APIRouter, FastAPI, HTTPException, Request, Response, logger
from typing import Optional 
from pydantic import BaseModel  
import json
from app.model.response import getResponse
from app.service.ListagemService import listaPerfil, listaAbordagem, listaHobbies, listaCRP, listaHorarioTrabalho, listaIdiomas, listaNosConheceu, listaPlanos, listaProfissao, listaSintomas, listaUsarPlataforma
from app.model.usuarioModel import UsuarioModel
from fastapi.responses import JSONResponse
from app.service.usuarioService import CadastrarUsuario

router_web = APIRouter(
    prefix="/web",
    tags=["web"]
)

@router_web.post("/cadastrarUsuario/{IdPerfil}")
async def cadastrar(IdPerfil:int, UsuarioModel: UsuarioModel):
    response = CadastrarUsuario(IdPerfil, UsuarioModel)
    return response

@router_web.get("/ListarPerfis/")
def ListarPerfil():
    return listaPerfil()


@router_web.get("/ListarAbordagem/")
def ListaAbordagem():
    return listaAbordagem()


@router_web.get("/ListaHobbies/")
def ListaHobbies():
    return listaHobbies()


@router_web.get("/ListaCRP/")
def ListaCRP():
    return listaCRP()


@router_web.get("/ListaHorarioTrabalho/")
def ListaHorarioTrabalho():
    return listaHorarioTrabalho()


@router_web.get("/ListaIdiomas/")
def ListaIdiomas():
    return listaIdiomas()


@router_web.get("/ListaNosConheceu/")
def ListaNosConheceu():
    return listaNosConheceu()

@router_web.get("/ListaPlanos/")
def ListaPlanos():
    return listaPlanos()


@router_web.get("/ListaProfissao/")
def ListaProfissao():
    return listaProfissao()

@router_web.get("/ListaSintomas/")
def ListaSintomas():
    return listaSintomas()

@router_web.get("/ListaUsarPlataforma/")
def ListaUsarPlataforma():
    return listaUsarPlataforma()

# @router_web.get("/paymentmethods/{merchantAccount}", summary="Get Methods Web Payments")
# async def paymentMethods(merchantAccount: str): 
#     try:
#         response = adyen_payment_methods(merchantAccount)
#         return response
#     except Exception as e:
#         logger.debug(e)
#         return getResponse(400, "Request error.", "")          

# @router_web.post("/payment/", summary="Create new Payment Web")
# async def payment(paymentsWebModel: PaymentsWebModel):
#     try:
#         response = adyen_payments(paymentsWebModel)
#         return response
#     except Exception as e:
#         logger.debug(e)
#         return getResponse(400, "Request error.", "")          

# @router_web.post("/cancelorrefundpayment/", summary="Cancel Payment Web")
# async def payment(cancelPaymentsModel: CancelPaymentsModel):
#     try:
#         response = adyen_payment_cancel_refund(cancelPaymentsModel)
#         return response
#     except Exception as e:
#         logger.debug(e)
#         return getResponse(400, "Request error.", "")