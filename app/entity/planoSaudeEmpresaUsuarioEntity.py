from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PlanodeSaudeEmpresaUsuarioEntity(BaseModel):
    Id:Optional[int] = None 
    IdPlanoCredenciado: Optional[int]
    IdUsuario: Optional[int] = None 