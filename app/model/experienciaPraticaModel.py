from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ExperienciaPraticaModel(BaseModel):
   IdUsuario: int
   TipoExperiencia: str
   AtividadePrincipal: str
   Descricao: str
   DataInicio: datetime
   DataTermino: datetime