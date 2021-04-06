import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
from app.data.perfisData import buscaPerfis, buscaAbordagem, buscaHobbie, buscaCRP, buscaHorarioTrabalho, buscaIdiomas, buscaNosConheceu, buscaPlanos, buscaProfissao, buscaSintomas, buscaUsarPlataforma 
from app.model.usuarioModel import UsuarioModel


def CadastrarUsuario(request: UsuarioModel):
    return ''


def listaPerfil():
    return buscaPerfis()

def listaAbordagem():
    return buscaAbordagem()

def listaHobbies():
    return buscaHobbie()


def listaCRP():
    return buscaCRP()

def listaHorarioTrabalho():
    return buscaHorarioTrabalho()

def listaIdiomas():
    return buscaIdiomas()

def listaNosConheceu():
    return buscaNosConheceu()

def listaPlanos():
    return buscaPlanos()

def listaProfissao():
    return buscaProfissao()

def listaSintomas():
    return buscaSintomas()


def listaUsarPlataforma():
    return buscaUsarPlataforma()