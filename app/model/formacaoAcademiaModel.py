from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class FormacaoAcademicaModel(BaseModel):
   IdFormacao: int
   IdUsuario: int
   InstituicaoEnsino: str
   NomeCurso : str
   NivelAcademico: str
   AnoInicio: int
   AnoTermino: int
   DescricaoCurso: str
   Anexo: str
   
