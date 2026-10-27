from fastapi import FastAPI, HTTPException
from schemas import Tarefa, TarefaCreate, TarefaUpdate

app = FastAPI(
    title="API Gerenciador de Tarefas",
    description="API RESTful simples com CRUD de tarefas em memória.",
    version="1.0.0",
)
#BD
tarefas_db: dict[int, Tarefa] = {}
proximo_id = 1

@app.get("/", tags=["Raiz"])
def raiz():
    return {"mensagem": "API de Tarefas no ar!"}

@app.get("/tarefas", response_model=list[Tarefa], tags=["Tarefas"])
def listar_tarefas(concluida: bool | None = None):
    tarefas = list(tarefas_db.values())
    if concluida is not None:
        tarefas = [t for t in tarefas if t.concluida == concluida]
    return tarefas


@app.get("/tarefas/{tarefa_id}", response_model=Tarefa, tags=["Tarefas"])
def buscar_tarefa(tarefa_id: int):
    tarefa = tarefas_db.get(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

#tarefa
@app.post("/tarefas", response_model=Tarefa, status_code=201, tags=["Tarefas"])
def criar_tarefa(dados: TarefaCreate):
    global proximo_id
    tarefa = Tarefa(id=proximo_id, **dados.model_dump())
    tarefas_db[proximo_id] = tarefa
    proximo_id += 1
    return tarefa
