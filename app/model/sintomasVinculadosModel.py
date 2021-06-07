from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class SintomasVinculadosModel(BaseModel):
    Id: Optional[int]
    IdSintomaAtendido:str
    IdUsuario: int