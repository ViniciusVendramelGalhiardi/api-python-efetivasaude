from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class UsuarioEntity(BaseModel):
    Nome: Optional[str]
    Telefone: Optional[str]
    Email: Optional[str]
    Cidade: Optional[str]
    Estado: Optional[str]
    IdConheceu: Optional[int]
    Senha: Optional[str]
    TermosCondicoes: Optional[bool]
    PoliticaPrivacidade: Optional[bool]
    Apelido: Optional[str]
    EstadoCivil: Optional[str]
    PossuiFilhosQtd: Optional[int]
    IdHobbie: Optional[int]
    DataNascimento: Optional[str]
    Genero: Optional[str]
    IdProfissao: Optional[int]
    Cpf: Optional[str]
    Dependente:Optional[bool]
    idUsuario: Optional[int]
    Dependentes: Optional[List]
