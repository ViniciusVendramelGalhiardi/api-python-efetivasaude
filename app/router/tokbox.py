from fastapi import APIRouter, FastAPI, HTTPException, Request, Response, logger
from typing import Optional 
from pydantic import BaseModel  
import json
from app.model.response import getResponse
from app.service.ListagemService import listaPerfil, listaAbordagem, listaHobbies, listaCRP, listaHorarioTrabalho, listaIdiomas, listaNosConheceu, listaPlanos, listaProfissao, listaSintomas, listaUsarPlataforma
from app.model.usuarioModel import UsuarioModel
from fastapi.responses import JSONResponse
from app.service.usuarioService import CadastrarUsuario, BuscaUsuarioService
from opentok.opentok import MediaModes, OpenTok, Roles
from settings import TOK_BOX_API_KEY, API_SECRET_TOK_BOX
from app.model.returdefaultValue import DefaultValueModel

router_tokbox = APIRouter(
    prefix="/tokbox",
    tags=["tokbox"]
)

@router_tokbox.get("/gerarSessao/")
async def geraSessaoTokBox():
    api_key = TOK_BOX_API_KEY 
    api_secret = API_SECRET_TOK_BOX 
    opentok_sdk = OpenTok(api_key, api_secret)
    session = opentok_sdk.create_session(media_mode=MediaModes.routed)
    ret = DefaultValueModel()
    ret.value = session.session_id
    return ret
     

@router_tokbox.get("/gerarTokenParaSessao/{session_id}")
async def gerarTokenChamada(session_id:str):
    api_key = TOK_BOX_API_KEY 
    api_secret = API_SECRET_TOK_BOX
    opentok_sdk = OpenTok(api_key, api_secret)
    token = opentok_sdk.generate_token(session_id)
    ret = DefaultValueModel()
    ret.value = token
    return ret