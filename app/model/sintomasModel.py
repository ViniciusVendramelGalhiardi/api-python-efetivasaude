from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class SintomasModel(BaseModel):
    IdSintoma: int
    Tipo:str