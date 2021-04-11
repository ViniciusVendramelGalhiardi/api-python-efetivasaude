from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
from .contaCorrenteModel import ContaCorrenteModel
from .experienciaPraticaModel import ExperienciaPraticaModel
from .dependenteModel import DependenteModel
from .formacaoAcademiaModel import FormacaoAcademicaModel
from .idiomasAtendidosModel import IdiomasAtendidosModel
from typing import List
from .atendimentoPresencialModel import AtendimentoPresencialModel
from .planodeSaudeEmpresaUsuario import PlanodeSaudeEmpresaUsuario
from .perfilUsuarioModel import PerfilUsuarioModel


class UsuarioModel(BaseModel):
    IdUsuario: Optional[int] = 0
    Nome: str
    Telefone:str
    Email: str
    Cidade:str
    Estado:str
    IdConheceu:int
    Senha:str
    Senha_Confirmar:Optional[str] 
    TermosCondicoes:bool = False
    PoliticaPrivacidade:bool  = False
    Apelido: str
    
    EstadoCivil: Optional[str]
    PossuiFilhosQtd: Optional[int] 
    IdHobbie: Optional[int]
    DataNascimento:Optional[str]
    Genero:Optional[str]
    IdProfissao:Optional[int]
    Cpf: Optional[str]
    Dependente: bool = False
    Dependentes: Optional[List[DependenteModel]]
    IdHorarioTrabalhoProf: Optional[int] 
    IdUsarPlataformaProf: Optional[int]
    IdConselhoRegionalProf: Optional[int] 
    PossuiCNPJProf: Optional[bool] 
    TrabalharComCNPJProf: Optional[bool] 
    CnPj: Optional[str] 
    CartaApresentacaoProf: Optional[str] 
    IdAbordagemProf: Optional[int] 
    DuracaoAtendimentoProf:Optional[str] = ''
    AtendePlanoDeSaudeProf:Optional[bool] = False
    ReciboReembolsavelProf: Optional[bool] = False
    AtendePresencialmenteProf: Optional[bool] = False
    PrimeiroClienteCobraProf: Optional[bool] = True
    PrimeiroClienteValorFixoProf: Optional[bool] = True
    EmpresasParceirasDescontoProf: Optional[bool] = True
    ValorPorSessaoProf: Optional[float] = 0.00

    ExperienciasPraticaProf: Optional[List[ExperienciaPraticaModel]]
    FormacoesProf:  Optional[List[FormacaoAcademicaModel]]
    IdiomasAtendidosProf: Optional[List[IdiomasAtendidosModel]]
    AtendimentoPresencialProf:  Optional[List[AtendimentoPresencialModel]] 

    NomeEmpresaEmp: Optional[str] 
    TelefoneCorporativoEmp: Optional[str] 
    EmailCorporativoEmp: Optional[str] 
    SiteEmpr: Optional[str] 
    LinkedinEmpr: Optional[str] 
    InstagramEmp: Optional[str] 
    CargoFuncaoEmp: Optional[str] 
    NumeroColaboradoresEmp: Optional[int] 
    PlanodeSaudeEmpresa: Optional[List[PlanodeSaudeEmpresaUsuario]]  
    ContasCorrente: Optional[List[ContaCorrenteModel]]

    @validator('Senha_Confirmar')
    def passwords_match(cls, v, values, **kwargs):
        if 'Senha' in values and v != values['Senha']:
            raise ValueError('As senhas estão diferentes')
        return v

 