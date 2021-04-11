from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ProfissionalEntity:
    def __init__(self,
                 Nome, Telefone,Email, Cidade,Estado,  IdConheceu, Senha, TermosCondicoes,
                 PoliticaPrivacidade,Apelido, EstadoCivil, PossuiFilhosQtd,IdHobbie, DataNascimento, 
                  Genero, IdProfissao, Cpf, Dependente):
        Nome: Nome
        Telefone: Telefone
        Email: Email
        Cidade: Cidade
        Estado: Estado
        IdConheceu: IdConheceu
        Senha: Senha
        TermosCondicoes: TermosCondicoes
        PoliticaPrivacidade: PoliticaPrivacidade
        Apelido: Apelido
        EstadoCivil: EstadoCivil
        PossuiFilhosQtd: PossuiFilhosQtd
        IdHobbie: IdHobbie
        DataNascimento: DataNascimento
        Genero: Genero
        IdProfissao: IdProfissao
        Cpf: Cpf
        Dependente: Dependente
