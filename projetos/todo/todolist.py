from fastapi import FastAPI # Essa linha importa a classe FastAPI, que é o núcleo do framework.
from pydantic import BaseModel # Você usa BaseModel para definir os dados de entrada e saída da sua API, com validação automática de tipos.
from typing import Optional # Optional é usado para indicar que um campo pode ser ausente.
from datetime import date

# Create the FastAPI app
app = FastAPI()

# Criando a lista de tarefas
class Todo(BaseModel):
    tarefa: str
    objetivo: str
    realizada: bool
    prazo: Optional[date]  # Pode estar ausente

# Lista de tarefas inicialmente vazia
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

# Exclui uma tarefa pelo id
@app.post("/excluir")
def excluir(id: int):
    try:
        # Remove a tarefa com a posição do id especificado
        del list_tarefas[id]
    except:
        return {"status": "Tarefa inexistente"}
    return {"status": "Tarefa excluída com sucesso", "tarefa": list_tarefas[id]}        

    