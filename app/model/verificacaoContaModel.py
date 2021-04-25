from typing import  Optional

class VerificacaoContaModel:
    IdSubConta: Optional[str]
    IdPerfil: Optional[int]
    TokenSubContaPrd: Optional[str]
    RetornoJson: Optional[str]
    IdUsuario: Optional[int]
    IdUsuarioIugu: Optional[str]


    def __init__(self, IdSubConta: Optional[str],  IdPerfil: Optional[int], TokenSubContaPrd: Optional[str], RetornoJson: Optional[str], IdUsuario:Optional[int], IdUsuarioIugu: Optional[str]) -> None:
        self.IdSubConta = IdSubConta
        self.IdPerfil = IdPerfil
        self.TokenSubContaPrd = TokenSubContaPrd
        self.RetornoJson = RetornoJson
        self.IdUsuario = IdUsuario
        self.IdUsuarioIugu = IdUsuarioIugu