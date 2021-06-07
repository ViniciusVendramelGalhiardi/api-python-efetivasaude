from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class DefaultValueModel(BaseModel):
    value: Optional[str]