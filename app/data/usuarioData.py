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
from app.model.historicoAtendimentoModel import HistoricoAtendimentoModel
from app.model.usuarioPronturioModel import UsuarioProntuarioModel
from app.model.colaboradoresEmpresa import ColaboradoresEmpresa


def CadastraUsuario(uEntity: UsuarioEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO usuario (Nome, Telefone,Email,Cidade, Estado, Cep, Endereco, IdConheceu, Senha, TermosCondicoes,PoliticaPrivacidade, Apelido, EstadoCivil, PossuiFilhosQtd, IdHobbie,DataNascimento, Genero, IdProfissao,Cpf , Dependente, IdPerfil, BaseImage, DataCadastro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (uEntity.Nome, uEntity.Telefone, uEntity.Email, uEntity.Cidade, uEntity.Estado, uEntity.Cep, uEntity.Endereco, uEntity.IdConheceu, uEntity.Senha, uEntity.TermosCondicoes,
                        uEntity.PoliticaPrivacidade, uEntity.Apelido, uEntity.EstadoCivil, uEntity.PossuiFilhosQtd, uEntity.IdHobbie, uEntity.DataNascimento,
                        uEntity.Genero, uEntity.IdConheceu, uEntity.Cpf, uEntity.Dependente, IdPerfil, uEntity.BaseImage, uEntity.DataCadastro))
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


def EditarUsuarioData(uEntity: UsuarioEntity, IdPerfil: int, IdUsuario: int):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''UPDATE [dbo].[usuario]
                            SET 
                            Nome = ?, 
                            Telefone = ?,
                            Email = ?,
                            Cidade = ?, 
                            Estado = ?, 
                            Cep = ?, 
                            Endereco = ?, 
                            IdConheceu = ?, 
                            TermosCondicoes = ?,
                            PoliticaPrivacidade = ?, 
                            Apelido = ?, 
                            EstadoCivil = ?, 
                            PossuiFilhosQtd = ?, 
                            IdHobbie = ?,
                            DataNascimento = ?, 
                            Genero = ?, 
                            IdProfissao= ?,
                            Cpf = ?, 
                            Dependente = ?, 
                            IdPerfil = ?
                            FROM usuario
                            WHERE IdUsuario = ?''',
                       (uEntity.Nome, uEntity.Telefone, uEntity.Email, uEntity.Cidade, uEntity.Estado, uEntity.Cep, uEntity.Endereco, uEntity.IdConheceu, uEntity.TermosCondicoes,
                        uEntity.PoliticaPrivacidade, uEntity.Apelido, uEntity.EstadoCivil, uEntity.PossuiFilhosQtd, uEntity.IdHobbie, uEntity.DataNascimento,
                        uEntity.Genero, uEntity.IdConheceu, uEntity.Cpf, uEntity.Dependente, IdPerfil, IdUsuario))
        cursor.commit()

        if uEntity.Dependente and uEntity.Dependentes is not None:
            for item in uEntity.Dependentes:
                cursor.execute('''UPDATE [dbo].[dependente]
                                    SET  [Nome] = ?
                                        ,[Apelido] = ?
                                        ,[DataNascimento] = ?
                                        ,[Genero] = ?
                                        ,[Telefone] = ?
                                        ,[Email] = ?
                                        ,[CPF] = ?
                                    WHERE IdUsuario = ?''',
                               (item.Nome, item.Apelido, item.DataNascimento, item.Genero, item.Telefone, item.Email, item.Cpf, item.IdUsuario))
                cursor.commit()

    except Exception as mensagemErro:
        return mensagemErro
    return uEntity


def CadastraProfissional(pEntity: ProfissionalEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuario (Nome, Telefone,Email,Cidade, Estado, Cep, Endereco, IdConheceu, Senha, TermosCondicoes,PoliticaPrivacidade, Apelido, EstadoCivil, PossuiFilhosQtd, IdHobbie,DataNascimento, Genero, IdProfissao,Cpf , Dependente,IdHorarioTrabalhoProf,IdUsarPlataformaProf,IdConselhoRegionalProf,PossuiCNPJProf,TrabalharComCNPJProf,Cnpj,CartaApresentacaoProf, OutraAbordagemProf, DuracaoAtendimentoProf, AtendePlanoDeSaudeProf,ReciboReembolsavelProf,AtendePresencialmenteProf,PrimeiroClienteCobraProf,PrimeiroClienteValorFixoProf,EmpresasParceirasDescontoProf,ValorPorSessaoProf, IdPerfil,RegistroCRPePsi,RegistroePsiValidado, OutroPublicoProf, OutroIdiomaProf, BaseImage, DataCadastro) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (pEntity.Nome, pEntity.Telefone, pEntity.Email, pEntity.Cidade, pEntity.Estado, pEntity.Cep, pEntity.Endereco, pEntity.IdConheceu, pEntity.Senha, pEntity.TermosCondicoes, pEntity.PoliticaPrivacidade,
                        pEntity.Apelido, pEntity.EstadoCivil, pEntity.PossuiFilhosQtd, pEntity.IdHobbie, pEntity.DataNascimento, pEntity.Genero, pEntity.IdProfissao, pEntity.Cpf, pEntity.Dependente, pEntity.IdHorarioTrabalhoProf,
                        pEntity.IdUsarPlataformaProf, pEntity.IdConselhoRegionalProf, pEntity.PossuiCNPJProf, pEntity.TrabalharComCNPJProf, pEntity.Cnpj, pEntity.CartaApresentacaoProf, pEntity.OutraAbordagemProf, pEntity.DuracaoAtendimentoProf,
                        pEntity.AtendePlanoDeSaudeProf, pEntity.ReciboReembolsavelProf, pEntity.AtendePresencialmenteProf, pEntity.PrimeiroClienteCobraProf, pEntity.PrimeiroClienteValorFixoProf, pEntity.EmpresasParceirasDescontoProf, pEntity.ValorPorSessaoProf, IdPerfil, pEntity.RegistroCRPePsi, pEntity.RegistroePsiValidado, pEntity.OutroPublicoProf, pEntity.OutroIdiomaProf, pEntity.BaseImage, pEntity.DataCadastro))
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


def EditarProfissional(pEntity: ProfissionalEntity, IdPerfil: int, IdUsuario: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''UPDATE usuario SET
                            Nome = ?
                            ,Telefone= ?
                            ,Email= ?
                            ,Cidade= ?
                            ,Estado= ?
                            ,Cep=?
                            ,Endereco= ?
                            ,IdConheceu= ?
                            ,TermosCondicoes= ?
                            ,PoliticaPrivacidade= ?
                            ,Apelido= ?
                            ,EstadoCivil= ?
                            ,PossuiFilhosQtd= ?
                            ,IdHobbie= ?
                            ,DataNascimento= ?
                            ,Genero= ?
                            ,IdProfissao=?
                            ,Cpf= ?
                            ,IdPerfil= ?
                            ,IdHorarioTrabalhoProf= ?
                            ,IdUsarPlataformaProf= ?
                            ,IdConselhoRegionalProf= ?
                            ,PossuiCNPJProf= ?
                            ,TrabalharComCNPJProf= ?
                            ,Cnpj= ?
                            ,CartaApresentacaoProf= ?
                            ,OutraAbordagemProf= ?
                            ,idUsuarioIugu= ?
                            ,RegistroCRPePsi= ?
                            ,RegistroePsiValidado= ?
                            ,OutroPublicoProf= ?
                            ,OutroIdiomaProf= ?
                            ,DuracaoAtendimentoProf= ?
                            ,AtendePlanoDeSaudeProf= ?
                            ,ReciboReembolsavelProf= ?
                            ,AtendePresencialmenteProf= ?
                            ,PrimeiroClienteCobraProf= ?
                            ,PrimeiroClienteValorFixoProf= ?
                            ,EmpresasParceirasDescontoProf= ?
                            ,ValorPorSessaoProf=?
                            ,Dependente= ?
                            WHERE IdUsuario = ?''',
                       (pEntity.Nome, pEntity.Telefone, pEntity.Email, pEntity.Cidade, pEntity.Estado, pEntity.Cep, pEntity.Endereco, pEntity.IdConheceu, pEntity.TermosCondicoes,
                        pEntity.PoliticaPrivacidade, pEntity.Apelido, pEntity.EstadoCivil, pEntity.PossuiFilhosQtd, pEntity.IdHobbie, pEntity.DataNascimento,
                        pEntity.Genero, pEntity.IdProfissao, pEntity.Cpf, IdPerfil, pEntity.IdHorarioTrabalhoProf, pEntity.IdUsarPlataformaProf,
                        pEntity.IdConselhoRegionalProf,
                        pEntity.PossuiCNPJProf,
                        pEntity.TrabalharComCNPJProf,
                        pEntity.Cnpj,
                        pEntity.CartaApresentacaoProf,
                        pEntity.OutraAbordagemProf,
                        pEntity.idUsuarioIugu,
                        pEntity.RegistroCRPePsi,
                        pEntity.RegistroePsiValidado,
                        pEntity.OutroPublicoProf,
                        pEntity.OutroIdiomaProf,
                        pEntity.DuracaoAtendimentoProf,
                        pEntity.AtendePlanoDeSaudeProf,
                        pEntity.ReciboReembolsavelProf,
                        pEntity.AtendePresencialmenteProf,
                        pEntity.PrimeiroClienteCobraProf,
                        pEntity.PrimeiroClienteValorFixoProf,
                        pEntity.EmpresasParceirasDescontoProf,
                        pEntity.ValorPorSessaoProf,
                        pEntity.Dependente, IdUsuario))
        cursor.commit()

        if pEntity.IdAbordagemProf is not None:
            for item in pEntity.IdAbordagemProf:
                cursor.execute('''UPDATE [abordagemProfissional] SET IdAbordagemAdotada = ? WHERE IdUsuarioProfissional = ?''',
                               (item.IdAbordagemAdotada,  IdUsuario))
                cursor.commit()

        if pEntity.IdiomasAtendidosProf is not None:
            for item in pEntity.IdiomasAtendidosProf:
                cursor.execute('UPDATE [idiomasAtendidos] SET Ididioma = ? WHERE IdUsuario = ?',
                               (item.Ididioma, IdUsuario))
                cursor.commit()

        # BIEL DISSE QUE NAO TEM ESSA TELA NO DITE
        # if pEntity.AtendimentoPresencialProf is not None:
        #     for item in pEntity.AtendimentoPresencialProf:
        #         cursor.execute('INSERT INTO atendimentoPresencial (Endereco,Numero,Conjunto,Bairro,Cidade,Estado,Cep,IdUsuario) VALUES (?, ?,?,?,?,?,?,?)',
        #                        (item.Endereco, item.Numero, item.Conjunto, item.Bairro, item.Cidade, item.Estado, item.Cep, idUsuario))
        #         cursor.commit()

        if pEntity.ContasCorrente is not None:
            for item in pEntity.ContasCorrente:
                cursor.execute('UPDATE ContaCorrente SET Banco = ?, Agencia = ?, ContaCorrente = ?, DigitoVerificador = ?  WHERE IdUsuario = ?',
                               (item.Banco, item.Agencia, item.ContaCorrente, item.DigitoVerificador, IdUsuario))
                cursor.commit()

        if pEntity.IdsPublicoAtendido is not None:
            for item in pEntity.IdsPublicoAtendido:
                cursor.execute('''UPDATE publicoAtendidoProfissional SET IdPublicoAtendindo = ? WHERE IdUsuarioProfissional = ?''',
                               (item.IdPublicoAtendido, IdUsuario))
                cursor.commit()

        #pEntity.idUsuario = idUsuario

    except Exception as mensagemErro:
        return mensagemErro

    return pEntity


