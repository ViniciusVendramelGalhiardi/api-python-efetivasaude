from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class RequestPagamentoModel(BaseModel):
   DescricaoProduto: Optional[str]
   Valor: Optional[str]
   IdFormaPagtoIugu:Optional[str]
   IdUsuarioSubConta:Optional[str]
   EmailUsuario: Optional[str]
   tokenSubConta: Optional[str]

