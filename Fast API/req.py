import requests
from ..projetos.todo.todolist import Todo
from testeAPI import app

# Get
retorno = requests.get("http://127.0.0.1:8000")
print(retorno.json())
# Post
retorno = requests.post("http://127.0.0.1:8000")
print(retorno.json())