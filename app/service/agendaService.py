import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
import requests
from settings import API_TOKEN_IUGU, URL_API_IUGU_CUSTOMERS
from app.model.agendamentoConsultaModel import AgendamentoConsultaModel
from app.data.agendaData import efetuaAgendamento, buscarAgendamentoProfissional, atualizarAgendamento, CadastraAvaliacaoEF, buscarAvaliacaoProfissional
from app.service.usuarioService import BuscaUsuarioService
from app.entity.profissionalEntity import ProfissionalEntity
from app.model.listaAgendamento import ListarAgendamentosProfissionalModel
from app.model.avaliacaoefModel import AvaliacaoEfModel
from app.model.listargendamentoModel import ListarAgendamentoModel
from app.data.usuarioData import BuscarExpedienteById


def efetuaAgendamentoService(agenda: AgendamentoConsultaModel):
    return efetuaAgendamento(agenda)


def listarAgendamentosProfissional(IdUsuarioProfissional: int):
    try:
        aglst = []
        agendametoList = buscarAgendamentoProfissional(IdUsuarioProfissional)
        
        # IdAgendamento: Optional[int]
        # Idexpediente: Optional[int]
        # IdUsuario: Optional[int]
        # IdUsuarioProfissional: Optional[int]
        # IdDependente: Optional[str] = 'NULL'
        # StatusPagamento: Optional[str]
        # IdTransacao: Optional[int]
        # statusAgendamento: Optional[int]
        # IDSessao: Optional[str]
    
        ag = ListarAgendamentoModel()
        for agenda in agendametoList:
            ag.IdAgendamento = agenda.IdAgendamento
            ag.IdExpediente = agenda.Idexpediente
            ag.IdTransacao = agenda.IdTransacao
            ag.StatusAgendamento = agenda.statusAgendamento
            ag.StatusPagamento = agenda.StatusPagamento
            ag.IdSessao = agenda.IDSessao
            # ag.TempoEstimado = agenda.TempoEstimado
            # ag.Preco = agenda.Preco
            # ag.IdUsuario = agenda.IdUsuario
            exp = BuscarExpedienteById(agenda.Idexpediente)
            
            ag.Data = exp[0].DataAtendimento
            ag.Hora = exp[0].HorarioStart
            
            ag.Profissional = BuscaUsuarioService(IdUsuarioProfissional, 2)
            ag.Paciente = BuscaUsuarioService(agenda.IdUsuario, 1)
            aglst.append(ag)

    except Exception as mensagemErro:
        return mensagemErro
    return aglst


def atualizaStatusService(IdAgenda: int, StatusAgendamento: str):
    return atualizarAgendamento(IdAgenda, StatusAgendamento)


def cadastraAvaliacaoService(av: AvaliacaoEfModel):
    return CadastraAvaliacaoEF(av)


def buscarAvaliacaoProfissionalService(IdProfissional: int):
    return buscarAvaliacaoProfissional(IdProfissional)
