from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ListarProfissaoModel(BaseModel):
    Id: Optional[int]
    Nome: Optional[str]