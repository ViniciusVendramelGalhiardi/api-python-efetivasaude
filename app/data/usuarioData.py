import pyodbc 
from settings import CONNECTION_STRING_DB
from app.model.perfisModel import PerfisModel
from app.entity.usuarioEntity import UsuarioEntity
from app.entity.profissionalEntity import ProfissionalEntity
from app.entity.empresaEntity import EmpresaEntity


def CadastraUsuario(uEntity: UsuarioEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO usuario (Nome, Telefone,Email,Cidade, Estado, IdConheceu, Senha, TermosCondicoes,PoliticaPrivacidade, Apelido, EstadoCivil, PossuiFilhosQtd, IdHobbie,DataNascimento, Genero, IdProfissao,Cpf , Dependente) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )',
                 (uEntity.Nome, uEntity.Telefone, uEntity.Email,uEntity.Cidade,uEntity.Estado,uEntity.IdConheceu,uEntity.Senha,uEntity.TermosCondicoes,
                 uEntity.PoliticaPrivacidade, uEntity.Apelido, uEntity.EstadoCivil, uEntity.PossuiFilhosQtd, uEntity.IdHobbie, uEntity.DataNascimento,
                 uEntity.Genero, uEntity.IdConheceu, uEntity.Cpf, uEntity.Dependente))

        #commit the transaction
        cursor.commit()
    except Exception as mensagemErro: 
         return mensagemErro
    return lista

def CadastraProfissional(pEntity: ProfissionalEntity, IdPerfil: int):
    
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuario (Nome, Telefone,Email,Cidade, Estado, IdConheceu, Senha, TermosCondicoes,PoliticaPrivacidade, Apelido, EstadoCivil, PossuiFilhosQtd, IdHobbie,DataNascimento, Genero, IdProfissao,Cpf , Dependente,IdHorarioTrabalhoProf,IdUsarPlataformaProf,IdConselhoRegionalProf,PossuiCNPJProf,TrabalharComCNPJProf,CnPj,CartaApresentacaoProf,IdAbordagemProf,DuracaoAtendimentoProf, AtendePlanoDeSaudeProf,ReciboReembolsavelProf,AtendePresencialmenteProf,PrimeiroClienteCobraProf,PrimeiroClienteValorFixoProf,EmpresasParceirasDescontoProf,ValorPorSessaoProf) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (pEntity.Nome, pEntity.Telefone,pEntity.Email,pEntity.Cidade,pEntity.Estado, pEntity.IdConheceu, pEntity.Senha, pEntity.TermosCondicoes,pEntity.PoliticaPrivacidade,
        pEntity.Apelido, pEntity.EstadoCivil, pEntity.PossuiFilhosQtd, pEntity.IdHobbie,pEntity.DataNascimento, pEntity.Genero, pEntity.IdProfissao,pEntity.Cpf , pEntity.Dependente,pEntity.IdHorarioTrabalhoProf,pEntity.IdUsarPlataformaProf,pEntity.IdConselhoRegionalProf,pEntity.PossuiCNPJProf,pEntity.TrabalharComCNPJProf,pEntity.CnPj,pEntity.CartaApresentacaoProf,pEntity.IdAbordagemProf,pEntity.DuracaoAtendimentoProf, pEntity.AtendePlanoDeSaudeProf,pEntity.ReciboReembolsavelProf,pEntity.AtendePresencialmenteProf,pEntity.PrimeiroClienteCobraProf,pEntity.PrimeiroClienteValorFixoProf,pEntity.EmpresasParceirasDescontoProf,pEntity.ValorPorSessaoProf))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        idUsuario = cursor.fetchone()[0]

        if pEntity.Dependentes is not None:
            for item in pEntity.Dependentes:
                cursor.execute('INSERT INTO Dependente (Nome, Apelido, DataNascimento, Genero, Telefone, Email, CPF, IdUsuario) VALUES(?,?,?,?,?,?,?,?)',
                (item.Nome, item.Apelido,item.DataNascimento,item.Genero,item.Telefone, item.Email, item.Cpf, idUsuario))
                cursor.commit()

        if pEntity.FormacoesProf is not None:
            for item in pEntity.FormacoesProf:
                cursor.execute('INSERT INTO formacaoAcademica (IdUsuario, InstituicaoEnsino, NomeCurso,NivelAcademico,AnoInicio,AnoTermino,DescricaoCurso,Anexo) VALUES (?,?, ?, ?, ?, ?, ?, ?)',
                (idUsuario, item.InstituicaoEnsino,item.NomeCurso,item.NivelAcademico,item.AnoInicio, item.AnoTermino, item.DescricaoCurso, item.Anexo))
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
                (item.Endereco,item.Numero,item.Conjunto,item.Bairro,item.Cidade,item.Estado,item.Cep, idUsuario))
                cursor.commit()

        if pEntity.ContasCorrente is not None:
            for item in pEntity.ContasCorrente:
                cursor.execute('INSERT INTO ContaCorrente (Banco,Agencia,ContaCorrente,DigitoVerificador,IdUsuario) VALUES (?,?,?,?,?)',
                (item.Banco,item.Agencia,item.ContaCorrente,item.DigitoVerificador, idUsuario))
                cursor.commit()

    except Exception as mensagemErro: 
        return mensagemErro

    return lista

def CadastraEmpresa(eEntity: EmpresaEntity, IdPerfil: int):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO [dbo].[usuario] (Nome, Telefone, Email, Cidade, Estado, IdConheceu, Senha, TermosCondicoes, PoliticaPrivacidade, Apelido, NomeEmpresaEmp, TelefoneCorporativoEmp, EmailCorporativoEmp,SiteEmpr,LinkedinEmpr, InstagramEmp,CargoFuncaoEmp,NumeroColaboradoresEmp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (eEntity.Nome, eEntity.Telefone, eEntity.Email, eEntity.Cidade, eEntity.Estado, eEntity.IdConheceu, eEntity.Senha, eEntity.TermosCondicoes, eEntity.PoliticaPrivacidade, eEntity.Apelido, eEntity.NomeEmpresaEmp, eEntity.TelefoneCorporativoEmp, eEntity.EmailCorporativoEmp,eEntity.SiteEmpr,eEntity.LinkedinEmpr, eEntity.InstagramEmp,eEntity.CargoFuncaoEmp,eEntity.NumeroColaboradoresEmp))    
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
                (item.Banco,item.Agencia,item.ContaCorrente,item.DigitoVerificador, idUsuario))
                cursor.commit()

    except Exception as mensagemErro:
            return mensagemErro

    return lista