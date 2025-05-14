# Contendo as tabelas do banco de dados
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Caminho do banco de dados
CONN = "sqlite:///projetos/Fast API/banco_api.db" # Caminho do banco de dados
# Usando Banco de Dados Local com SQLite
engine = create_engine(CONN, echo=True)

# Sessão e base
Session = sessionmaker(bind=engine) # Criando a sessão
session = Session() 
Base = declarative_base() # Declarando a base

# Definindo a tabela de Pessoas
class Pessoas(Base):
    __tablename__ = 'Pessoas' # Nome da tabela
    id = Column(Integer, primary_key=True) # Chave primária
    nome = Column(String(50)) # Nome da pessoa
    usuario = Column(String(20)) # Nome de usuário
    senha = Column(String(10)) # Senha
    data_cadastro = Column(String, default=datetime.datetime.now()) # Data de cadastro

# Class para os tokens para evitar o login de um usuario diferente
class Token(Base):
    __tablename__ = 'Token' # Nome da tabela
    id = Column(Integer, primary_key=True) # Chave primária
    token = Column(String(100)) # Token
    id_usuario = Column(Integer, ForeignKey('Pessoas.id')) # Chave estrangeira
    data = Column(DateTime, default=datetime.datetime.utcnow()) # Data da geração do token

# Definindo as informações no nosso banco de dados
Base.metadata.create_all(engine) # Criando as tabelas no banco de dados



