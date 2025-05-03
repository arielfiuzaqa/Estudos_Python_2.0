# Acesso ao banco de dados ou armazenamento de dados - Armazenando os dados de forma persistente da class Pessoa
from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as file:
            file.write(f"{pessoa.nome}, {pessoa.idade}, {pessoa.cpf}\n")
    
    def ler(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'r') as file:
            file.read({pessoa.nome}, {pessoa.idade}, {pessoa.cpf})
            return file.readlines()