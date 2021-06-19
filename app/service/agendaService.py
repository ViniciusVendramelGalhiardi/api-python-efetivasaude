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
from app.model.listargendamentoModel import ListarAgendamentoModel

def efetuaAgendamentoService(agenda: AgendamentoConsultaModel):
    return efetuaAgendamento(agenda)

def listarAgendamentosProfissional(IdUsuarioProfissional: int):
    agendametoList = buscarAgendamentoProfissional(IdUsuarioProfissional)

    ag = ListarAgendamentoModel()
    for agenda in agendametoList:
        ag.IdAgendamento = agenda.IdAgendamento
        print(ag.IdAgendamento)

    
    
    #ag.profissional = BuscaUsuarioService(IdUsuario, 2) # id 2 representa um profissional
    #ag.Agendamentos = 
    return ag

def atualizaStatusService(IdAgenda:int , StatusAgendamento: str):
    return atualizarAgendamento(IdAgenda,StatusAgendamento)

def cadastraAvaliacaoService(av: AvaliacaoEfModel):
    return CadastraAvaliacaoEF(av)

def buscarAvaliacaoProfissionalService(IdProfissional: int):
    return buscarAvaliacaoProfissional(IdProfissional)
