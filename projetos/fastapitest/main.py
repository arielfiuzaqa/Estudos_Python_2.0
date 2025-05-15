# Contendo a lógica da nossa API
from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Pessoa, Token, CONN
from secrets import token_hex # Importando a biblioteca para gerar o token

app = FastAPI() # Criando a instância do FastAPI

def conectarBanco():
    # Usando Banco de Dados Local com SQLite
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine) # Criando a sessão
    return Session() # Retornando a sessão

@app.post("/cadastro")
def cadastro(name: str, user: str, password: str):
    session = conectarBanco()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=password).all() # Verificando se o usuário já existe
    if len(usuario) == 0:
        x = Pessoa(nome=name, usuario=user, senha=password) # Criando o objeto
        session.add(x)
        session.commit()
        return {"status": "Usuário cadastrado com sucesso!"}
    elif len(usuario) > 0:
        return {"status": "Usuário já existe!"}

@app.post("/login")
def login(usuario: str, senha: str):
    session = conectarBanco()
    user = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all() # Verificando se o usuário existe
    if len(user) == 0:
        return {"status": "Usuário não encontrado!"}
    
    while True:
        token = token_hex(50) # Gerando o token
        tokenExiste = session.query(Token).filter_by(token=token).all() # Verificando se o token já existe
        if len(tokenExiste) == 0:
            pessoaExiste = session.query(Pessoa).filter_by(id_usuario=user[0].id).all() # Verificando se a pessoa existe
            if len(pessoaExiste) == 0:
                novoToken = Token(id_usuario=user[0].id, token=token) # Criando o objeto
                session.add(novoToken)
            elif len(pessoaExiste) > 0:
                pessoaExiste[0].token = token
                session.commit()
                break        
    return token # Retornando o token
