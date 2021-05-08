from typing import  Optional

class UsuarioVinculadoSubConta:
    IdUsuarioSubConta: Optional[str]
    IdUsuarioContaMaster: Optional[int]

    def __init__(self, IdUsuarioSubConta: Optional[str],  IdUsuarioContaMaster: Optional[str]) -> None:
        self.IdUsuarioSubConta = IdUsuarioSubConta
        self.IdUsuarioContaMaster = IdUsuarioContaMaster
