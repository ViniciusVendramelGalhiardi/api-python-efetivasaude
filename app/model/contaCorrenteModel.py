from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ContaCorrenteModel(BaseModel):
    Banco: str
    Agencia: int
    ContaCorrente: int
    DigitoVerificador: int
    IdUsuario: int