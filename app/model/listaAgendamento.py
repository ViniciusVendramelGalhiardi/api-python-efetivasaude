from app.entity.profissionalEntity import ProfissionalEntity
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
from app.model.agendamentoConsultaModel import AgendamentoConsultaModel


class ListarAgendamentosProfissionalModel(BaseModel):
    Agendamentos: Optional[List[AgendamentoConsultaModel]]
    profissional: Optional[ProfissionalEntity]
    
