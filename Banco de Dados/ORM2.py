from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usando Banco de Dados Local com SQLite
# Conexão com banco SQLite - ele criará o arquivo banco.db na pasta do script
engine = create_engine("sqlite:///Banco de Dados/Dados/banco.db", echo=True)

# Sessão e base
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

