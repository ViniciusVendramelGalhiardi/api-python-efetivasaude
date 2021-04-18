from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class DependentesEntity(BaseModel):
    IdDependente: Optional[int]
    Nome: Optional[str]
    Apelido: Optional[str]
    DataNascimento: Optional[str]
    Genero: Optional[str]
    Telefone:Optional[str]
    Email:Optional[str]
    Cpf:Optional[str]
    IdUsuario: Optional[str]