from pydantic.errors import ConfigError
import pyodbc
from settings import CONNECTION_STRING_DB
from app.model.perfisModel import PerfisModel
from app.entity.usuarioEntity import UsuarioEntity
from app.entity.profissionalEntity import ProfissionalEntity
from app.entity.empresaEntity import EmpresaEntity
from app.factory.clienteFactory import UsuarioFactory
from app.entity.usuarioEntity import UsuarioEntity
from app.model.expedienteProfissionalModel import ExpedienteProfissionalModel
from typing import List
from app.model.sintomasVinculadosModel import SintomasVinculadosModel
from app.model.cartaoModel import CartaoModel


def CadastraUsuario(uEntity: UsuarioEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO usuario (Nome, Telefone,Email,Cidade, Estado, Cep, Endereco, IdConheceu, Senha, TermosCondicoes,PoliticaPrivacidade, Apelido, EstadoCivil, PossuiFilhosQtd, IdHobbie,DataNascimento, Genero, IdProfissao,Cpf , Dependente, IdPerfil) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (uEntity.Nome, uEntity.Telefone, uEntity.Email, uEntity.Cidade, uEntity.Estado, uEntity.Cep, uEntity.Endereco, uEntity.IdConheceu, uEntity.Senha, uEntity.TermosCondicoes,
                        uEntity.PoliticaPrivacidade, uEntity.Apelido, uEntity.EstadoCivil, uEntity.PossuiFilhosQtd, uEntity.IdHobbie, uEntity.DataNascimento,
                        uEntity.Genero, uEntity.IdConheceu, uEntity.Cpf, uEntity.Dependente, IdPerfil))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idUsuario = cursor.fetchone()[0]

        if uEntity.Dependente and uEntity.Dependentes is not None:
            for item in uEntity.Dependentes:
                cursor.execute('INSERT INTO Dependente (Nome, Apelido, DataNascimento, Genero, Telefone, Email, CPF, IdUsuario) VALUES(?,?,?,?,?,?,?,?)',
                               (item.Nome, item.Apelido, item.DataNascimento, item.Genero, item.Telefone, item.Email, item.Cpf, idUsuario))
                cursor.commit()

        uEntity.idUsuario = idUsuario

    except Exception as mensagemErro:
        return mensagemErro
    return uEntity


