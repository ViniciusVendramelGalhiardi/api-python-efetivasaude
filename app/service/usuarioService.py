import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
from app.model.usuarioModel import UsuarioModel
from app.data.usuarioData import CadastraUsuario, CadastraProfissional, CadastraEmpresa
from app.factory.clienteFactory import UsuarioFactory
from app.data.usuarioData import CadastraUsuario


def CadastrarUsuario(IdPerfil, User: UsuarioModel):
    if IdPerfil == 1:
        uEntity = UsuarioFactory.UsuarioModelToEntity(User)
        #TODO: SALVAR NO BANCO O USUARIO TRATADO
        response = CadastraUsuario(uEntity, IdPerfil)
        return response
    elif IdPerfil == 2:
        pEntity = UsuarioFactory.ProfissionalModelToEntity(User)
          #TODO: SALVAR NO BANCO O PROFISSIONAL TRATADA
        response = CadastraProfissional(pEntity,IdPerfil)
        return response
    else:
       eEntity = UsuarioFactory.EmpresaModelToEntity(User)
       #TODO: SALVAR NO BANCO O EMPRESA TRATADA
       response = CadastraEmpresa(eEntity,IdPerfil)
       return response