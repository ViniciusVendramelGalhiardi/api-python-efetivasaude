import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
import requests
from settings import API_TOKEN_IUGU, URL_API_IUGU_CUSTOMERS
from app.model.agendamentoConsultaModel import AgendamentoConsultaModel
from app.data.agendaData import efetuaAgendamento, buscarAgendamentoProfissional, atualizarAgendamento, CadastraAvaliacaoEF,buscarAvaliacaoProfissional
from app.service.usuarioService import BuscaUsuarioService
from app.entity.profissionalEntity import ProfissionalEntity
from app.model.listaAgendamento import ListarAgendamentosProfissionalModel
from app.model.avaliacaoefModel import AvaliacaoEfModel


def efetuaAgendamentoService(agenda: AgendamentoConsultaModel):
    return efetuaAgendamento(agenda)

def listarAgendamentosProfissional(IdUsuario: int):
    ag = ListarAgendamentosProfissionalModel()
    ag.profissional = BuscaUsuarioService(IdUsuario, 2) # id 2 representa um profissional
    ag.Agendamentos = buscarAgendamentoProfissional(IdUsuario)
    return ag

def atualizaStatusService(IdAgenda:int , StatusAgendamento: str):
    return atualizarAgendamento(IdAgenda,StatusAgendamento)

def cadastraAvaliacaoService(av: AvaliacaoEfModel):
    return CadastraAvaliacaoEF(av)

def buscarAvaliacaoProfissionalService(IdProfissional: int):
    return buscarAvaliacaoProfissional(IdProfissional)
