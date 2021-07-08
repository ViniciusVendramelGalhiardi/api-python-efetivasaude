from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class HistoricoAtendimentoModel(BaseModel):
   IdUsuario: Optional[int]
   Nome: Optional[str]
   BaseImage: Optional[str]
   DataCadastro:Optional[str]