def CadastraProfissional(pEntity: ProfissionalEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuario (Nome, Telefone,Email,Cidade, Estado, Cep, Endereco, IdConheceu, Senha, TermosCondicoes,PoliticaPrivacidade, Apelido, EstadoCivil, PossuiFilhosQtd, IdHobbie,DataNascimento, Genero, IdProfissao,Cpf , Dependente,IdHorarioTrabalhoProf,IdUsarPlataformaProf,IdConselhoRegionalProf,PossuiCNPJProf,TrabalharComCNPJProf,Cnpj,CartaApresentacaoProf, OutraAbordagemProf, DuracaoAtendimentoProf, AtendePlanoDeSaudeProf,ReciboReembolsavelProf,AtendePresencialmenteProf,PrimeiroClienteCobraProf,PrimeiroClienteValorFixoProf,EmpresasParceirasDescontoProf,ValorPorSessaoProf, IdPerfil,RegistroCRPePsi,RegistroePsiValidado, OutroPublicoProf, OutroIdiomaProf) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (pEntity.Nome, pEntity.Telefone, pEntity.Email, pEntity.Cidade, pEntity.Estado, pEntity.Cep, pEntity.Endereco, pEntity.IdConheceu, pEntity.Senha, pEntity.TermosCondicoes, pEntity.PoliticaPrivacidade,
                        pEntity.Apelido, pEntity.EstadoCivil, pEntity.PossuiFilhosQtd, pEntity.IdHobbie, pEntity.DataNascimento, pEntity.Genero, pEntity.IdProfissao, pEntity.Cpf, pEntity.Dependente, pEntity.IdHorarioTrabalhoProf,
                        pEntity.IdUsarPlataformaProf, pEntity.IdConselhoRegionalProf, pEntity.PossuiCNPJProf, pEntity.TrabalharComCNPJProf, pEntity.Cnpj, pEntity.CartaApresentacaoProf, pEntity.OutraAbordagemProf, pEntity.DuracaoAtendimentoProf,
                        pEntity.AtendePlanoDeSaudeProf, pEntity.ReciboReembolsavelProf, pEntity.AtendePresencialmenteProf, pEntity.PrimeiroClienteCobraProf, pEntity.PrimeiroClienteValorFixoProf, pEntity.EmpresasParceirasDescontoProf, pEntity.ValorPorSessaoProf, IdPerfil, pEntity.RegistroCRPePsi, pEntity.RegistroePsiValidado, pEntity.OutroPublicoProf, pEntity.OutroIdiomaProf))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idUsuario = cursor.fetchone()[0]

        if pEntity.Dependentes is not None:
            for item in pEntity.Dependentes:
                cursor.execute('INSERT INTO Dependente (Nome, Apelido, DataNascimento, Genero, Telefone, Email, CPF, IdUsuario) VALUES(?,?,?,?,?,?,?,?)',
                               (item.Nome, item.Apelido, item.DataNascimento, item.Genero, item.Telefone, item.Email, item.Cpf, idUsuario))
                cursor.commit()

        if pEntity.IdAbordagemProf is not None:
            for item in pEntity.IdAbordagemProf:
                cursor.execute('''INSERT INTO [dbo].[abordagemProfissional]
                                    ([IdAbordagemAdotada],[IdUsuarioProfissional])
                                VALUES(?,?)''',
                               (item.IdAbordagemAdotada,  idUsuario))
                cursor.commit()

        if pEntity.FormacoesProf is not None:
            for item in pEntity.FormacoesProf:
                cursor.execute('INSERT INTO formacaoAcademica (IdUsuario, InstituicaoEnsino, NomeCurso,NivelAcademico,AnoInicio,AnoTermino,DescricaoCurso,Anexo) VALUES (?,?, ?, ?, ?, ?, ?, ?)',
                               (idUsuario, item.InstituicaoEnsino, item.NomeCurso, item.NivelAcademico, item.AnoInicio, item.AnoTermino, item.DescricaoCurso, item.Anexo))
                cursor.commit()

        if pEntity.ExperienciasPraticaProf is not None:
            for item in pEntity.ExperienciasPraticaProf:
                cursor.execute('INSERT INTO experienciaPratica (IdUsuario, TipoExperiencia, AtividadePrincipal, Descricao, DataInicio, DataTermino) VALUES (?,?,?,?,?,?)',
                               (idUsuario, item.TipoExperiencia, item.AtividadePrincipal, item.Descricao, item.DataInicio, item.DataTermino))
                cursor.commit()

        if pEntity.IdiomasAtendidosProf is not None:
            for item in pEntity.IdiomasAtendidosProf:
                cursor.execute('INSERT INTO idiomasAtendidos (Ididioma,IdUsuario) VALUES (?,?)',
                               (item.Ididioma, idUsuario))
                cursor.commit()

        if pEntity.AtendimentoPresencialProf is not None:
            for item in pEntity.AtendimentoPresencialProf:
                cursor.execute('INSERT INTO atendimentoPresencial (Endereco,Numero,Conjunto,Bairro,Cidade,Estado,Cep,IdUsuario) VALUES (?, ?,?,?,?,?,?,?)',
                               (item.Endereco, item.Numero, item.Conjunto, item.Bairro, item.Cidade, item.Estado, item.Cep, idUsuario))
                cursor.commit()

        if pEntity.ContasCorrente is not None:
            for item in pEntity.ContasCorrente:
                cursor.execute('INSERT INTO ContaCorrente (Banco,Agencia,ContaCorrente,DigitoVerificador,IdUsuario) VALUES (?,?,?,?,?)',
                               (item.Banco, item.Agencia, item.ContaCorrente, item.DigitoVerificador, idUsuario))
                cursor.commit()

        if pEntity.IdsPublicoAtendido is not None:
            for item in pEntity.IdsPublicoAtendido:
                cursor.execute('''INSERT INTO [dbo].[publicoAtendidoProfissional]
                                        ([IdPublicoAtendindo]
                                        ,[IdUsuarioProfissional])
                                    VALUES
                                        (?,?)''',
                               (item.IdPublicoAtendido, idUsuario))
                cursor.commit()

        pEntity.idUsuario = idUsuario

    except Exception as mensagemErro:
        return mensagemErro

    return pEntity