def CadastraEmpresa(eEntity: EmpresaEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO [dbo].[usuario] (Nome, Telefone, Email, Cidade, Estado, Cep, Endereco, IdConheceu, Senha, TermosCondicoes, PoliticaPrivacidade, Apelido, NomeEmpresaEmp, TelefoneCorporativoEmp, EmailCorporativoEmp,SiteEmpr,LinkedinEmpr, InstagramEmp,CargoFuncaoEmp,NumeroColaboradoresEmp,Cnpj, IdPerfil, BaseImage, DataCadastro, BaseImageCompany) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (eEntity.Nome, eEntity.Telefone, eEntity.Email, eEntity.Cidade, eEntity.Estado, eEntity.Cep, eEntity.Endereco, eEntity.IdConheceu, eEntity.Senha, eEntity.TermosCondicoes, eEntity.PoliticaPrivacidade, eEntity.Apelido, eEntity.NomeEmpresaEmp, eEntity.TelefoneCorporativoEmp, eEntity.EmailCorporativoEmp, eEntity.SiteEmpr, eEntity.LinkedinEmpr, eEntity.InstagramEmp, eEntity.CargoFuncaoEmp, eEntity.NumeroColaboradoresEmp, eEntity.Cnpj, IdPerfil, eEntity.BaseImage, eEntity.DataCadastro, eEntity.BaseImageCompany))
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
							IdPerfil,
                            BaseImage
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
                        OutroIdiomaProf,
                        BaseImage
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
    cursor.execute(
        '''SELECT DataAtendimento,HorarioStart FROM [dbo].[expedienteProfissional] WHERE Id = ?''', (IdExpediente))
    records = cursor.fetchall()
    return records

