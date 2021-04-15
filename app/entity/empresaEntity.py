from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class EmpresaEntity(BaseModel):
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
    NomeEmpresaEmp: Optional[str] 
    TelefoneCorporativoEmp: Optional[str] 
    EmailCorporativoEmp: Optional[str] 
    SiteEmpr: Optional[str] 
    LinkedinEmpr: Optional[str] 
    InstagramEmp: Optional[str] 
    CargoFuncaoEmp: Optional[str] 
    NumeroColaboradoresEmp:  Optional[int] 
    
    PlanodeSaudeEmpresa: Optional[List]  
    ContasCorrente: Optional[List]  