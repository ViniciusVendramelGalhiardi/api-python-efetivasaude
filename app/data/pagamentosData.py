import pyodbc
from settings import CONNECTION_STRING_DB
from app.model.formapgtoModel import FormaPagamentoModel
from app.factory.pagamentoFactory import UsuarioEntityToModel
from app.model.formapgtoModel import FormaPagamentoModel, Data, FormaPgtoEntity
from app.model.responsePagamentoModel import ResponsePagamentoModel
from datetime import datetime
from app.model.subContaResponseModel import SubContaResponseModel
from app.entity.subContaEntity import SubContaEntity
from app.model.verificacaoContaModel import VerificacaoContaModel
from app.model.pedidosaqueModel import PedidoSaqueModel

def CadastraFormaPgtoUsuario(pgto: FormaPagamentoModel):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[formaPagamentoUsuarioIugu]
                            ([IdFormaPgtoIugu]
                            ,[DescricaoPgto]
                            ,[TipoFormaPgto]
                            ,[IdUsuarioIugu]
                            ,[BandeiraCartao]
                            ,[NomeCartao]
                            ,[NumeroCartao]
                            ,[Bin]
                            ,[AnoVencimento]
                            ,[Mes]
                            ,[UltimosDigitos]
                            ,[PrimeirosDigitos]
                            ,[NumeroMascara])
                        VALUES
                            (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (pgto.id, pgto.description, pgto.item_type, pgto.customer_id, pgto.data['brand'], pgto.data['holder_name'], pgto.data['display_number'], pgto.data['bin'], pgto.data['year'], pgto.data['month'], pgto.data['last_digits'], pgto.data['first_digits'], pgto.data['masked_number']))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        Id = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return ''
    return Id


def BuscarFormasPagamento(IdUsuarioIugu: str):
    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute(''' SELECT TOP 1 [Id]
                            ,[IdFormaPgtoIugu]
                            ,[DescricaoPgto]
                            ,[TipoFormaPgto]
                            ,[IdUsuarioIugu]
                            ,[BandeiraCartao]
                            ,[NomeCartao]
                            ,[NumeroCartao]
                            ,[Bin]
                            ,[AnoVencimento]
                            ,[Mes]
                            ,[UltimosDigitos]
                            ,[PrimeirosDigitos]
                            ,[NumeroMascara]
                        FROM [dbo].[formaPagamentoUsuarioIugu] WHERE [IdUsuarioIugu] = ? ORDER BY Id DESC ''', (IdUsuarioIugu))
        records = cursor.fetchall()

        result = FormaPgtoEntity(records[0][0],
                                 records[0][1],
                                 records[0][2],
                                 records[0][3],
                                 records[0][4],
                                 records[0][5],
                                 records[0][6],
                                 records[0][7],
                                 records[0][8],
                                 records[0][9],
                                 records[0][10],
                                 records[0][11],
                                 records[0][12],
                                 records[0][13])

    except Exception as mensagemErro:
        return mensagemErro
    return result


def GravaTransacaoAutorizadaDb(subconta: SubContaResponseModel, IdUsuarioIugu: str):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[transacao]
                            ([status]
                            ,[info_message]
                            ,[reversible]
                            ,[token]
                            ,[brand]
                            ,[bin]
                            ,[success]
                            ,[url]
                            ,[pdf]
                            ,[identification]
                            ,[invoice_id]
                            ,[LR]
                            ,[idUsuarioIugu]
                            ,[DataTransacao])
                        VALUES
                            (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (pgto.status, pgto.info_message, pgto.reversible, pgto.token, pgto.brand, pgto.bin, pgto.success, pgto.url, pgto.pdf, pgto.identification, pgto.invoice_id, pgto.lr, IdUsuarioIugu, datetime.now()))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        Id = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return ''
    return Id


