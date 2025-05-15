from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Base declarada primeiro
Base = declarative_base()

# Caminho do banco de dados
CONN = "sqlite:///C:/Users/t_ariel.fiuza/Downloads/python triton/projetos/fastapitest/banco_api.db"
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(128))  # compatível com hash de senha
    data_cadastro = Column(DateTime, default=datetime.datetime.utcnow)

class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    token = Column(String(100))
    id_usuario = Column(Integer, ForeignKey('pessoas.id'))
    data = Column(DateTime, default=datetime.datetime.utcnow)

# Criar tabelas
Base.metadata.create_all(engine)
