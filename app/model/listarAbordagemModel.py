from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ListarAbordagemModel(BaseModel):
    Id: Optional[int]
    Nome: Optional[str]