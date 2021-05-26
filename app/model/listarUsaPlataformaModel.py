from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ListarUsaPlataformaModel(BaseModel):
    Id: Optional[int]
    Nome: Optional[str]