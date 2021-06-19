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
from app.model.agendamentoConsultaModel import AgendamentoConsultaModel
from app.model.avaliacaoefModel import AvaliacaoEfModel


def efetuaAgendamento(agenda: AgendamentoConsultaModel):

    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[agendamento]
                        ([Idexpediente]
                        ,[IdUsuario]
                        ,[IdDependente]
                        ,[StatusPagamento]
                        ,[IdTransacao]
                        ,[statusAgendamento]
                        ,[IDSessao]
                        ,[IdUsuarioProfissional])
                    VALUES
                        (?,?,?,?,?,?,?)''',
                       (agenda.Idexpediente, agenda.IdUsuario, agenda.IdDependente,
                        agenda.StatusPagamento, agenda.IdTransacao, agenda.statusAgendamento, agenda.IDSessao, agenda.IdUsuarioProfissional))

        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        #IdAgenda = cursor.fetchone()[0]
        agenda.IdAgendamento = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return mensagemErro
    return agenda


def buscarAgendamentoProfissional(IdUsuarioProfissional: int):
    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()
        lista = cursor.execute(
            "SELECT * FROM [dbo].[agendamento] WHERE IdUsuario = ?;", (IdUsuarioProfissional))

        listcc = []
        for row in lista:
            cc = AgendamentoConsultaModel(
                IdAgendamento=row[0],
                Idexpediente=row[1],
                IdUsuario=row[2],
                IdDependente=row[3],
                StatusPagamento=row[4],
                IdTransacao=row[5],
                statusAgendamento=row[6],
                IDSessao=row[7]
            )
            listcc.append(cc)

        cursor.close()
        conn.close()
    except Exception as ms:
        return ''

    return listcc


def atualizarAgendamento(IdAgenda: int, StatusAgendamento: str):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''UPDATE [dbo].[agendamento] SET StatusPagamento = ? WHERE IdAgendamento = ?''',
                       (StatusAgendamento, IdAgenda))

        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        IdAgenda = cursor.fetchone()[0]
        #agenda.IdAgendamento = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return '{retorno:"' + 'Erro, verifique o IdAgenda e o Status passados como parametro.' + '"}'
    cursor.close()
    conn.close()
    return '{retorno:"' + 'Atualização efetuada com sucesso' + '"}'


def CadastraAvaliacaoEF(avaliacao: AvaliacaoEfModel):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[avaliacao]
                            ([IdProfissional]
                            ,[IdUsuario]
                            ,[NotaEfetivaSaude]
                            ,[NotaProfissional]
                            ,[DarContinuidade]
                            ,[Descricao_atendimento]
                            ,[Sugestoes])
                        VALUES
                            (?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?
                            ,?)''',
                       (avaliacao.IdProfissional, avaliacao.IdUsuario, avaliacao.NotaEfetivaSaude,
                        avaliacao.NotaProfissional, avaliacao.DarContinuidade, avaliacao.Descricao_atendimento,
                        avaliacao.Sugestoes))

        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        #IdAgenda = cursor.fetchone()[0]
        avaliacao.IdAvaliacao = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return mensagemErro
    return avaliacao


def buscarAvaliacaoProfissional(IdProfissional: int):
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute(
        "SELECT * FROM [dbo].[avaliacao] WHERE IdProfissional = ?;", (IdProfissional))

    list = []
    for row in lista:
        cc = AvaliacaoEfModel(
            IdAvaliacao=row[0],
            IdProfissional=row[1],
            IdUsuario=row[2],
            NotaEfetivaSaude=row[3],
            NotaProfissional=row[4],
            DarContinuidade=row[5],
            Descricao_atendimento=row[6],
            Sugestoes=row[7],
        )
        list.append(cc)

    cursor.close()
    conn.close()

    return list
