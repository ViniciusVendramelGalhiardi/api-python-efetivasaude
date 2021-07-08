from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class UsuarioProntuarioModel(BaseModel):
    Id: Optional[int]
    IdUsuario: Optional[int]
    Prontuario:Optional[str]