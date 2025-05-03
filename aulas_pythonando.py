# Estudos das aulas
"""
nomes = ['Matheus', 'Caio', 'Ariel', 'Fiuza', 'Brown', 'Jojo', 'Monkey-D', 'Naruto']
# Add Krisna com append e com insert insere o nome "Yuri" na posição de index 0 que é a primeria
nomes.append('Krisna')
nomes.insert(0, 'Yuri')
print(nomes)
# Remove o último nome pop e remove o nome "Caio" da lista ou indix com o remove
nomes.pop()
nomes.remove('Caio')
print(nomes)
# Ordena os nomes em ordem alfanumerica
nomes.sort()
print(nomes)
# Ordena os nomes em ordem alfanumerica reversa
nomes.sort(reverse=nomes)
print(nomes)

# Criando uma lista através de um range
x = list(range(0, 21+1))
print(x)

# Contando o numero de index e dizendo a posição de cada valor no indice apontado
idades = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
idades.sort(reverse=True)

for i in range(0, len(idades)):
    print(idades[i], i)

# Enumerando uma lista de outra forma com enumerate()
for i, j in enumerate(idades, 0):
    print(f"idade: {j}, Posição: {i}")

# Acessando elemento da lista através de calculo de matriz
m = [
    # Colunas de 0 a 3
    [1, 2, 3, 4], # Linha 0
    [5, 6, 7, 8], # Linha 1
    [9, 10, [0.1, 0.2, 0.3, 0.4], 12] # Linha 2
]

print(m[1]) # Lista da linha 1
print(m[1][2]) # Elemento 7 
print(m[2][2]) # Posição de um elemento especifico na matriz
print(m[2][2][3]) # Posição de um elemento especifico na matriz da lista elemento 0.4

# Um outro método para mostrar todos os itens da lista e suas posições
for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        print(m[i][j])

# Criando uma soma continua do numeros
x = [ 10 for i in range(0, 10)]
print(x)

# 21/03/2025
# Dicionário x = dict() ou x = {'nome': 'valor atribuido a esse nome', próximo...} abre as chaves
x = {'nome': 'Ariel Fiuza', 'idade': 21, 'CEP': '60180-420'}
print(x['idade'])

# Ou ainda para fazer atribuição a uma pessoa x
pessoa = x['nome']
print(pessoa)

# Agora vamos misturar dicionarios com listas, isso me parece bom
y = {'nomes': [], 'idades': 21, 'CEPs': [ '60180-420', '60555-444' ]}

y['nomes'].append('Ariel Fiuza')
y['nomes'].append('Yuri Fiuza')
y['nomes'].append('Jorge Fiuza')

print(y) # Todos os itens contidos dentro dos dicionários
print(y['nomes']) # itens do nome dentro do dicionário
print(y['nomes'][0]) # único item dentro da lista de um pedaço do dicionário

# Podemos fazer também o contrário, tornando cada pessoa em um dicionário - lista de dicionários
pessoas = [
    {"nome": "Alice", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"}
]
# Tenho uma lista agora de dicionários saíndo
for pessoa in pessoas:
    print(pessoa)
    print(pessoa['nome'])
# Faça um programa que precise de cadastro e senha e que possa inserir dados de n clientes básicos
# Deve poder adicionar nome, idade e altura
pessoas = []
while True:
    decisao = int(input('Digite 1 para cadastra uma pessoa e 2 para sair: '))
    if decisao == 2:
        break

    pessoa = {'nome': input('Digite seu nome: '), 'idade': input('Digite a idade: '), 'altura': input('Digite a altura: ')}
    pessoas.append(pessoa)

print(pessoas)
# Criando um update dentro do Dicionário
pessoas = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
# pessoas['CEP'] = '60888-777' # Adicionando uma nova chave no dicionário
pessoas.update({'CEP': '60777-888'}) # Para atualizar o dicionário
print(pessoas)
"""
"""# ==== Mais uma aula sobre =====
pessoas = {"nome": "Alice", "idade": 25, "altura": 175}
print(pessoas.values()) # Trás os valores dentro do dicionário - trás os valores das chaves
print(pessoas.keys()) # Trás os valores dentro do dicionário - trás as chaves
for i in pessoas.items(): # Trás os itens em tuplas
    print(i)
for i, j in pessoas.items(): # Trás os itens em tuplas separando os valores
    print(f'i = {i}, j = {j}')
"""
# key_api_google_ai = 'AIzaSyCa3QDpeW_EXGaS5tYtM_JT0tFN5kIBPss'

