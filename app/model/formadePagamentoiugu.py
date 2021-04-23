from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class FormaDePagamentoIugu(BaseModel):
   tokenGeradoIugu: Optional[str]
   idClienteIugu: Optional[str]
   Descricao: Optional[str]
   CartaoPrincipal:Optional[bool]