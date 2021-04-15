from app.model.usuarioModel import UsuarioModel

def CadastrarU(nome: str, idade: str):
    nomeAtual = nome + " tem " + idade + " anos"
    return nomeAtual