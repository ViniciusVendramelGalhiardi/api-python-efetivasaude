
from fastapi import APIRouter, FastAPI, HTTPException, Request, Response, Depends, status 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json   
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from app.model.formadePagamentoiugu import FormaDePagamentoIugu
from app.service.pagamentoService import CriarFormaPagamentoService, BuscarFormasPagamentoService, EfetuarPagamentoService, CriarSubContaService,BuscarSubContaService, EnviaVerificacaoSubConta
from app.model.requestPagamentoModel import RequestPagamentoModel
from app.model.subContaRequestModel import SubContaRequestModel

router_pgto = APIRouter(
    prefix="/pgtoIugu",
    tags=["pgtoIugu"]
)


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

@router_pgto.post("/Efetuarpagamento/")
async def pagar(formapgto: RequestPagamentoModel):
    response = EfetuarPagamentoService(formapgto)
    return response

@router_pgto.post("/CriarSubConta/")
async def NovaSubConta(dadossubconta: SubContaRequestModel):
    response = CriarSubContaService(dadossubconta)
    return response

@router_pgto.get("/BuscarSubContaUsuario/{idUsuarioIugu}")
def BuscarSubConta(idUsuarioIugu: str):
    try:
      return  BuscarSubContaService(idUsuarioIugu)
    except Exception as mensagemErro: 
            return mensagemErro  

    
@router_pgto.get("/EnviaVerificacaoConta/{idUsuario}/{IdSubConta}/{TokenSubContaPrd}/{IdPerfil}")
def EnviaVerificacaoContaParaIugu(idUsuario: int, IdSubConta: str, TokenSubContaPrd: str, IdPerfil: int):
    try:
      return  EnviaVerificacaoSubConta(idUsuario,IdSubConta, TokenSubContaPrd,IdPerfil)
    except Exception as mensagemErro: 
            return mensagemErro    

