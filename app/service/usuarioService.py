import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
import requests
from settings import API_TOKEN_IUGU, URL_API_IUGU_CUSTOMERS
from app.model.usuarioModel import UsuarioModel
from app.data.usuarioData import CadastraUsuario, CadastraProfissional, CadastraEmpresa, BuscarUsuarioData, BuscarProfissionalData, BuscarEmpresaData, AtualizaIdUsuarioIugu
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
        response.idUsuarioIugu = CadastraUsuarioIugu(response, 2)
        #cadastra usuario na iugu
        AtualizaIdUsuarioIugu(response.idUsuarioIugu, response.idUsuario)
        return response
    else:
       eEntity = UsuarioFactory.EmpresaModelToEntity(User)
       #TODO: SALVAR NO BANCO O EMPRESA TRATADA
       response = CadastraEmpresa(eEntity,IdPerfil)
       CadastraUsuarioIugu(response, 3)
       return response

def BuscaUsuarioService(idUsuario, IdPerfil):
      if IdPerfil == 1:
        return BuscarUsuarioData(idUsuario)
      elif IdPerfil == 2:
        return BuscarProfissionalData(idUsuario)
      else:
       return BuscarEmpresaData(idUsuario)

def CadastraUsuarioIugu(response, IdPerfil):
  querystring = {"api_token":API_TOKEN_IUGU}

  tel1 = response.Telefone[3:11]
  tel2 = response.Telefone[0:2]
  Documento = ''
  tipoUsuario = ''

  if IdPerfil == 2:
    Documento =  response.Cpf   
    tipoUsuario = 'Profissional'
  elif IdPerfil == 3:
    Documento = response.Cnpj
    tipoUsuario = 'Empresa'

  payload = {
      "email":response.Email,
      "name": response.Nome,
      "notes": "Eu sou um(a) " + tipoUsuario,
      "cpf_cnpj": Documento
  }

  headers = {"Content-Type": "application/json"}
  response = requests.request("POST", URL_API_IUGU_CUSTOMERS, json=payload, headers=headers, params=querystring)
  print(response.text)
  
  return response.json()['id']


