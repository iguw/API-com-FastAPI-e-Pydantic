# API Gerenciador de Tarefas (FastAPI + Pydantic)

API RESTful com CRUD de tarefas, usando FastAPI, Pydantic e armazenamento em memória.

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/iguw/API-com-FastAPI-e-Pydantic.git
   cd API-com-FastAPI-e-Pydantic
   ```

2. Crie e ative o ambiente virtual:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

5. Acesse a documentação Swagger em http://127.0.0.1:8000/docs

## Autor

Guilherme Alves ([@iguw](https://github.com/iguw))