def BuscarValorTransacaoData(IdTransacao):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT Valor FROM [dbo].[transacao] WHERE IdTransacao = ?''', (IdTransacao))
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

        cursor.execute(
            'DELETE FROM sintomasVinculados WHERE IdUsuario = ?', (sintomas[0].IdUsuario))
        cursor.commit()

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


def CadastraDependente(dependente):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[dependente]
           ([Nome]
           ,[Imagem]
           ,[Apelido]
           ,[DataNascimento]
           ,[Genero]
           ,[Telefone]
           ,[Email]
           ,[Cpf]
           ,[IdUsuario])
     VALUES
           (?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?)''',
                       (dependente.Nome, dependente.Imagem, dependente.Apelido, dependente.DataNascimento, dependente.Genero, dependente.Telefone, dependente.Email, dependente.Cpf, dependente.IdUsuario))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idDependente = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return False

    if (idDependente < 0 or idDependente is None):
        return False

    return idDependente


def AtualizaDependente(id, dependente):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('UPDATE [dbo].[dependente] SET [Nome] = ?, [Imagem] = ?, [Apelido] = ?, [DataNascimento] = ?, [Genero] = ?, [Telefone] = ?, [Email] = ?, [Cpf] = ?, [IdUsuario] = ? WHERE IdDependente = ?',
                       (dependente.Nome, dependente.Imagem, dependente.Apelido, dependente.DataNascimento, dependente.Genero, dependente.Telefone, dependente.Email, dependente.Cpf, dependente.IdUsuario, id))
        cursor.commit()

    except Exception as mensagemErro:
        return False

    return True


