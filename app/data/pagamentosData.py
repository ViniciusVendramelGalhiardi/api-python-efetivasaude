import pyodbc
from settings import CONNECTION_STRING_DB
from app.model.formapgtoModel import FormaPagamentoModel
from app.factory.pagamentoFactory import UsuarioEntityToModel
from app.model.formapgtoModel import FormaPagamentoModel, Data, FormaPgtoEntity

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
                            (pgto.id
                            ,pgto.description
                            ,pgto.item_type
                            ,pgto.customer_id
                            ,pgto.data['brand']
                            ,pgto.data['holder_name']
                            ,pgto.data['display_number']
                            ,pgto.data['bin']
                            ,pgto.data['year']
                            ,pgto.data['month']
                            ,pgto.data['last_digits']
                            ,pgto.data['first_digits']
                            ,pgto.data['masked_number']))
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

        cursor.execute(''' SELECT [Id]
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
                        FROM [dbo].[formaPagamentoUsuarioIugu] WHERE [IdUsuarioIugu] = ? ''', (IdUsuarioIugu))
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