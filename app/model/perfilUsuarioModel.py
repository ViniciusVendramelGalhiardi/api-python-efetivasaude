from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PerfilUsuarioModel(BaseModel):
    Id: Optional[int]
    IdUsuario:Optional[int]
    IdPerfil:int