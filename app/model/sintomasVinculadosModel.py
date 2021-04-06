from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class SintomasVinculadosModel(BaseModel):
    Id: int
    IdSintomaAtendido:str
    IdUsuario: int