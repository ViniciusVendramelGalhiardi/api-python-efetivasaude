import pyodbc 
from settings import CONNECTION_STRING_DB
from app.model.perfisModel import PerfisModel
from app.entity.usuarioEntity import UsuarioEntity
from app.entity.profissionalEntity import ProfissionalEntity
from app.entity.empresaEntity import EmpresaEntity

def CadastraUsuario(uEntity: UsuarioEntity):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from Perfis")
    return lista

def CadastraProfissional(pEntity: ProfissionalEntity):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from Perfis")
    return lista

def CadastraEmpresa(eEntity: EmpresaEntity):
    conn = pyodbc.connect(CONNECTION_STRING_DB)
    cursor = conn.cursor()
    lista = cursor.execute("select * from Perfis")
    return lista