# Contendo a lógica da nossa API
from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Pessoas, Token, CONN
from secrets import token_urlsafe # Importando a biblioteca para gerar o token

app = FastAPI() # Criando a instância do FastAPI

def conectarBanco():
    # Usando Banco de Dados Local com SQLite
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine) # Criando a sessão
    session = Session() # Criando a sessão
    return session # Retornando a sessão

@app.post("/cadastro")
def cadastro(nome: str, usuario: str, senha: str):
    session = conectarBanco()
    usuario = session.query(Pessoas).filter_by(usuario=usuario, senha=senha).all() # Verificando se o usuário já existe
    if len(usuario) == 0:
        x = Pessoas(nome=nome, usuario=usuario, senha=senha) # Criando o objeto
        session.add(x)
        session.commit()
        return {"status": "Usuário cadastrado com sucesso!"}
    elif len(usuario) > 0:
        return {"status": "Usuário já existe!"}