# Aula 51, 52 e 53 - Funções, Parâmetros, args e kwargs, retornando valores
"""def minha_funcao():
    funcao = print('Esta funcionando!!')
    tudo_bem = print('Esta tudo bem?')

minha_funcao()

def soma_valores(a, b):
    soma = a + b
    return soma, 1, 2

x = soma_valores(10, 20)
print(x)"""


# Modularização - Dividir sua aplicação em diversas partes e arquivos para facilitar a manutenção e o entendimento do código.
'''y = 20
z = 30

def soma_numeros(n1, n2, n3):
    return (n1 + n2) / n3
'''
# 55 - Tratamento de exceções 1 e 2

'''while True:
    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1 / n2)
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except TypeError:
        print('Não é possível dividir string por inteiro')
    except ValueError:
        print('Valor inválido, digite apenas números inteiros')
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        print('Finalizando...')'''
# Cada tipo de excessão pode ter um tratamento diferente, isso ajuda a quem não entende de codigo para poder entender o que está acontecendo

# 58 - Raise e assert
# Raise força o erro e assert verifica se o erro é verdadeiro ou falso, se for falso ele gera um erro
# Assert é uma forma de verificar se o valor é verdadeiro ou falso, se for falso ele gera um erro

# 59 - Geradores
'''from pympler.asizeof import asizesof

print(asizesof([1, 2, 3, 4, 5])) # Tamanho em bytes da lista

def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i * 2)
    return lista_dobro

x = dobro(range(0, 10))
y = asizesof(x)
print(x)
print(f'Tamanho da lista: {y} bytes')

# yeld - Gera um valor e para a execução da função, quando for chamado novamente ele continua de onde parou
def dobro_yield(lista):
    for i in lista:
        yield i*2 # Gera o valor e para a execução da função, quando for chamado novamente ele continua de onde parou

def dobro_normal(list):
    lista_dobro = []
    for i in list:
        lista_dobro.append(i)
        return lista_dobro

x = dobro_yield(range(0, 10000))
y = dobro_normal(range(0, 10000))

print(f"Função c/ Yield => {asizesof(x)}") # Tamanho em bytes da lista gerada pelo yeld
print(f"Função Normal {asizesof(y)}") # Tamanho em bytes da lista gerada pela função normal'''


# 60 - Lambda - programação funcional
'''x = lambda a, b: a + b # Função lambda que soma dois valores
y = lambda nome, idade: print(f'Nome: {nome}, Idade: {idade}') # Função lambda que imprime o nome e a idade
z = lambda *nomes: print(nomes) # Função lambda que imprime os nomes passados como parâmetro
print(x(10, 20)) # Chama a função lambda e passa os valores
y('Ariel', 21) # Chama a função lambda e passa os valores
z('Ariel', 'Yuri', 'Jorge', 'Henrique', 'Marcia') # Chama a função z lambda que trás vários valores *nomes
# Esses pontos é importante para entender que é possível fazer funções dentro de funções também usando o def + lambda'''

# 61 - Filter - programação funcional - filtrando valores - A maneira convencional é criar uma função mas vamos usar o filter
'''idades = [10, 12, 14, 13, 17, 16, 18, 19, 20, 25, 30, 33, 40, 50, 60, 70, 80, 90, 100]
idades_maiores = filter(lambda idade: idade > 18, idades) # Filtra as idades maiores que 18
idades_menores = filter(lambda idade: idade <= 18, idades) # Filtra as idades menores que 18
dicionario = [{'nome': 'Ariel', 'idade': 30, 'altura': 1.75}, {'nome': 'Tiago', 'idade': 17, 'altura': 1.85}] # Dicionário com os dados de uma pessoa
print(list(idades_maiores)) # Transforma o filtro em uma lista e imprime
print(list(idades_menores)) # Transforma o filtro em uma lista e imprime
print(list(filter(lambda dicionario: dicionario['idade'] < 18, dicionario))) # Filtra o dicionário e imprime os valores maiores que 18
print(list(filter(lambda dicionario: dicionario['nome'] == 'Ariel', dicionario))) # Filtra o dicionário e imprime os valores iguais a Ariel
'''

