from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator


class AgendamentoConsultaModel(BaseModel):
    IdAgendamento: Optional[int]
    Idexpediente: Optional[int]
    IdUsuario: Optional[int]
    IdUsuarioProfissional: Optional[int]
    IdDependente: Optional[str] = 'NULL'
    StatusPagamento: Optional[str]
    IdTransacao: Optional[int]
    statusAgendamento: Optional[int]
    IDSessao: Optional[str]
