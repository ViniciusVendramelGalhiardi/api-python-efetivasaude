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

class UsuarioModel(BaseModel):
    IdUsuario: int
    Nome: str
    Telefone:str
    Email: str
    Cidade:str
    Estado:str
    IdConheceu:int
    Senha:str
    Senha_Confirmar:str
    TermosCondicoes:bool = False
    PoliticaPrivacidade:bool  = False
    Apelido: str
    EstadoCivil: str
    PossuiFilhosQtd: int
    IdHobbie: int
    DataNascimento:datetime
    Genero:str
    IdProfissao:int
    Cpf: str
    Dependente: bool = False
    IdHorarioTrabalho: int
    IdTipoUsuario: int
    IdUsarPlataformaProfissionais: int
    IdConselhoRegional: int
    PossuiCNPJ: bool = False
    TrabalharComCNPJ: bool = False
    CartaApresentacao: str
    IdAbordagem: int
    HorasPorSemana: str
    FimDesemana: str
    DuracaoAtendimento:str
    AtendePlanoDeSaude:bool = False
    ReciboReembolsavel: bool = False
    AtendimentoPresencial: bool = False
    PrimeiroClienteCobra: bool
    PrimeiroClienteValorFixo: bool
    EmpresasParceirasDesconto: bool
    ValorPorSessao: float
    NomeEmpresa: str
    TelefoneCorporativo: str
    EmailCorporativo: str
    Site: str
    CnPj: str
    Linkedin: str
    Instagram: str
    CargoFuncao: str
    NumeroColaboradores: int
    ContasCorrente: List[ContaCorrenteModel]
    ExperienciasPratica: List[ExperienciaPraticaModel]
    Formacoes: List[FormacaoAcademicaModel]
    IdiomasAtendidos: List[IdiomasAtendidosModel]
    Dependentes: List[DependenteModel]
    AtendimentoPresencial: AtendimentoPresencialModel
    
    @validator('Senha_Confirmar')
    def passwords_match(cls, v, values, **kwargs):
        if 'Senha' in values and v != values['Senha']:
            raise ValueError('As senhas estão diferentes')
        return v

 