# 62 - MAP programação funcional
'''b = [i for i in range(12, 26)] # Lista de números de 12 a 25
print(b)
# O map aplica uma função a cada item de um iterável (como uma lista) e retorna um novo iterável com os resultados.
x = list(map(lambda b: 10 if b < 18 else b, b))
y = list(map(lambda b: 10 if b > 18 else b, b))
print(x, y) # Aplica a função lambda a cada item da lista b e imprime o resultado
a = [{'idade': 10}, {'idade': 20}, {'idade': 30}, {'idade': 40}]
n = list(map(lambda a: {'idades': a['idade'], 'maioridade': a['idade'] >= 18}, a)) # uma forma de se fazer
print(n)'''
# O filter filtra os itens de um iterável com base em uma condição e retorna um novo iterável com os itens que atendem a essa condição.
# O reduce reduz um iterável a um único valor aplicando uma função cumulativa a cada item.
# O zip combina dois ou mais iteráveis em um único iterável de tuplas.
# O all verifica se todos os itens de um iterável atendem a uma condição.
# O any verifica se pelo menos um item de um iterável atende a uma condição.
# O sorted ordena os itens de um iterável com base em uma função de chave.
# O reversed inverte a ordem dos itens de um iterável.
# O enumerate adiciona um índice a cada item de um iterável.
# O len retorna o comprimento de um iterável.
# O sum retorna a soma dos itens de um iterável.
# O max retorna o maior item de um iterável.
# O min retorna o menor item de um iterável.
# O list converte um iterável em uma lista.
# O tuple converte um iterável em uma tupla.
# O set converte um iterável em um conjunto.
# O dict converte um iterável de pares chave-valor em um dicionário.
# O str converte um objeto em uma string.
# O int converte um objeto em um inteiro.
# O float converte um objeto em um número de ponto flutuante.
# O bool converte um objeto em um valor booleano.
# O complex converte um objeto em um número complexo.
# O chr converte um inteiro em um caractere.
# O ord converte um caractere em um inteiro.


# 63, 64 e 65 - Arquivos 1, 2 e 3 - Criando arquivos, lendo arquivos e escrevendo arquivos
arquivo = open('pandas/docs/pessoas.txt', 'w') # Abre o arquivo pessoas.txt em modo escrita
arquivo.write('Ariel Fiuza\nYuri Fiuza\n\n') # Escreve no arquivo pessoas.txt

'''arquivo = open('pandas/docs/pessoas.txt', 'a') # Abre o arquivo pessoas.txt em modo append
i = 0
while True:
    if i >= 2:
        break
    nome = arquivo.write(input('Digite o nome: ') + ' ' + input('Digite sua idade: ') +'\n') # Escreve no arquivo pessoas.txt
    i += 1
    
arquivo.close() # Fecha o arquivo pessoas.txt'''

'''arquivo = open('pandas/docs/pessoas.txt', 'r') # Abre o arquivo pessoas.txt em modo leitura
resultados = arquivo.read() # Lê o arquivo pessoas.txt
print(resultados) # Lê o arquivo pessoas.txt e imprime

# Fechando o arquivo sem precisa colocar ao final que precisa fechar o arquivo
with open('pandas/docs/pessoas.txt', 'r') as arq: # abre o arquivo mas quando termina tudo ele fecha automaticamente o arquivo
    x = arq.readlines() # Lê o arquivo pessoas.txt e armazena em uma lista
    print(x)
'''

# Serialização de objetos - pickle
'''import pickle # Importa o módulo pickle para serialização de objetos, pegar algo em memoria e torna-lo um arquivo persistente
u = [1, 2, 3, 4, 5] # Cria uma lista com os números de 1 a 5
arq = open('pandas/docs/serializacao.pkl', 'wb') # Abre o arquivo serializacao.pickle em modo escrita binária
pickle.dump(u, arq) # Serializa a lista u e escreve no arquivo serializacao.pickle
arq = open('pandas/docs/serializacao.pkl', 'rb') # Abre o arquivo serializacao.pickle em modo leitura binária
retornou = pickle.load(arq) # Deserializa o arquivo serializacao.pickle e armazena em uma variável
print(retornou)
'''

