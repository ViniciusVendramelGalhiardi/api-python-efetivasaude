from __future__ import annotations
from typing import List
from pydantic import BaseModel
from typing import Optional

class Hora(BaseModel):
    start: Optional[str]
    end: Optional[str]

class ExpedienteItem(BaseModel):
    Idexpediente: Optional[int]
    Data: Optional[str]
    Horas: Optional[List[Hora]]

class ExpedienteProfissionalModel(BaseModel):
    IdUsuarioProfissional: int
    Expediente: Optional[List[ExpedienteItem]]