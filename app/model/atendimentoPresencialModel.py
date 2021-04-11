from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class AtendimentoPresencialModel(BaseModel):
    IdAtendimentoPresencial: int
    Endereco: str
    Numero: int
    Conjunto: str
    Bairro:str
    Cidade:str
    Estado:str
    Cep:str
    IdUsuario: int