# 66 - 1 - Introdução POO - Programação Orientada a Objetos
# Uma forma de se pensar e chegar a um resultado, uma forma de se pensar em objetos e classes
'''x = []
for i in range(0, 100):
    if i % 2 == 0:
        x.append(i)

print(x)

# Analogo mas com o pensamento diferente temos
y = [i for i in range(0, 100) if i % 2 == 0] # List Comprehension - Uma forma de se pensar diferente
print(y)
'''


# 67 - 2 - Modelagem 
# Uma forma de se pensar e chegar a um resultado, uma forma de se pensar em objetos e classes
'''class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
    
    def logar_sistema(self):
        print(f'{self.nome} esta logando no sistema...')

p1 = Pessoas('Ariel', 31, '123.456.789-00') # Cria um objeto da classe Pessoas
p2 = Pessoas('Yuri', 33, '123.456.789-00') # Cria um objeto da classe Pessoas
print(p1) # Acessa o atributo p1 __main__.Pessoas object at 0x0000019F47816FF0>
print(p1.nome) # Acessa o atributo nome do objeto p1
print(p1.idade) # Acessa o atributo idade do objeto p1
print(p2.nome) # Acessa o atributo nome do objeto p2
print(p2.idade) # Acessa o atributo idade do objeto p2
# Metodo é uma função dentro(pertencente) de uma classe! EXEMPLO - def logar_sistema(self):
p1.logar_sistema() # Chama o método logar_sistema da classe Pessoas
p2.logar_sistema() # Chama o método logar_sistema da classe Pessoas'''


# 68 - 3 - Método construtor - 
'''class MetodoConstrutor:
    def __init__(self, nome, idade, cpf): # Método construtor - sempre que criar um objeto da classe MetodoConstrutor ele vai chamar o método __init__
        print('Construtor chamado')
        print(f'{nome} | {idade} | {cpf}')

    def logar_sistema(self):
        print('\nLogando no sistema...')

# Chama o método construtor da classe MetodoConstrutor - Sempre vai ser chamado o metodo __init__
# p1.logar_sistema() # Chama o método logar_sistema da classe MetodoConstrutor
p1 = MetodoConstrutor('Ariel', 31, '123.456.789-00') # Chama o método construtor da classe MetodoConstrutor
p2 = MetodoConstrutor('Yuri', 31, '123.456.789-10') # Chama o método construtor da classe MetodoConstrutor
p1.logar_sistema() # Chama o método logar_sistema da classe MetodoConstrutor'''

# 69 - 4 - Atributos de instâncias
# Diferenças entre instâncias e atributos de instâncias e atributos de classe
'''class AtributosInstancias:
    def __init__(self, nome, idade, cpf):
        self.nome = nome # Atributo de instância - cada objeto tem seu próprio atributo
        self.idade = idade # Atributo de instância - cada objeto tem seu próprio atributo
        self.cpf = cpf # Atributo de instância - cada objeto tem seu próprio atributo

    def logar_sistema(self):
        print(f'{self.nome} esta logando no sistema...')'''

# 70 - 5 - Atributos de classe / Atributos de instancia
# Diferenças entre instâncias e atributos de instâncias e atributos de classe
'''class AtributosClasse:
    contador = 0 # Atributo de classe - todos os objetos compartilham o mesmo atributo
    def __init__(self, nome, idade, cpf):
        self.nome = nome # Atributo de instância - cada objeto tem seu próprio atributo
        self.idade = idade # Atributo de instância - cada objeto tem seu próprio atributo
        self.cpf = cpf # Atributo de instância - cada objeto tem seu próprio atributo
        AtributosClasse.contador += 1 # Incrementa o contador a cada vez que um objeto é criado

    def logar_sistema(self):
        print(f'{self.nome} esta logando no sistema...')'''

