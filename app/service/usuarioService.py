from math import e, trunc
import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
import requests
from settings import API_TOKEN_IUGU, URL_API_IUGU_CUSTOMERS
from app.model.usuarioModel import UsuarioModel
from app.data.usuarioData import CadastraUsuario, CadastraProfissional, CadastraEmpresa, BuscarUsuarioData, BuscarProfissionalData, BuscarEmpresaData, AtualizaIdUsuarioIugu, CadastraExpProfissional, BuscarExpedienteProfissional, VincularSintomaProfissional, BuscarSintomaPorUsuarioData, CadastrarCartao, BuscarCartaoUsuarioData, ExcluirCartao, CadastraExperiencia, AtualizaExperiencia, ExcluirExperiencia, CadastraFormacao, AtualizaFormacao, ExcluirFormacao, CadastraDependente, AtualizaDependente, ExcluirDependente
from app.factory.clienteFactory import UsuarioFactory
from app.data.usuarioData import CadastraUsuario
from app.model.usuarioVinculadoSubConta import UsuarioVinculadoSubConta
from app.model.expedienteProfissionalModel import ExpedienteProfissionalModel
from app.model.sintomasVinculadosModel import SintomasVinculadosModel
from random import randrange
import os
from twilio.rest import Client
from app.model.returdefaultValue import DefaultValueModel
from app.model.experienciaPraticaModel import ExperienciaPraticaModel


def CadastrarUsuario(IdPerfil, User: UsuarioModel):
    if IdPerfil == 1:
        uEntity = UsuarioFactory.UsuarioModelToEntity(User)
        # TODO: SALVAR NO BANCO O USUARIO TRATADO
        response = CadastraUsuario(uEntity, IdPerfil)
        response.IdUsuarioIugu = CadastraUsuarioIugu(response, 2)
        # cadastra usuario na iugu
        AtualizaIdUsuarioIugu(response.IdUsuarioIugu, response.idUsuario)
        return response
    elif IdPerfil == 2:
        pEntity = UsuarioFactory.ProfissionalModelToEntity(User)
        # TODO: SALVAR NO BANCO O PROFISSIONAL TRATADA
        response = CadastraProfissional(pEntity, IdPerfil)
        response.idUsuarioIugu = CadastraUsuarioIugu(response, 2)
        # cadastra usuario na iugu
        AtualizaIdUsuarioIugu(response.idUsuarioIugu, response.idUsuario)
        return response
    else:
        eEntity = UsuarioFactory.EmpresaModelToEntity(User)
        # TODO: SALVAR NO BANCO O EMPRESA TRATADA
        response = CadastraEmpresa(eEntity, IdPerfil)
        response.idUsuarioIugu = CadastraUsuarioIugu(response, 3)
        AtualizaIdUsuarioIugu(response.idUsuarioIugu, response.idUsuario)
        response.idUsuario = IdPerfil
        return response


def VincularUsuarioSubConta(IdUsuario: int, IdPerfil: int, TokenSubContaPrd: str):
    user = BuscaUsuarioService(IdUsuario, IdPerfil)
    IdUsuarioVinculado = CadastraUsuarioSubConta(
        user, IdPerfil, TokenSubContaPrd)
    ret = UsuarioVinculadoSubConta(IdUsuarioVinculado, user.IdUsuarioIugu)
    return ret


def BuscaUsuarioService(idUsuario, IdPerfil):
    if IdPerfil == 1:
        return BuscarUsuarioData(idUsuario)
    elif IdPerfil == 2:
        return BuscarProfissionalData(idUsuario)
    else:
        return BuscarEmpresaData(idUsuario)


def CadastraUsuarioIugu(response, IdPerfil):
    querystring = {"api_token": API_TOKEN_IUGU}

    tel1 = response.Telefone[3:11]
    tel2 = response.Telefone[0:2]
    Documento = ''
    tipoUsuario = ''

    if IdPerfil == 2:
        Documento = response.Cpf
        tipoUsuario = 'Profissional'
    elif IdPerfil == 3:
        Documento = response.Cnpj
        tipoUsuario = 'Empresa'

    payload = {
        "email": response.Email,
        "name": response.Nome,
        "notes": "Eu sou um(a) " + tipoUsuario,
        "cpf_cnpj": Documento
    }

    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", URL_API_IUGU_CUSTOMERS, json=payload, headers=headers, params=querystring)
    print(response.text)

    return response.json()['id']


