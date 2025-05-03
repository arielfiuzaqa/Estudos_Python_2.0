from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open(r'projetos\mercearia\arquivos txt\categoria.txt', 'a') as file:
            file.writelines(f"{categoria}\n")

    @classmethod
    def ler(cls):
        with open(r'projetos\mercearia\arquivos txt\categoria.txt', 'r') as file:
            cls.categoria = file.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        print(cls.categoria)

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
            #print(cat)
        return cat
    # Teste de Add categorias

class DaoVendas:
    @classmethod
    def salvar(cls, venda: Venda):
        with open(r'projetos\mercearia\arquivos txt\venda.txt', 'a') as file:
            file.writelines(
                f"{venda.itensVendido.nome}|{venda.itensVendido.preco}|{venda.itensVendido.categoria}|"
                f"{venda.vendedor}|{venda.comprador}|{venda.quantidade_vendida}|{venda.data.strftime('%d/%m/%Y')}\n"
            )   

    @classmethod
    def ler(cls):
        with open(r'projetos\mercearia\arquivos txt\venda.txt', 'r') as file:
            cls.venda = file.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        print(cls.venda)

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], float(i[1]), i[2]), i[3], i[4], int(i[5]), datetime.strptime(i[6], '%d/%m/%Y')))
            print(vend)
        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open(r'projetos\mercearia\arquivos txt\estoque.txt', 'a') as file:
            file.writelines(f"{produto.nome}|{produto.preco}|{produto.categoria}|{quantidade}\n")

    @classmethod
    def ler(cls):
        try:
            with open(r'projetos\mercearia\arquivos txt\estoque.txt', 'r') as file:
                linhas = file.readlines()
        except FileNotFoundError:
            # Arquivo não existe ainda, retorna lista vazia
            return []

        # Remove quebras de linha e divide os campos
        linhas = [linha.strip().split('|') for linha in linhas if linha.strip()]

        # Cria objetos Estoque a partir das linhas lidas
        est = []
        for i in linhas:
            produto = Produtos(i[0], float(i[1]), i[2])
            estoque_item = Estoque(produto, int(i[3]))
            est.append(estoque_item)
        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open(r'projetos\mercearia\arquivos txt\fornecedor.txt', 'a') as file:
            file.writelines(f"{fornecedor}\n")

    @classmethod
    def ler(cls):
        with open(r'projetos\mercearia\arquivos txt\fornecedor.txt', 'r') as file:
            cls.fornecedor = file.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        print(cls.fornecedor)

        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3], i[4]))
            print(forn)
        return forn
    
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open(r'projetos\mercearia\arquivos txt\pessoa.txt', 'a') as file:
            file.writelines(f"{pessoa}\n")

    @classmethod
    def ler(cls):
        with open(r'projetos\mercearia\arquivos txt\pessoa.txt', 'r') as file:
            cls.pessoa = file.readlines()
        
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        print(cls.pessoa)

        pes = []
        for i in cls.pessoa:
            pes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
            print(pes)
        return pes

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open(r'projetos\mercearia\arquivos txt\funcionario.txt', 'a') as file:
            file.writelines(f"{funcionario}\n")

    @classmethod
    def ler(cls):
        with open(r'projetos\mercearia\arquivos txt\funcionario.txt', 'r') as file:
            cls.funcionario = file.readlines()
        
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        print(cls.funcionario)

        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4]))
            print(func)
        return func
    
