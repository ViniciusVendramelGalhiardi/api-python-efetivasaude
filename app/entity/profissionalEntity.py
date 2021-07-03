from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator


class ProfissionalEntity(BaseModel):
    Nome: str
    Telefone: str
    Email: str
    Cidade: str
    Estado: str
    Cep:Optional[str]
    Endereco:Optional[str]
    IdConheceu: int
    Senha: Optional[str]
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
    IdHorarioTrabalhoProf: Optional[int] 
    IdUsarPlataformaProf: Optional[int]
    IdConselhoRegionalProf: Optional[int] 
    PossuiCNPJProf: Optional[bool] 
    TrabalharComCNPJProf: Optional[bool] 
    Cnpj: Optional[str] 
    CartaApresentacaoProf: Optional[str] 
    OutraAbordagemProf: Optional[str] 
    idUsuario: Optional[int]
    idUsuarioIugu:Optional[str]
    IdPerfil: Optional[str]

    #ePsi
    RegistroCRPePsi: Optional[str]
    RegistroePsiValidado: Optional[bool]
 
    OutroPublicoProf:Optional[str]
    OutroIdiomaProf: Optional[str]
    
    DuracaoAtendimentoProf:Optional[str] = ''
    AtendePlanoDeSaudeProf:Optional[bool] = False
    ReciboReembolsavelProf: Optional[bool] = False
    AtendePresencialmenteProf: Optional[bool] = False
    PrimeiroClienteCobraProf: Optional[bool] = True
    PrimeiroClienteValorFixoProf: Optional[bool] = True
    EmpresasParceirasDescontoProf: Optional[bool] = True
    ValorPorSessaoProf: Optional[float] = 0.00
    Dependente:Optional[bool] = False
    
    Dependentes: Optional[List] #lista
    ExperienciasPraticaProf: Optional[List]
    FormacoesProf:  Optional[List]
    IdiomasAtendidosProf: Optional[List]
    AtendimentoPresencialProf: Optional[List]
    ContasCorrente: Optional[List]
    IdAbordagemProf: Optional[List]
    IdsPublicoAtendido:Optional[List]
  