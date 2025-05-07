from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
    # Usando Banco de Dados Local com SQLite
    CONN = "sqlite:///projetos/sistema de login/banco_sistema_login.db"
    # Conexão com banco SQLite - ele criará o arquivo banco_sistema_login.db na pasta do script
    engine = create_engine(CONN, echo=True)
    # Sessão de base
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class ControllerCadastro:
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        # Verifica se os dados estão vazios
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200 or len(email) < 10:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        sesseion = retorna_session()
        # Verifica se o email já existe
        usuario = sesseion.query(Pessoa).filter(Pessoa.email==email).all()

        if len(usuario) > 0:
            return 5
        
        dados_verificados = cls.verifica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados
        
        try:
            # Criptografa a senha - O .encode() converte a string em bytes e o .hexdigest() retorna a string hexadecimal
            senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
            # Cria o objeto Pessoa com os dados fornecidos
            pessoa = Pessoa(nome=nome, email=email, senha=senha_criptografada)
            # Adiciona o objeto à sessão do banco de dados
            sesseion.add(pessoa)
            # Salva as alterações no banco de dados
            sesseion.commit()
            return 1
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            return 6
        
class ControllerLogin:
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        # Criptografa a senha - O .encode() converte a string em bytes e o .hexdigest() retorna a string hexadecimal
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
        # Verifica se o email e a senha estão corretos
        logado = session.query(Pessoa).filter(Pessoa.email==email, Pessoa.senha==senha_criptografada).all()
        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False
        

#print(ControllerCadastro.cadastrar('Lucas', 'govaident@gmal.com', '123654789'))
print(ControllerLogin.login('govaident@gmal.com', '123654789'))
