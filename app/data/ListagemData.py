import pyodbc 
from settings import CONNECTION_STRING_DB
from app.model.perfisModel import PerfisModel

def buscaPerfis():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from Perfis")
    return lista


def buscaAbordagem():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from abordagemAdotada")
    return lista


def buscaHobbie():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from hobbie")
    return lista


def buscaCRP():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from conselhoRegionalCRP")
    return lista


def buscaHorarioTrabalho():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from horarioTrabalho")
    return lista


def buscaIdiomas():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from idiomas")
    return lista


def buscaNosConheceu():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from nosConheceu")
    return lista


def buscaPlanos():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from planos")
    return lista


def buscaProfissao():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from profissao")
    return lista


def buscaSintomas():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from sintomas")
    return lista


def buscaUsarPlataforma():
    vlrconexao = CONNECTION_STRING_DB
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from usarPlataforma")
    return lista