from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ContasCorrenteEntity(BaseModel):
    IdContaBancaria: Optional[int]
    Banco: Optional[str]
    Agencia: Optional[int]
    ContaCorrente: Optional[int]
    DigitoVerificador: Optional[int]
    IdUsuario: Optional[int]