def CadastraEmpresa(eEntity: EmpresaEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO [dbo].[usuario] (Nome, Telefone, Email, Cidade, Estado, Cep, Endereco, IdConheceu, Senha, TermosCondicoes, PoliticaPrivacidade, Apelido, NomeEmpresaEmp, TelefoneCorporativoEmp, EmailCorporativoEmp,SiteEmpr,LinkedinEmpr, InstagramEmp,CargoFuncaoEmp,NumeroColaboradoresEmp,Cnpj, IdPerfil) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (eEntity.Nome, eEntity.Telefone, eEntity.Email, eEntity.Cidade, eEntity.Estado, eEntity.Cep, eEntity.Endereco, eEntity.IdConheceu, eEntity.Senha, eEntity.TermosCondicoes, eEntity.PoliticaPrivacidade, eEntity.Apelido, eEntity.NomeEmpresaEmp, eEntity.TelefoneCorporativoEmp, eEntity.EmailCorporativoEmp, eEntity.SiteEmpr, eEntity.LinkedinEmpr, eEntity.InstagramEmp, eEntity.CargoFuncaoEmp, eEntity.NumeroColaboradoresEmp, eEntity.Cnpj, IdPerfil))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idUsuario = cursor.fetchone()[0]

        if eEntity.PlanodeSaudeEmpresa is not None:
            for item in eEntity.PlanodeSaudeEmpresa:
                cursor.execute('INSERT INTO planodeSaudeEmpresaUsuario (IdPlanoCredenciado, IdUsuario) VALUES (?,?)',
                               (item.IdPlanoCredenciado, idUsuario))
                cursor.commit()

        if eEntity.ContasCorrente is not None:
            for item in eEntity.ContasCorrente:
                cursor.execute('INSERT INTO ContaCorrente (Banco,Agencia,ContaCorrente,DigitoVerificador,IdUsuario) VALUES (?,?,?,?,?)',
                               (item.Banco, item.Agencia, item.ContaCorrente, item.DigitoVerificador, idUsuario))
                cursor.commit()

        eEntity.idUsuario = idUsuario

    except Exception as mensagemErro:
        return mensagemErro
    return eEntity


