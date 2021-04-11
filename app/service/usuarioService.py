import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
from app.model.usuarioModel import UsuarioModel
from app.data.usuarioData import CadastraUsuario, CadastraProfissional, CadastraEmpresa
from app.factory.clienteFactory import UsuarioFactory

def CadastrarUsuario(IdPerfil, User: UsuarioModel):
    if IdPerfil is 1:
        uEntity = UsuarioFactory.UsuarioModelToEntity(User)
        #TODO: SALVAR NO BANCO O USUARIO TRATADO
        return uEntity
    elif IdPerfil is 2:
        pEntity = UsuarioFactory.ProfissionalModelToEntity(User)
          #TODO: SALVAR NO BANCO O PROFISSIONAL TRATADA
        return eEntity
    else:
       eEntity = UsuarioFactory.EmpresaModelToEntity(User)
       #TODO: SALVAR NO BANCO O EMPRESA TRATADA
       return eEntity