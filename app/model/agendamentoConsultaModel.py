from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class AgendamentoConsultaModel(BaseModel):
    IdAgendamento: Optional[int]
    Idexpediente: int
    IdUsuario: int
    IdDependente: Optional[str] = 'NULL'
    StatusPagamento: str
    IdTransacao: int
    statusAgendamento: int
    IDSessao: Optional[str]