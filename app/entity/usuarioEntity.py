from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class UsuarioEntity(BaseModel):
    Nome: str
    Telefone: str
    Email: str
    Cidade: str
    Estado: str
    IdConheceu: int
    Senha: str
    TermosCondicoes: bool
    PoliticaPrivacidade: bool
    Apelido: str
    EstadoCivil: str
    PossuiFilhosQtd: int
    IdHobbie: int
    DataNascimento: str
    Genero: str
    IdProfissao: int
    Cpf: str
    Dependente:bool
