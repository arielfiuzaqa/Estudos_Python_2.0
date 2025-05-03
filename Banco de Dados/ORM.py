from sqlalchemy import create_engine,
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Se estiver conectado ao banco de dados externo ou local.
'''USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "Banco_de_Dados_01"
PORTA = 3306

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
'''
# Usando Banco de Dados Local com SQLite
# Conexão com banco SQLite - ele criará o arquivo banco.db na pasta do script
engine = create_engine("sqlite:///Banco de Dados/Dados/banco.db", echo=True)

# Sessão e base
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definindo a tabela Pessoa
class Pessoas(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    usuario = Column(String(20), nullable=False)
    senha = Column(String(10), nullable=False)

# Aqui poderia criar várias tabelas, mas como o foco é só um exemplo, vamos deixar assim mesmo.

# Cria a tabela no banco (caso não exista)
Base.metadata.create_all(engine)