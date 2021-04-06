from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class UsarPlataformaModel(BaseModel):
    IdUsarPlataforma: int
    Tipo:str