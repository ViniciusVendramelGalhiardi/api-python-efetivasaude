from __future__ import annotations
from typing import List
from pydantic import BaseModel

class Profissional(BaseModel):
    Id: int
    Nome: str
    Imagem: str
    Profissao: str
    Crp: str

class Paciente(BaseModel):
    Id: int
    Nome: str
    Imagem: str
    Cpf: str
    DataNascimento: str

class ListarAgendamentoModel(BaseModel):
    IdAgendamento: int
    IdExpediente: int
    IdTransacao: int
    StatusAgendamento: int
    StatusPagamento: str
    IdSessao: str
    
    Data: str
    Hora: str
    TempoEstimado: str
    Preco: float
    Profissional: Profissional
    Paciente: Paciente

class Model(BaseModel):
    __root__: List[ListarAgendamentoModel]