def GravaDadosSubContaProfissional(sub: SubContaResponseModel, IdUsuarioIugu: str):
    try:
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[subcontasiugu]
                                ([IdSubConta]
                                ,[Nome]
                                ,[TokenPrd]
                                ,[TokenDev]
                                ,[TokenUsuario]
                                ,[ComissaoBankSplipCents]
                                ,[ComissaoBankSplipPorcentagem]
                                ,[ValorComissao]
                                ,[DataCriacao]
                                ,[ComissaoCartaoCredito]
                                ,[PorcentagemCartaoCredito]
                                ,[IdComissao]
                                ,[PercentualFixo]
                                ,[PermiteAgregados]
                                ,[ComissaoPix]
                                ,[ComissaoPixPorcentagem]
                                ,[TokenContaReceptador]
                                ,[SplitId]
                                ,[UltimaAtualizacao]
                                ,[IdUsuarioIugu]
                                ,[StatusConta])
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (sub.account_id, sub.name, sub.live_api_token, sub.test_api_token, sub.user_token, sub.commissions['bank_slip_cents'], sub.commissions['bank_slip_percent'], sub.commissions['cents'], sub.commissions['created_at'], sub.commissions['credit_card_cents'], sub.commissions['credit_card_percent'], sub.commissions['id'], sub.commissions['percent'], sub.commissions['permit_aggregated'], sub.commissions['pix_cents'], sub.commissions['pix_percent'], sub.commissions['recipient_account_id'], sub.commissions['split_id'], sub.commissions['updated_at'], IdUsuarioIugu, False))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        Id = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return ''
    return Id


def BuscarSubConta(IdUsuarioIugu: str):
    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute(''' SELECT TOP 1 
                                 [Id]
                                ,[IdSubConta]
                                ,[Nome]
                                ,[TokenPrd]
                                ,[TokenDev]
                                ,[TokenUsuario]
                                ,[ComissaoBankSplipCents]
                                ,[ComissaoBankSplipPorcentagem]
                                ,[ValorComissao]
                                ,[DataCriacao]
                                ,[ComissaoCartaoCredito]
                                ,[PorcentagemCartaoCredito]
                                ,[IdComissao]
                                ,[PercentualFixo]
                                ,[PermiteAgregados]
                                ,[ComissaoPix]
                                ,[ComissaoPixPorcentagem]
                                ,[TokenContaReceptador]
                                ,[SplitId]
                                ,[UltimaAtualizacao]
                                ,[IdUsuarioIugu]
                                ,[StatusConta]
                            FROM [dbo].[subcontasiugu] WHERE [IdUsuarioIugu] = ? ORDER BY Id DESC ''', (IdUsuarioIugu))
        records = cursor.fetchall()

        result = SubContaEntity(records[0][0],
                                records[0][1],
                                records[0][2],
                                records[0][3],
                                records[0][4],
                                records[0][5],
                                records[0][6],
                                records[0][7],
                                records[0][8],
                                records[0][9],
                                records[0][10],
                                records[0][11],
                                records[0][12],
                                records[0][13],
                                records[0][14],
                                records[0][15],
                                records[0][16],
                                records[0][17],
                                records[0][18],
                                records[0][19],
                                records[0][20],
                                records[0][21])

    except Exception as mensagemErro:
        return mensagemErro
    return result


def GravaVerificacaoContaRetorno(response: VerificacaoContaModel):
    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[VerificacaoConta]
                            ([IdSubConta]
                            ,[IdPerfil]
                            ,[TokenSubContaPrd]
                            ,[RetornoJson]
                            ,[IdUsuario]
                            ,[IdUsuarioIugu])
                            VALUES (?,?,?,?,?,?)''',
                       (response.IdSubConta, response.IdPerfil,response.TokenSubContaPrd, response.RetornoJson, response.IdUsuario, response.IdPerfil))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        Id = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return mensagemErro
    return Id


def GravaSolicitacaoSaque(response: PedidoSaqueModel):
    try:
        vlrconexao = CONNECTION_STRING_DB
        conn = pyodbc.connect(CONNECTION_STRING_DB)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO [dbo].[pedidosaque]
                                ([IdSubConta]
                                ,[ValorSaque]
                                ,[IdUsuario]
                                ,[DataSolicitacao]
                                ,[IdRetorno])
                            VALUES (?,?,?,?,?)''',
                       (response.IdSubConta, response.ValorSaque,response.IdUsuario, response.DataSolicitacao,
                        response.IdRetorno))
        cursor.commit()
        cursor.execute("SELECT @@IDENTITY AS ID;")
        Id = cursor.fetchone()[0]

    except Exception as mensagemErro:
        return mensagemErro
    return Id
