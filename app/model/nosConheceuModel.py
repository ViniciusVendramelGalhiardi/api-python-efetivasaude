from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class NosConheceuModel(BaseModel):
    IdNosConheceu: int
    Tipos:str