from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class HobbieModel(BaseModel):
    IdHorario: int
    Tipo:str