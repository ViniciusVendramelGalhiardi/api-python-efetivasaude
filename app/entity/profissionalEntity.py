from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ProfissionalEntity(BaseModel):
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
    Dependentes: List #lista
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

    ExperienciasPraticaProf: Optional[List]
    FormacoesProf:  Optional[List]
    IdiomasAtendidosProf: Optional[List]
    AtendimentoPresencialProf: Optional[List]
    ContasCorrente: Optional[List]

    