def BuscarUsuarioData(idUsuario: int):

    try:

        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''SELECT  
                            Nome,
                            Telefone, 
                            Email, 
                            Cidade, 
                            Estado, 
                            IdConheceu, 
                            TermosCondicoes, 
                            PoliticaPrivacidade, 
                            Apelido, 
                            EstadoCivil, 
                            PossuiFilhosQtd, 
                            IdHobbie, 
                            DataNascimento, 
                            Genero, 
                            IdProfissao,
                            Cpf,
                            idUsuario, 
                            Dependente,
                           	Cep, 
							Endereco,
							IdUsuarioIugu,
							IdPerfil
                        FROM usuario WHERE idUsuario = ?''', (idUsuario))
        records = cursor.fetchall()

        listdep = []
        if records[0][17] == True:
            cursor.execute('''SELECT IdDependente,Nome,Apelido,DataNascimento,Genero, Telefone, Email, Cpf, IdUsuario
                            FROM dependente WHERE idUsuario = ?''', (idUsuario))
            dependentes = cursor.fetchall()

            if len(dependentes) > 0:
                listdep = UsuarioFactory.DependenteEntityToModel(dependentes)

        entity = UsuarioFactory.UsuarioEntityToModel(records, listdep)

    except Exception as mensagemErro:
        return mensagemErro

    return entity


def BuscarProfissionalData(idUsuario: int):
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()

    cursor.execute('''SELECT 
                        Nome, 
                        Telefone, 
                        Email, 
                        Cidade, 
                        Estado, 
                        IdConheceu, 
                        TermosCondicoes, 
                        PoliticaPrivacidade, 
                        Apelido, 
                        EstadoCivil, 
                        PossuiFilhosQtd, 
                        IdHobbie, 
                        DataNascimento, 
                        Genero, 
                        IdProfissao, 
                        Cpf,
                        IdHorarioTrabalhoProf, 
                        IdUsarPlataformaProf, 
                        IdConselhoRegionalProf, 
                        PossuiCNPJProf, 
                        TrabalharComCNPJProf, 
                        Cnpj, 
                        CartaApresentacaoProf, 
                        OutraAbordagemProf, 
                        DuracaoAtendimentoProf, 
                        AtendePlanoDeSaudeProf,
                        ReciboReembolsavelProf, 
                        AtendePresencialmenteProf, 
                        PrimeiroClienteCobraProf, 
                        PrimeiroClienteValorFixoProf, 
                        EmpresasParceirasDescontoProf, 
                        ValorPorSessaoProf, 
                        idUsuario,
                        Cep, 
						Endereco,
						IdUsuarioIugu,
						IdPerfil,
                        RegistroCRPePsi,
                        RegistroePsiValidado,
                        OutroPublicoProf,
                        OutroIdiomaProf
                        FROM usuario WHERE idUsuario = ?''', (idUsuario))

    records = cursor.fetchall()

    # Experiencias
    cursor.execute(''' SELECT IdExperiencia, IdUsuario, TipoExperiencia, AtividadePrincipal, Descricao,DataInicio,DataTermino FROM experienciaPratica
                       WHERE idUsuario = ?''', (idUsuario))
    experiencias = cursor.fetchall()

    listexperiencias = []
    if len(experiencias) > 0:
        listexperiencias = UsuarioFactory.ExperienciasEntityToModel(
            experiencias)

    # Conta Corrente
    cursor.execute(''' SELECT IdContaBancaria, Banco, Agencia, ContaCorrente, DigitoVerificador, IdUsuario FROM [dbo].[ContaCorrente]
                       WHERE idUsuario = ?''', (idUsuario))
    cc = cursor.fetchall()

    listCC = []
    if len(cc) > 0:
        listCC = UsuarioFactory.ContaCorrenteEntityToModel(cc)

    # Atendimento Presencial
    cursor.execute(''' SELECT IdAtendimentoPresencial, Endereco, Numero, Conjunto, Bairro, Cidade, Estado,Cep,IdUsuario FROM atendimentoPresencial
                       WHERE idUsuario = ?''', (idUsuario))
    atp = cursor.fetchall()

    listAtp = []
    if len(atp) > 0:
        listAtp = UsuarioFactory.AtendimentoEntityToModel(atp)

    # Idiomas
    cursor.execute(''' SELECT Ididioma, idUsuario FROM idiomasAtendidos
                       WHERE idUsuario = ?''', (idUsuario))
    idiomas = cursor.fetchall()

    listIdiomas = []
    if len(idiomas) > 0:
        listIdiomas = UsuarioFactory.IdiomasEntityToModel(idiomas)

    # Formacao Academica
    cursor.execute(''' SELECT IdFormacao,IdUsuario,InstituicaoEnsino,NomeCurso,NivelAcademico,AnoInicio,AnoTermino,DescricaoCurso,Anexo FROM formacaoAcademica
                       WHERE idUsuario = ?''', (idUsuario))
    formacoes = cursor.fetchall()

    listFormacoes = []
    if len(formacoes) > 0:
        listFormacoes = UsuarioFactory.FormacoesEntityToModel(formacoes)

    # Formacao Academica
    cursor.execute(''' SELECT [IdAbordagemAdotada]
                        FROM [dbo].[abordagemProfissional]
                        WHERE IdUsuarioProfissional = ?''', (idUsuario))
    abordagem = cursor.fetchall()

    listabordagem = []
    if len(abordagem) > 0:
        listabordagem = UsuarioFactory.AbordagemEntityToModel(abordagem)

    cursor.execute('''SELECT * FROM [dbo].[publicoAtendidoProfissional] 
                    WHERE IdUsuarioProfissional = ?''', (idUsuario))
    publicoalvo = cursor.fetchall()

    listaPublicoProf = []
    if len(publicoalvo) > 0:
        listaPublicoProf = UsuarioFactory.PublicoAlvoEntityToModel(abordagem)

    # Objeto completo
    entity = UsuarioFactory.ProfEntityToModel(
        records, listCC, listAtp, listIdiomas, listFormacoes, listexperiencias, listabordagem, listaPublicoProf)
    return entity


def CadastraExpProfissional(expediente: ExpedienteProfissionalModel):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        for i in expediente.Expediente:
            print(i.Data)
            for j in i.Horas:
                print(j.start)
                print(j.end)
                cursor.execute('''INSERT INTO [dbo].[expedienteProfissional]
                                ([IdUsuarioProfissional]
                                ,[DataAtendimento]
                                ,[HorarioStart]
                                ,[HorarioEnd]
                                ,[Status])
                                    VALUES
                                        (?
                                        ,?
                                        ,?
                                        ,?
                                        ,?)''',
                               (expediente.IdUsuarioProfissional, i.Data,
                                j.start, j.end, False))
                cursor.commit()
                cursor.execute("SELECT @@IDENTITY AS ID;")
                idExpediente = cursor.fetchone()[0]

        if (idExpediente < 0 or idExpediente is None):
            return False

    except Exception as mensagemErro:
        return mensagemErro

    return True


def BuscarDataDisponivelProfissional(IdProfissional: int):
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    cursor.execute('''SELECT DataAtendimento  FROM [dbo].[expedienteProfissional] 
                      WHERE IdUsuarioProfissional = ? group by DataAtendimento''', (IdProfissional))
    records = cursor.fetchall()
    return records


def BuscarExpedienteProfissional(IdProfissional: int,  Status: str, DataAtendimento: str, IdExpediente: str):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()

    if (DataAtendimento is not None):
        DataAtendimento = "'" + str(DataAtendimento.replace('-', '')) + "'"

    if (DataAtendimento is None):
        DataAtendimento = 'NULL'

    if (Status is None):
        Status = 'NULL'

    if (IdExpediente is None):
        IdExpediente = 'NULL'

    if (DataAtendimento is None):
        DataAtendimento = 'NULL'

    _sql = '''SELECT [Id]
                            ,[IdUsuarioProfissional]
                            ,[DataAtendimento]
                            ,[HorarioStart]
                            ,[HorarioEnd]
                            ,[Status]
                        FROM [dbo].[expedienteProfissional] EX WHERE  EX.IdUsuarioProfissional = ''' + str(IdProfissional) + ''' AND EX.Status = ISNULL(''' + str(Status) + ''', EX.Status) AND EX.DataAtendimento = ISNULL(''' + DataAtendimento + ''', EX.DataAtendimento) AND EX.Id = ISNULL(''' + IdExpediente + ''', EX.Id)'''

    cursor.execute(_sql)
    records = cursor.fetchall()

    if len(records) > 0:
        exp = UsuarioFactory.ExpedientesModel(records)
        return exp
    return None

def BuscarExpedienteById(IdExpediente):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    cursor.execute('''SELECT DataAtendimento,HorarioStart FROM [dbo].[expedienteProfissional] WHERE Id = ?''', (IdExpediente))      
    records = cursor.fetchall()
    return records


def BuscarEmpresaData(idUsuario: int):

    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()

    cursor.execute('''SELECT Nome,
                        Telefone,
                        Email,
                        Cidade,
                        Estado,
                        IdConheceu,
                        TermosCondicoes,
                        PoliticaPrivacidade,
                        Apelido,
                        NomeEmpresaEmp,
                        TelefoneCorporativoEmp,
                        EmailCorporativoEmp,
                        SiteEmpr,
                        LinkedinEmpr,
                        InstagramEmp,
                        CargoFuncaoEmp,
                        NumeroColaboradoresEmp,
                        Cnpj,
                        idUsuario,
                        IdUsuarioIugu,
                        Cep,
                        Endereco
                    FROM usuario WHERE idUsuario = ?''', (idUsuario))
    records = cursor.fetchall()

    listplanos = []
    cursor.execute('''SELECT Id, IdPlanoCredenciado, IdUsuario  
                        FROM planodeSaudeEmpresaUsuario WHERE idUsuario = ?''', (idUsuario))
    planos = cursor.fetchall()
    if len(planos) > 0:
        listplanos = UsuarioFactory.PlanosEntityToModel(planos)

    # Conta Corrente
    cursor.execute(''' SELECT IdContaBancaria, Banco, Agencia, ContaCorrente, DigitoVerificador, IdUsuario FROM [dbo].[ContaCorrente]
                    WHERE idUsuario = ?''', (idUsuario))
    cc = cursor.fetchall()

    listCC = []
    if len(cc) > 0:
        listCC = UsuarioFactory.ContaCorrenteEntityToModel(cc)
    entity = UsuarioFactory.EmpresaEntityToModel(records, listplanos, listCC)

    return entity


def AtualizaIdUsuarioIugu(IdUsuarioIugu, IdUsuario):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    cursor.execute('UPDATE usuario SET IdUsuarioIugu = ? WHERE IdUsuario = ?',
                   (IdUsuarioIugu, IdUsuario))
    cursor.commit()


def VincularSintomaProfissional(sintomas):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        for item in sintomas:
            cursor.execute('''INSERT INTO [dbo].[sintomasVinculados]
                                    ([IdSintomaAtendido]
                                    ,[IdUsuario])
                                VALUES
                                    (?,?)''',
                           (item.IdSintomaAtendido, item.IdUsuario))
            cursor.commit()
            #cursor.execute("SELECT @@IDENTITY AS ID;")
    except Exception as mensagemErro:
        return mensagemErro

    return True


def BuscarSintomaPorUsuarioData(idUsuario: int):

    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute(
            '''SELECT * FROM sintomasVinculados WHERE IdUsuario = ?''', (idUsuario))
        records = cursor.fetchall()

        entity = UsuarioFactory.SintomasEntityToModel(records)

    except Exception as mensagemErro:
        return mensagemErro

    return entity


def CadastrarCartao(card: CartaoModel):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO [dbo].[cartao]
                                ([Nome]
                                ,[Numero]
                                ,[Validade]
                                ,[IdUsuario])
                            VALUES
                                (?
                                ,?
                                ,?
                                ,?)''',
                       (card.Nome, card.Numero, card.Validade, card.IdUsuario))
        cursor.commit()
        #cursor.execute("SELECT @@IDENTITY AS ID;")
    except Exception as mensagemErro:
        return mensagemErro
    return True

