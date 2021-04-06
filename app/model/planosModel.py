from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PlanosModel(BaseModel):
    IdPlano: int
    Tipo:str