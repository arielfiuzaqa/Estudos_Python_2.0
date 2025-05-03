import pymysql
import pymysql.cursors

# Conexão com o banco de dados - Adicionar um gratuito depois e ir testando.
con = pymysql.connect(
    host='db4free.net',
    port=3306,
    user='afiuza1994',
    passwd='afiuza1994',
    database='banco_python',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def criar_tabela(nome_tabela): # Quando quiser criar a tabela já tenho aqui como fazer
# Vamos criar um cursor que vai ser isso que vai interagir com nosso banco e colocar nossos codigos em sql
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nome_tabela}(nome varchar(50))")
        print("Tabela criada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erros {e}")

def remove_tabela(nome_tabela): # Quando quiser remover a tabela já tenho aqui como fazer
# Vamos criar um cursor que vai ser isso que vai interagir com nosso banco e colocar nossos codigos em sql
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nome_tabela}")
        print("Tabela removida com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erros {e}")

def inserir_tabela(): # Quando quiser inserir alguma informação na tabela já tenho aqui como fazer
    nome_tabela = input('Digite a Tabela que quer inserir o nome: ')
    nome = input('Digite seu nome: ')
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO {nome_tabela} values('{nome}')")
        print("Valor inserido na tabela com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erros {e}")

def select_tabela(): # Quando quiser inserir alguma informação na tabela já tenho aqui como fazer
    nome_tabela = input('Digite a Tabela que quer selecionar o nome: ')
    try:
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {nome_tabela}")
        print("Valor inserido na tabela com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erros {e}")

def update_tabela(): # Quando quiser update alguma informação na tabela já tenho aqui como fazer
    nome_tabela = input('Digite a Tabela que quer update no nome: ')
    nome = input("Qual nome você quer dar update? ")
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE {nome_tabela} SET nome = '{nome}'")
        print("Atualização feita com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erros {e}")

def delete_tabela(): # Quando quiser update alguma informação na tabela já tenho aqui como fazer
    nome_tabela = input('Digite a Tabela que quer deletar: ')
    nome = input("Qual nome você quer dar deletar? ") # Melhor usar a chave primaria pelo id
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM {nome_tabela} WHERE nome = '{nome}'")
        print("Remoção feita com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erros {e}")






# Fechando a conexão com o banco após todos os comandos
con.close()

