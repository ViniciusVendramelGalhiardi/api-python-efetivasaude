
from app.model.formapgtoModel import FormaPagamentoModel


def UsuarioEntityToModel(records, _dependentes):
        user = UsuarioEntity(
            Nome=records[0][0],
            Telefone=records[0][1],
            Email=records[0][2],
            Cidade=records[0][3],
            Estado=records[0][4],
            IdConheceu=records[0][5],
            TermosCondicoes=records[0][6],
            PoliticaPrivacidade=records[0][7],
            Apelido=records[0][8],
            EstadoCivil=records[0][9],
            PossuiFilhosQtd=records[0][10],
            IdHobbie=records[0][11],
            DataNascimento=records[0][12],
            Genero=records[0][13],
            IdProfissao=records[0][14],
            Cpf=records[0][15],
            idUsuario=records[0][16],
            Dependente=records[0][17],
            Dependentes=_dependentes
        )

        return user


def FormaPagtotyToModel(obj):
        metodoPagamentoUsuario = FormaPagamentoModel(response.json()['id'],response.json()['description'], response.json()['item_type'],
                            response.json()['customer_id'],response.json()['data'])
        return metodoPagamentoUsuario