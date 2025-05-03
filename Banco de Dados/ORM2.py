from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Pessoas # Importando a classe Pessoas do arquivo ORM.py

def RetornaSession():
    
    # Usando Banco de Dados Local com SQLite
    # Conexão com banco SQLite - ele criará o arquivo banco.db na pasta do script
    engine = create_engine("sqlite:///Banco de Dados/Dados/banco.db", echo=True)

    # Sessão e base
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
session = RetornaSession()

x = Pessoas(nome='Lucas', 
            usuario='Lukinha69', 
            senha=171869)
y = Pessoas(nome='Fabio', 
            usuario='Cofabi123', 
            senha=181899)

#session.add(x) # Adiciona o objeto à sessão
session.add_all([x, y]) # Adiciona todos os objetos à sessão
session.rollback() # Desfaz as alterações na sessão
session.commit() # Salva as alterações no banco de dados
