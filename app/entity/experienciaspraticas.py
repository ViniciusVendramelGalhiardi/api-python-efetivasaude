from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ExperienciasEntity(BaseModel):
    IdExperiencia: Optional[int]
    IdUsuario: Optional[int]
    TipoExperiencia: Optional[str]
    AtividadePrincipal: Optional[str]
    Descricao: Optional[str]
    DataInicio:Optional[str]
    DataTermino:Optional[str]