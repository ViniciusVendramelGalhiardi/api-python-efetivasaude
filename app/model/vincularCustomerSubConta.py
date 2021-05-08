from typing import  Optional

class UsuarioVinculadoSubConta:
    IdUsuarioSubConta: Optional[str]
    IdUsuarioContaMaster: Optional[str]
    UserTokenDaSubConta: Optional[str]

    def __init__(self, IdUsuarioSubConta: Optional[str],  IdUsuarioContaMaster: Optional[str], UserTokenDaSubConta: Optional[str]) -> None:
        self.IdUsuarioSubConta = IdUsuarioSubConta
        self.IdUsuarioContaMaster = IdUsuarioContaMaster
        self.UserTokenDaSubConta = UserTokenDaSubConta
