from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PlanodeSaudeEmpresaUsuario(BaseModel):
    Id:Optional[int] = None 
    IdPlanoCredenciado: int
    IdUsuario: Optional[int] = None 