def ExcluirDependente(id):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''DELETE FROM [dbo].[dependente] WHERE IdDependente = ?''',
                       (id))
        cursor.commit()

    except Exception as mensagemErro:
        return False

    return True


def CadastraExperiencia(experiencia):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[experienciaPratica]
           ([IdUsuario]
           ,[TipoExperiencia]
           ,[AtividadePrincipal]
           ,[Descricao]
           ,[DataInicio]
           ,[DataTermino])
     VALUES
           (?
           ,?
           ,?
           ,?
           ,?
           ,?)''',
                       (experiencia.IdUsuario, experiencia.TipoExperiencia, experiencia.AtividadePrincipal, experiencia.Descricao, experiencia.DataInicio, experiencia.DataTermino))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idExperiencia = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return False

    if (idExperiencia < 0 or idExperiencia is None):
        return False

    return idExperiencia


def AtualizaExperiencia(id, experiencia):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('UPDATE [dbo].[experienciaPratica] SET [IdUsuario] = ?, [TipoExperiencia] = ?, [AtividadePrincipal] = ?, [Descricao] = ?, [DataInicio] = ?, [DataTermino] = ? WHERE IdExperiencia = ?',
                       (experiencia.IdUsuario, experiencia.TipoExperiencia, experiencia.AtividadePrincipal, experiencia.Descricao, experiencia.DataInicio, experiencia.DataTermino, id))
        cursor.commit()

    except Exception as mensagemErro:
        return False

    return True


