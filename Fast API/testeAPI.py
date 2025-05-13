from fastapi import FastAPI

app = FastAPI()

'''@app.get("/home") # 127.0.0.1:8000/home
def root():
    return {"message": "Home"}
@app.get("/cadastro") # 127.0.0.1:8000/cadastro
def root():
    return {"message": "Cadastro"}
@app.get("/login") # 127.0.0.1:8000/login
def root():
    return {"message": "Login"}
'''
usuario = [(1, "Lucas", "123456"), (2, "João", "123456"), (3, "Maria", "123456")]

#127.0.0.1:8000/docs
'''@app.get("/usuario/{id}")  # 
def main(id: int):
    for i in usuario:
        if i[0] == int(id):
            return {"id": i[0], "nome": i[1], "senha": i[2]}
    return {"message": "Usuario não encontrado"}'''

'''@app.post("/usuario")
def main(nome: str):
    for i in usuario:
        if i[1] == nome:
            return {"id": i[0], "nome": i[1], "senha": i[2]}
    return {"message": "Usuario não encontrado"}'''

from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str

lista = [
    Usuario(id=1, nome="Lucas", senha="123456"),
    Usuario(id=2, nome="João", senha="123456"),
    Usuario(id=3, nome="Maria", senha="123456")
    ]

# Cadastra um novo usuario
@app.post("/usuario")
def main(usuario: Usuario):
    lista.append(usuario)
    return "usuario adicionado com sucesso"

# Mostra todos os usuarios cadastrados
@app.get("/usuarioListar")
def main():
    return lista