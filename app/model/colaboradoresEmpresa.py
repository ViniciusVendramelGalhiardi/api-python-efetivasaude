from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class ColaboradoresEmpresa(BaseModel):
   Id: Optional[int]
   IDUSUARIOEMPRESA: Optional[int]
   REGISTRO: Optional[str]
   NOME: Optional[str]
   CPF:Optional[str]
   DATANASCIMENTO:Optional[str]
   VINCULO:Optional[str]
   CARGO:Optional[str]
   PLANODESAUDE:Optional[str]
   SUBSIDIOCORP:Optional[bool]
   VALOR:Optional[str]