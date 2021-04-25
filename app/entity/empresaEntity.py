from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class EmpresaEntity(BaseModel):
    Nome: Optional[str] 
    Telefone: Optional[str] 
    Email: Optional[str] 
    Cidade: Optional[str] 
    Estado: Optional[str] 
    Cep:Optional[str]
    Endereco:Optional[str]
    IdConheceu: Optional[int] 
    Senha: Optional[str]
    TermosCondicoes: Optional[bool] 
    PoliticaPrivacidade: Optional[bool] 
    Apelido: Optional[str] 
    NomeEmpresaEmp: Optional[str] 
    TelefoneCorporativoEmp: Optional[str] 
    EmailCorporativoEmp: Optional[str] 
    SiteEmpr: Optional[str] 
    LinkedinEmpr: Optional[str] 
    InstagramEmp: Optional[str] 
    CargoFuncaoEmp: Optional[str] 
    NumeroColaboradoresEmp:  Optional[int] 
    Cnpj: Optional[str]

    PlanodeSaudeEmpresa: Optional[List]  
    ContasCorrente: Optional[List]  
    idUsuario: Optional[int]

    idUsuarioIugu:Optional[str]
    IdPerfil: Optional[str]