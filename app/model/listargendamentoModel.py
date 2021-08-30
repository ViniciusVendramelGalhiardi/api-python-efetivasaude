from __future__ import annotations
from typing import List
from pydantic import BaseModel
from typing import List, Optional


class Profissional(BaseModel):
    Id: Optional[int]
    Nome: Optional[str]
    Imagem: Optional[str]
    Profissao: Optional[str]
    Crp: Optional[str]


class Paciente(BaseModel):
    Id: Optional[int]
    Nome: Optional[str]
    Imagem: Optional[str]
    Cpf: Optional[str]
    DataNascimento: Optional[str]


class ListarAgendamentoModel(BaseModel):
    IdAgendamento: Optional[int]
    IdExpediente: Optional[int]
    IdTransacao: Optional[int]
    StatusAgendamento: Optional[int]
    StatusPagamento: Optional[str]
    IdSessao: Optional[str]
    Data: Optional[str]
    Hora: Optional[str]
    # TempoEstimado: Optional[str]
    # Preco: Optional[float]
    Profissional: Optional[Profissional]
    Paciente: Optional[Paciente]
    ValorTransacao: Optional[str]


class Model(BaseModel):
    __root__: List[ListarAgendamentoModel]
