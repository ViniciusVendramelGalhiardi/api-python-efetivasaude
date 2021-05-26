import pyodbc 
from settings import CONNECTION_STRING_DB
from app.model.perfisModel import PerfisModel
from app.model.listarPerfilModel import ListarPerfilModel
from app.model.listarAbordagemModel import ListarAbordagemModel
from app.model.listarHobbiesModel import ListarHobbiesModel
from app.model.listarCRPModel import ListarCRPModel
from app.model.listarHorarioTrabalhoModel import ListarHorarioTrabalhoModel
from app.model.listaridiomasModel import ListarIdiomasModel
from app.model.listarNosConheceuModel import ListarNosConheceuModel
from app.model.listarPlanosModel import ListarPlanosModel
from app.model.listarProfissaoModel import ListarProfissaoModel
from app.model.listarSintomasModel import ListarSintomasModel
from app.model.listarUsaPlataformaModel import ListarUsaPlataformaModel



def buscaPerfis():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from Perfis")

    listcc = []
    for row in lista:
        cc = ListarPerfilModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc

def buscaAbordagem():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from abordagemAdotada")
      
    listcc = []
    for row in lista:
        cc = ListarAbordagemModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaHobbie():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from hobbie")
    
    listcc = []
    for row in lista:
        cc = ListarHobbiesModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaCRP():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from conselhoRegionalCRP")
    
    listcc = []
    for row in lista:
        cc = ListarCRPModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaHorarioTrabalho():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from horarioTrabalho")
    
    listcc = []
    for row in lista:
        cc = ListarHorarioTrabalhoModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc

def buscaIdiomas():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from idiomas")
    
    listcc = []
    for row in lista:
        cc = ListarIdiomasModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaNosConheceu():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from nosConheceu")
    listcc = []
    for row in lista:
        cc = ListarNosConheceuModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaPlanos():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from planos")
    listcc = []
    for row in lista:
        cc = ListarPlanosModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaProfissao():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from profissao")
    
    listcc = []
    for row in lista:
        cc = ListarProfissaoModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc


def buscaSintomas():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from sintomas")
    listcc = []
    for row in lista:
        cc = ListarSintomasModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc



def buscaUsarPlataforma():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from usarPlataforma")

    listcc = []
    for row in lista:
        cc = ListarUsaPlataformaModel(
                Id=row[0],
                Nome= row[1]
        )
        listcc.append(cc)

    return listcc



    