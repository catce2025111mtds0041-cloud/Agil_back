from fastapi import FastAPI
from models import Paciente

app = FastAPI()

pacientes = []

@app.get("/")
def inicio():
    return {"mensagem": "API Enfermeiro Ágil funcionando"}

@app.get("/pacientes")
def listar_pacientes():
    return pacientes

@app.post("/pacientes")
def criar_paciente(paciente: Paciente):
    pacientes.append(paciente)
    return paciente

@app.get("/pacientes/{paciente_id}")
def buscar_paciente(paciente_id: int):
    for paciente in pacientes:
        if paciente.id == paciente_id:
            return paciente
    return {"erro": "Paciente não encontrado"}