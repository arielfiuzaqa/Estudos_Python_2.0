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
x1 = session.query(Pessoas).all() # Retorna todos os objetos da tabela Pessoas
x2 = session.query(Pessoas).filter(Pessoas.nome=='Lucas') # Retorna o primeiro objeto que atende ao filtro
#print(x1[0].id) # Imprime o id do primeiro objeto da lista x1
x3 = session.query(Pessoas).filter_by(nome='Fabio', usuario='Cofabi123')

for i in x3:
    print(i.id) # Imprime o nome de cada objeto da lista x1

'''
x = Pessoas(nome='Lucas', 
            usuario='Lukinha69', 
            senha=171869)
y = Pessoas(nome='Fabio', 
            usuario='Cofabi123', 
            senha=181899)'''

#session.add(x) # Adiciona o objeto à sessão
#session.add_all([x, y]) # Adiciona todos os objetos à sessão
#session.rollback() # Desfaz as alterações na sessão
#session.commit() # Salva as alterações no banco de dados