# 71 - 6 - Métodos de classe
# Métodos de classe são métodos que podem ser chamados sem precisar criar um objeto da classe
# Eles são definidos com o decorator @classmethod e recebem a classe como primeiro parâmetro
# Eles são usados para acessar ou modificar atributos de classe
# Eles são usados para criar métodos que não dependem de instâncias da classe
# Eles são usados para criar métodos que podem ser chamados diretamente na classe
# Eles são usados para criar métodos que podem ser chamados em subclasses
# Eles são usados para criar métodos que podem ser chamados em instâncias da classe
# Eles são usados para criar métodos que podem ser chamados em subclasses

'''class AtributosClasse:
    contador = 0 # Atributo de classe - todos os objetos compartilham o mesmo atributo
    def __init__(self, nome, idade, cpf):
        self.nome = nome # Atributo de instância - cada objeto tem seu próprio atributo
        self.idade = idade # Atributo de instância - cada objeto tem seu próprio atributo
        self.cpf = cpf # Atributo de instância - cada objeto tem seu próprio atributo
        AtributosClasse.contador += 1 # Incrementa o contador a cada vez que um objeto é criado

    @classmethod
    def logar_sistema(cls): # Método de classe - pode ser chamado sem precisar criar um objeto da classe
        print(f'{cls.contador} pessoas cadastradas no sistema...')

p1 = AtributosClasse('Ariel', 31, '123.456.789-00') # Chama o método construtor da classe AtributosClasse
p2 = AtributosClasse('Yuri', 31, '123.456.789-10') # Chama o método construtor da classe AtributosClasse
print(p1) # Acessa o atributo p1 __main__.AtributosClasse object at 0x0000019F47816FF0>
print(p2) # Acessa o atributo p2 __main__.AtributosClasse object at 0x0000019F47816FF0>
# Atributos de instância
print(p1.nome) # Acessa o atributo nome do objeto p1
print(p1.idade) # Acessa o atributo idade do objeto p1
print(p2.nome) # Acessa o atributo nome do objeto p2
print(p2.idade) # Acessa o atributo idade do objeto p2
print(AtributosClasse.contador) # Acessa o atributo contador da classe AtributosClasse

p1.logar_sistema() # Chama o método logar_sistema da classe AtributosClasse
AtributosClasse.logar_sistema() # Chama o método logar_sistema da classe AtributosClasse'''

# 72 - 7 - Entendendo o CLS
# O CLS é o primeiro parâmetro de um método de classe e representa a classe em si
# Ele é usado para acessar ou modificar atributos de classe
# Ele é usado para criar métodos que não dependem de instâncias da classe
'''class AtributosClasse:
    contador = 0  # Atributo de classe - todos os objetos compartilham o mesmo atributo

    def __init__(self, nome, idade, cpf):
        self.nome = nome  # Atributo de instância - cada objeto tem seu próprio atributo
        self.idade = idade  # Atributo de instância - cada objeto tem seu próprio atributo
        self.cpf = cpf  # Atributo de instância - cada objeto tem seu próprio atributo
        AtributosClasse.contador += 1  # Incrementa o contador a cada vez que um objeto é criado

    @classmethod
    def criar_com_idade_padrao(cls, nome, cpf):
        idade_padrao = 18
        return cls(nome, idade_padrao, cpf)

    @classmethod
    def logar_sistema(cls):  # Método de classe - pode ser chamado sem precisar criar um objeto da classe
        print(f'{cls.contador} pessoas cadastradas no sistema...')

# Criando objetos usando o método de classe
p1 = AtributosClasse.criar_com_idade_padrao('Ariel', '123.456.789-00')
p2 = AtributosClasse.criar_com_idade_padrao('Yuri', '123.456.789-10')

# Atributos de instância
print(p1.nome, p1.idade, p1.cpf)
print(p2.nome, p2.idade, p2.cpf)

# Atributos de classe
AtributosClasse.logar_sistema()'''

