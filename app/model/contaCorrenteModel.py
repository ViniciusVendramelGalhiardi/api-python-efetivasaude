from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ContaCorrenteModel(BaseModel):
    Banco: str
    Agencia: str
    ContaCorrente: int
    DigitoVerificador: str
    IdUsuario: Optional[int]