def ExcluirExperiencia(id):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''DELETE FROM [dbo].[experienciaPratica] WHERE IdExperiencia = ?''',
                       (id))
        cursor.commit()

    except Exception as mensagemErro:
        return False

    return True


def CadastraFormacao(formacao):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[formacaoAcademica]
           ([IdUsuario]
           ,[InstituicaoEnsino]
           ,[NomeCurso]
           ,[NivelAcademico]
           ,[AnoInicio]
           ,[AnoTermino]
           ,[DescricaoCurso]
           ,[Anexo])
     VALUES
           (?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?)''',
                       (formacao.IdUsuario, formacao.InstituicaoEnsino, formacao.NomeCurso, formacao.NivelAcademico, formacao.AnoInicio, formacao.AnoTermino, formacao.DescricaoCurso, formacao.Anexo))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idFormacao = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return False

    if (idFormacao < 0 or idFormacao is None):
        return False

    return idFormacao


def AtualizaFormacao(id, formacao):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('UPDATE [dbo].[formacaoAcademica] SET [IdUsuario] = ?, [InstituicaoEnsino] = ?, [NomeCurso] = ?, [NivelAcademico] = ?, [AnoInicio] = ?, [AnoTermino] = ?, [DescricaoCurso] = ?, [Anexo] = ? WHERE IdFormacao = ?',
                       (formacao.IdUsuario, formacao.InstituicaoEnsino, formacao.NomeCurso, formacao.NivelAcademico, formacao.AnoInicio, formacao.AnoTermino, formacao.DescricaoCurso, formacao.Anexo, id))
        cursor.commit()

    except Exception as mensagemErro:
        return False

    return True


def ExcluirFormacao(id):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''DELETE FROM [dbo].[formacaoAcademica] WHERE IdFormacao = ?''',
                       (id))
        cursor.commit()

    except Exception as mensagemErro:
        return False

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



def BuscarDezUltimosCadastrados():
    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''SELECT TOP 10
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
							U LEFT JOIN  [dbo].[expedienteProfissional] E
							ON U.IdUsuario = E.IdUsuarioProfissional
							WHERE IdPerfil = 2 
							GROUP BY 
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
							ORDER BY IdUsuario DESC''')

        records = cursor.fetchall()

        entity = UsuarioFactory.profissionalEntity(records)

    except Exception as mensagemErro:
        return mensagemErro
    return entity


def BuscarProfissionalPorPesquisaData(IdProfissao, AtendePresencialmenteProf, DataAtendimento, IdSintomaAtendido, IdAbordagemAdotada, Nome):

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
                            u.IdUsuario,
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
							INNER JOIN [dbo].[sintomasVinculados] SI
							ON U.IdUsuario = SI.IdUsuario
							INNER JOIN [dbo].[abordagemProfissional] AB
							ON U.IdUsuario = AB.IdUsuarioProfissional
							WHERE 
							u.IdProfissao = ?
							AND U.AtendePresencialmenteProf = ?
							AND E.DataAtendimento = ?
							OR SI.IdSintomaAtendido = ? --NOVO
							OR AB.IdAbordagemAdotada = ? --NOVO
							OR U.Nome = ? --NOVO
                            GROUP BY 
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
                            u.IdUsuario,
                            Cep, 
                            Endereco,
                            IdUsuarioIugu,
                            IdPerfil,
                            RegistroCRPePsi,
                            RegistroePsiValidado,
                            OutroPublicoProf,
                            OutroIdiomaProf''', (IdProfissao, AtendePresencialmenteProf, DataAtendimento, IdSintomaAtendido, IdAbordagemAdotada, Nome))

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


def EfetuaLoginUsuarioData(email: str, senha: str, idperfil: int):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''SELECT top 1 idusuario, email, senha FROM usuario WHERE Email = ? AND senha = ? AND idperfil = ? ''',
                       (email, senha, idperfil))
        registros = cursor.fetchall()

        listabordagem = []
        if len(registros) > 0:
            user = BuscarUsuarioData(registros[0].idusuario)
            return user

        return None
    except Exception as mensagemErro:
        return mensagemErro
    return True