# 73 - 8 - Métodos estáticos
# Métodos estáticos são métodos que podem ser chamados sem precisar criar um objeto da classe
# Eles são definidos com o decorator @staticmethod e não recebem a classe como primeiro parâmetro
# Eles são usados para criar métodos que não dependem de instâncias da classe
# Eles são usados para criar métodos que não dependem de atributos de classe
# Eles são usados para criar métodos que não dependem de atributos de instância
# Eles são usados para criar métodos que podem ser chamados diretamente na classe
'''class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

# Chamando métodos estáticos diretamente na classe
resultado_soma = Calculadora.somar(10, 5)
resultado_subtracao = Calculadora.subtrair(10, 5)

print(f"Soma: {resultado_soma}")
print(f"Subtração: {resultado_subtracao}")
'''

# 74 - 9 - Herança #1
# Herança é um mecanismo que permite criar uma nova classe a partir de uma classe existente
# A nova classe herda os atributos e métodos da classe existente
# A nova classe pode ter seus próprios atributos e métodos
# A nova classe pode sobrescrever os métodos da classe existente
# A nova classe pode chamar os métodos da classe existente

'''class Vendedor():

    def falar(self):
        print('Vendedor falando...')
    
    def andar(self):
        print('Vendedor andando...')
    
    def vender(self):
        print('Vendedor vendendo...')
    
class Cliente():

    def falar(self):
        print('Cliente falando...')

    def andar(self):
        print('Cliente andando...')

    def comprar(self):
        print('Cliente comprando...')

class Pessoa(Vendedor, Cliente): # Herança múltipla - A classe Pessoa herda os atributos e métodos da classe Vendedor e Cliente
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Pessoa falando...')
    
    def andar(self):
        print('Pessoa andando...')

c1 = Cliente()
c2 = Vendedor()
c1.falar()
c1.andar()
c1.comprar()
c2.falar()
c2.andar()
c2.vender()
c3 = Pessoa('Ariel', 31)'''

# 75 - 10 - Sobreposição de métodos
'''class Sobreposicao:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} falando...')
    
    def andar(self):
        print(f'{self.nome} andando...')

class Vendedor(Sobreposicao):

    def comprar(self):
        print(f'{self.nome} comprando...')

    def falar(self):
        super().falar() # Chama o método falar da classe pai
        print(f'{self.nome} Gritando...') # Depois segue mostrando esse metodo falar da classe Vendedor

v1 = Vendedor('Ariel', 31)
v1.falar()
'''

# 76 - 11 - Herança múltipla
# Herança múltipla é quando uma classe herda de mais de uma classe
# Isso pode causar problemas de ambiguidade se as classes pai tiverem métodos com o mesmo nome
# O Python resolve isso usando a ordem de resolução de métodos (MRO - Method Resolution Order)
# O MRO é a ordem em que o Python procura os métodos e atributos nas classes pai
'''class Animal():

    def andar(self):
        print('Animal andando...')
    
    def andar(self):
        print('Animal andando...')
    
    def pular(self):
        print('Animal pulando...')

class Felino(Animal): # Herda de Animal

    def felino(self):
        print('Eu sou um felino..')

class Gato(Felino): # Herda de Felino que herda de Animal

    def miar(self):
        print('Gato miando...')
        
class Cachorro(Animal): # Herda de Animal

    def latir(self):
        print('Cachorro latindo...')

x = Cachorro()
x.latir()
x.andar()
x.pular()

y = Gato()
y.miar()
y.andar()'''


# 77 - 1 - MVC Introdução
# MVC é um padrão de arquitetura de software que separa a aplicação em três partes: Modelo, Visão e Controlador
# O Modelo é responsável por gerenciar os dados da aplicação e a lógica de negócios
# A Visão é responsável por apresentar os dados ao usuário e receber as entradas do usuário
# O Controlador é responsável por intermediar a comunicação entre o Modelo e a Visão
# O MVC ajuda a separar as responsabilidades da aplicação e facilita a manutenção e o desenvolvimento
# O MVC é amplamente utilizado em aplicações web e desktop

# 78 - 2 - Model e Dal
# O Model é a parte da aplicação que representa os dados e a lógica de negócios
# O Model é responsável por gerenciar os dados da aplicação e a lógica de negócios
# O Model é responsável por validar os dados e garantir a integridade dos dados
# O Model é responsável por persistir os dados em um banco de dados ou arquivo
# O Model é responsável por fornecer os dados para a Visão
# Pasta MVC - Fazendo a estrutura de pastas para o projeto



# Ate aula 100
