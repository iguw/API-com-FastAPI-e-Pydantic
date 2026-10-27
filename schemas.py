from pydantic import BaseModel, Field


class TarefaBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100, examples=["Estudar FastAPI"])
    descricao: str | None = Field(default=None, max_length=300, examples=["Ler a documentação oficial"])
    concluida: bool = False


"""dados do post"""
class TarefaCreate(TarefaBase):

 """dados do put"""
class TarefaUpdate(TarefaBase):

 """dados de saida."""
class Tarefa(TarefaBase):
    id: int