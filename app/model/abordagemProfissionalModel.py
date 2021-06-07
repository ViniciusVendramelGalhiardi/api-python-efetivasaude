from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class AbordagemProfissionalModel(BaseModel):
    IdAbordagemAdotada: Optional[int]