def BuscarCartaoUsuarioData(idUsuario: int):

    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute(
            '''SELECT * FROM [dbo].[cartao] WHERE IdUsuario =  ?''', (idUsuario))
        records = cursor.fetchall()

        entity = UsuarioFactory.CartaoEntityToModel(records)

    except Exception as mensagemErro:
        return mensagemErro

    return entity



def BuscarProfissionalPorPesquisaData(IdProfissao, AtendePresencialmenteProf, DataAtendimento):

    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''SELECT 
                            Nome, 
                            Telefone, 
                            Email, 
                            Cidade, 
                            Estado, 
                            IdConheceu, 
                            TermosCondicoes, 
                            PoliticaPrivacidade, 
                            Apelido, 
                            EstadoCivil, 
                            PossuiFilhosQtd, 
                            IdHobbie, 
                            DataNascimento, 
                            Genero, 
                            IdProfissao, 
                            Cpf,
                            IdHorarioTrabalhoProf, 
                            IdUsarPlataformaProf, 
                            IdConselhoRegionalProf, 
                            PossuiCNPJProf, 
                            TrabalharComCNPJProf, 
                            Cnpj, 
                            CartaApresentacaoProf, 
                            OutraAbordagemProf, 
                            DuracaoAtendimentoProf, 
                            AtendePlanoDeSaudeProf,
                            ReciboReembolsavelProf, 
                            AtendePresencialmenteProf, 
                            PrimeiroClienteCobraProf, 
                            PrimeiroClienteValorFixoProf, 
                            EmpresasParceirasDescontoProf, 
                            ValorPorSessaoProf, 
                            idUsuario,
                            Cep, 
                            Endereco,
                            IdUsuarioIugu,
                            IdPerfil,
                            RegistroCRPePsi,
                            RegistroePsiValidado,
                            OutroPublicoProf,
                            OutroIdiomaProf
                            FROM usuario 
							U INNER JOIN  [dbo].[expedienteProfissional] E
							ON U.IdUsuario = E.IdUsuarioProfissional
							WHERE 
							u.IdProfissao = ?
							AND U.AtendePresencialmenteProf = ?
							AND E.DataAtendimento = ? ''', (IdProfissao,AtendePresencialmenteProf, DataAtendimento))
        
        records = cursor.fetchall()

        entity = UsuarioFactory.profissionalEntity(records)

    except Exception as mensagemErro:
        return mensagemErro
    return entity


def ExcluirCartao(idUsuario: int):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM [dbo].[cartao] WHERE IdUsuario = ?''',
                       (idUsuario))
        cursor.commit()
        #cursor.execute("SELECT @@IDENTITY AS ID;")
    except Exception as mensagemErro:
        return mensagemErro
    return True