from pydantic import BaseModel, Field


class TarefaBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100, examples=["Estudar FastAPI"])
    descricao: str | None = Field(default=None, max_length=300, examples=["Ler a documentação oficial"])
    concluida: bool = False


class TarefaCreate(TarefaBase):
    """Dados de entrada do POST."""

class TarefaUpdate(TarefaBase):
    """Dados de entrada do PUT."""

class Tarefa(TarefaBase):
    """Dados de saída."""
    id: int