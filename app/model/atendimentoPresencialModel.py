from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class AtendimentoPresencialModel(BaseModel):
    IdAtendimentoPresencial:Optional[int]
    Endereco: Optional[str]
    Numero: Optional[int]
    Conjunto: Optional[str]
    Bairro:Optional[str]
    Cidade:Optional[str]
    Estado:Optional[str]
    Cep:Optional[str]
    IdUsuario: Optional[int]