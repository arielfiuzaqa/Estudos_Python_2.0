from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Create the FastAPI app
app = FastAPI()

# Criando a lista de tarefas
class Todo(BaseModel):
    tarefa: str
    objetivo: str
    realizada: bool
    prazo: Optional[datetime] = None

list_tarefas = []

# Insere uma nova tarefa
@app.post("/inserir")
def inserir(todo: Todo):
    try:
        # Adiciona a tarefa à lista
        list_tarefas.append(todo)
        return {"message": "Tarefa inserida com sucesso!", "tarefa": todo}
    except Exception as e:
        return {"message": "Erro ao inserir a tarefa", "error": str(e)}

# Lista todas as tarefas com opção de filtro
@app.post("/listar")
def listar(opcao: int = 0):
        # Retorna a lista de tarefas
        if opcao == 0:
            return list_tarefas
        elif opcao == 1:
            return list(filter(lambda x: x.realizada == False, list_tarefas))
        elif opcao == 2:
            return list(filter(lambda x: x.realizada == True, list_tarefas))

# Lista todas as tarefas
@app.get("/listagemUnica/{id}")
def listar(id: int):
    try:
        # Retorna a tarefa com o id especificado
        return list_tarefas[id]
    except:
        return {"status": "Tarefa inexistente"}

# Altera o status da tarefa
@app.post("/alterarStatus")
def alterarStatus(id: int):
    try:
        # Altera o status da tarefa com o id especificado
        list_tarefas[id].realizada = not list_tarefas[id].realizada
        return {"status": "Tarefa alterada com sucesso", "tarefa": list_tarefas[id]}
    except:
        return {"status": "Tarefa inexistente"}
    
@app.post("/excluir")
def excluir(id: int):
    try:
        # Remove a tarefa com a posição do id especificado
        del list_tarefas[id]
    except:
        return {"status": "Tarefa inexistente"}
    return {"status": "Tarefa excluída com sucesso", "tarefa": list_tarefas[id]}        

    