from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class DependenteModel(BaseModel):
    Nome: str
    Apelido: str
    DataNascimento: str
    Genero: str
    Telefone:str
    Email:str
    Cpf:str
    IdUsuario: int