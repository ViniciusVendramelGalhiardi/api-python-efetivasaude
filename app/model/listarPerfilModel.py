from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ListarPerfilModel(BaseModel):
    Id: Optional[int]
    Nome: Optional[str]