def CadastraUsuarioSubConta(usuario, IdPerfil, TokenSubContaPrd):
    querystring = {"api_token": TokenSubContaPrd}

    tel1 = usuario.Telefone[3:11]
    tel2 = usuario.Telefone[0:2]
    Documento = ''
    tipoUsuario = ''

    if IdPerfil == 1 or IdPerfil == 2:
        Documento = usuario.Cpf
        if IdPerfil == 1:
            tipoUsuario = 'Paciente'
        elif IdPerfil == 2:
            tipoUsuario = 'Profissional'
    elif IdPerfil == 3:
        Documento = usuario.Cnpj
        tipoUsuario = 'Empresa'

    payload = {
        "email": usuario.Email,
        "name": usuario.Nome,
        "notes": "Eu sou um(a) " + tipoUsuario,
        "cpf_cnpj": Documento
    }

    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", URL_API_IUGU_CUSTOMERS, json=payload, headers=headers, params=querystring)
    print(response.text)
    return response.json()['id']


def CadastraExpedienteProfissional(expediente: ExpedienteProfissionalModel):
    return CadastraExpProfissional(expediente)


def ListarExpedienteProfissional(IdProfissional: int,  Status: str, DataAtendimento: str, IdExpediente: str):
    return BuscarExpedienteProfissional(IdProfissional, Status, DataAtendimento, IdExpediente)


def VincularSintomaProfissionalService(sintomas):
    if (VincularSintomaProfissional(sintomas)):
        return '{msg:"Sucesso"}'
    else:
        return '{msg:"Error"}'


def BuscarSintomaPorUsuarioDataService(idUsuario: int):
    return BuscarSintomaPorUsuarioData(idUsuario)


def CadastrarCartaoService(card):
    if (CadastrarCartao(card)):
        return '{msg:"Sucesso"}'
    else:
        return '{msg:"Error"}'


def BuscarCartaoUsuarioService(idUsuario: int):
    return BuscarCartaoUsuarioData(idUsuario)


def ExcluirCartaoService(idUsuario: int):
    if (ExcluirCartao(idUsuario)):
        return '{msg:"Sucesso"}'
    else:
        return '{msg:"Error"}'


def EnviarSmsUsuarioService(Numero: str, nome: str):
    try:
        number = randrange(5000)
        account_sid = "AC02f71138043bb8e7abe86c5f927494ea"
        auth_token = "c8a9fa953e68107ff2eead132e66f1c8"

        client = Client(account_sid, auth_token)

        mess = client.messages \
            .create(
                body="Olá, " + nome + " confirme o código: '" +
                str(number)+"' em seu cadastro.",
                from_='+18317099856',
                to='+55' + Numero.replace('.', '').replace('-', '')
            )

    except Exception as mensagemErro:
        return mensagemErro

    ret = DefaultValueModel()
    ret.value = str(number)
    return ret


def CadastraDependenteService(dep):
    return CadastraDependente(dep)


def AtualizaDependenteService(id, dep):
    return AtualizaDependente(id, dep)


def ExcluirDependenteService(id):
    return ExcluirDependente(id)


def CadastraExperienciaService(experiencia):
    return CadastraExperiencia(experiencia)


def AtualizaExperienciaService(id, experiencia):
    return AtualizaExperiencia(id, experiencia)


def ExcluirExperienciaService(id):
    return ExcluirExperiencia(id)


def CadastraFormacaoService(formacao):
    return CadastraFormacao(formacao)


def AtualizaFormacaoService(id, formacao):
    return AtualizaFormacao(id, formacao)


def ExcluirFormacaoService(id):
    return ExcluirFormacao(id)
