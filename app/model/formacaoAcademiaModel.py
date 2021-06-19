from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator


class FormacaoAcademicaModel(BaseModel):
    IdUsuario: Optional[int]
    IdFormacao: Optional[int]
    InstituicaoEnsino: Optional[str]
    NomeCurso: Optional[str]
    NivelAcademico: Optional[str]
    AnoInicio: Optional[str]
    AnoTermino: Optional[str]
    DescricaoCurso: Optional[str]
    Anexo: Optional[str]