def ListarHistoricoAtendimento(IdProfissional: int):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''SELECT U.IdUsuario, U.Nome, U.BaseImage , U.DataCadastro  FROM usuario U 
                            INNER JOIN agendamento A ON U.IdUsuario = A.IdUsuario
                            WHERE A.IdUsuarioProfissional = ?
                            GROUP BY U.IdUsuario,U.Nome, U.BaseImage, U.DataCadastro ''', (IdProfissional))

        registros = cursor.fetchall()

        if len(registros) > 0:
            list = []
            for row in registros:
                dep = HistoricoAtendimentoModel(
                    IdUsuario=row[0],
                    Nome=row[1],
                    BaseImage=row[2],
                    DataCadastro=row[3]
                )
                list.append(dep)
            return list

        return None
    except Exception as mensagemErro:
        return mensagemErro
    return True


def CadastrarProntuarioData(pront: UsuarioProntuarioModel):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO [dbo].[usuarioProntuario]
                                ([IdUsuario]
                                ,[Prontuario])
                            VALUES
                                (?
                                ,?)''', (pront.IdUsuario, pront.Prontuario))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idUsuario = cursor.fetchone()[0]
        return True
    except Exception as mensagemErro:
        return False


def CadastrarColaboradoreEmpresaData(col: ColaboradoresEmpresa):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO [dbo].[colaboradoresEmpresa]
                            ([IDUSUARIOEMPRESA]
                            ,[REGISTRO]
                            ,[NOME]
                            ,[CPF]
                            ,[DATANASCIMENTO]
                            ,[VINCULO]
                            ,[CARGO]
                            ,[PLANODESAUDE]
                            ,[SUBSIDIOCORP]
                            ,[VALOR])
                        VALUES
                            (?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?)''', (col.IDUSUARIOEMPRESA, col.REGISTRO, col.NOME, col.CPF, col.DATANASCIMENTO, col.VINCULO, col.CARGO, col.PLANODESAUDE, col.SUBSIDIOCORP, col.VALOR))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        col.Id = cursor.fetchone()[0]
        return True
    except Exception as mensagemErro:
        return False


def AtualizaProntuarioData(pront: UsuarioProntuarioModel):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''UPDATE [dbo].[usuarioProntuario] SET Prontuario = ? WHERE IdUsuario = ? ''', (
            pront.Prontuario, pront.IdUsuario))
        cursor.commit()
        return True
    except Exception as mensagemErro:
        return False


def AtualizaSenhaUsuarioData(email: str, senhaatual: str, novasenha: str, IdUsuario: int):
    try:

        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('''SELECT top 1 IdUsuario, Email, Senha FROM usuario WHERE Email = ? AND Senha = ?''',
                       (email, senhaatual))
        registros = cursor.fetchall()

        if len(registros) > 0:
            cursor = conn.cursor()
            cursor.execute('''UPDATE usuario SET Senha = ? WHERE Email = ? AND Senha = ? AND IdUsuario = ? ''',
                           (novasenha, email, senhaatual, IdUsuario))
            cursor.commit()
            return True

        return False
    except Exception as mensagemErro:
        return False


def ListaProntuarioPacienteData(IdUsuario: int):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT * FROM [dbo].[usuarioProntuario] WHERE IdUsuario = ?''', (IdUsuario))

        registros = cursor.fetchall()

        if len(registros) > 0:
            list = []
            for row in registros:
                dep = UsuarioProntuarioModel(
                    Id=row[0],
                    IdUsuario=row[1],
                    Prontuario=row[2]
                )
                list.append(dep)
            return list

        return None
    except Exception as mensagemErro:
        return mensagemErro
    return True


def ListaColaboradoresEmpresaData(IdUsuarioEmpresa: int):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT * FROM [dbo].[colaboradoresEmpresa] WHERE IDUSUARIOEMPRESA = ?''', (IdUsuarioEmpresa))

        registros = cursor.fetchall()

        if len(registros) > 0:
            list = []
            for row in registros:
                dep = ColaboradoresEmpresa(
                    Id=row[0],
                    IDUSUARIOEMPRESA=row[1],
                    REGISTRO=row[2],
                    NOME=row[3],
                    CPF=row[4],
                    DATANASCIMENTO=row[5],
                    VINCULO=row[6],
                    CARGO=row[7],
                    PLANODESAUDE=row[8],
                    SUBSIDIOCORP=row[9],
                    VALOR=row[10]
                )
                list.append(dep)
            return list

        return None
    except Exception as mensagemErro:
        return mensagemErro
    return True
