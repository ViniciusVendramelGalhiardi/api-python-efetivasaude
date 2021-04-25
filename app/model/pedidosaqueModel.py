from typing import  Optional
from datetime import datetime  

class PedidoSaqueModel:
    IdSaque: Optional[int]
    IdSubConta: Optional[str]
    ValorSaque: Optional[str]
    IdUsuario: Optional[int]
    DataSolicitacao: Optional[datetime]
    IdRetorno: Optional[str]


    def __init__(self, IdSaque: Optional[int],  IdSubConta: Optional[str], 
                ValorSaque: Optional[str], IdUsuario: Optional[int], DataSolicitacao:Optional[datetime], 
                IdRetorno:Optional[str]) -> None:
        self.IdSaque = IdSaque
        self.IdSubConta = IdSubConta
        self.ValorSaque = ValorSaque
        self.IdUsuario = IdUsuario
        self.DataSolicitacao = DataSolicitacao
        self.IdRetorno = IdRetorno