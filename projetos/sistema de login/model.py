from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usando Banco de Dados Local com SQLite
CONN = "sqlite:///projetos/sistema de login/banco_sistema_login.db"
# Conexão com banco SQLite - ele criará o arquivo banco_sistema_login.db na pasta do script
engine = create_engine(CONN, echo=True)
# Sessão de base
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definindo a tabela
class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    senha = Column(String(100), nullable=False)

# Cria a tabela no banco de dados Pessoa
Base.metadata.create_all(engine)


