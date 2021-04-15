from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ExperienciaPraticaModel(BaseModel):
   IdUsuario: Optional[int]
   TipoExperiencia: Optional[str]
   AtividadePrincipal: Optional[str]
   Descricao: Optional[str]
   DataInicio: Optional[str]
   DataTermino: Optional[str]