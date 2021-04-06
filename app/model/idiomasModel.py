from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class IdiomasModel(BaseModel):
    Id: int
    Idioma:str