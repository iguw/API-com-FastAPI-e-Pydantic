from fastapi import FastAPI

app = FastAPI(
    title="API Gerenciador de Tarefas",
    description="API RESTful simples com CRUD de tarefas em memória.",
    version="1.0.0",
)


@app.get("/", tags=["Raiz"])
def raiz():
    return {"mensagem": "API de Tarefas no ar!"}