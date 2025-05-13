from fastapi import FastAPI

app = FastAPI()

@app.get("/home") # 127.0.0.1:8000/home
def root():
    return {"message": "Home"}
@app.get("/cadastro") # 127.0.0.1:8000/cadastro
def root():
    return {"message": "Cadastro"}
@app.get("/login") # 127.0.0.1:8000/login
def root():
    return {"message": "Login"}

