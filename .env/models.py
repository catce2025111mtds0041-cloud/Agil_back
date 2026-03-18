from pydantic import BaseModel
from typing import List, Optional

class Paciente(BaseModel):
    id: int
    nome: str
    idade: int
    historico_medico: Optional[str] = None


class Enfermeiro(BaseModel):
    id: int
    nome: str
    email: str
    registro_profissional: str


class Prontuario(BaseModel):
    id: int
    paciente_id: int
    descricao: str
    sinais_vitais: str


class Medicacao(BaseModel):
    id: int
    paciente_id: int
    nome: str
    dosagem: str
    horario: str


class Tarefa(BaseModel):
    id: int
    paciente_id: int
    descricao: str
    data: str
    status: str