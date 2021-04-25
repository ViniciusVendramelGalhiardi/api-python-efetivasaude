from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class SubContaRequestModel(BaseModel):
    IdUsuarioIugu:str
    ApiTokenIugu: str
    ComissaoPorcentagem:str
    ValorEmRealComissao:str
    NomeSubConta:str