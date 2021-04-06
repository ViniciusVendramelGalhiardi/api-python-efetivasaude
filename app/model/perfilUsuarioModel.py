from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PerfilUsuarioModel(BaseModel):
    Id: int
    IdUsuario:int
    IdTipoUsuario:int