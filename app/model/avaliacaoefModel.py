from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class AvaliacaoEfModel(BaseModel):
    IdAvaliacao: Optional[int]
    IdProfissional: Optional[int]
    IdUsuario: Optional[int]
    NotaEfetivaSaude: Optional[int]
    NotaProfissional: Optional[int]
    DarContinuidade: Optional[int]
    Descricao_atendimento: Optional[str]
    Sugestoes: Optional[str]