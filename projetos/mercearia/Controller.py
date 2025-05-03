from DAO import *
from Models import *
from datetime import datetime

class ControllerCategoria:
    def cadastrar_categoria(self, nova_categoria):
        existe = False
        x = DaoCategoria.ler()

        for i in x:
            if i.categoria == nova_categoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print(f"Categoria {nova_categoria} cadastrada com sucesso!")
        else:
            print(f"Categoria {nova_categoria} já existe!")

    def remover_categoria(self, remover_categoria):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == remover_categoria, x))

        if len(cat) <= 0:
            print(f"Categoria {remover_categoria} que deseja remover não existe!")

        else:
            for i in range(len(x)):
                if x[i].categoria == remover_categoria:
                    del x[i]
                    break
                print(f"Categoria {remover_categoria} removida com sucesso!")

                #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open(r'projetos\mercearia\arquivos txt\categoria.txt', 'w') as file:
                for i in x:
                    file.writelines(f"{i.categoria}\n")
                    break
        
        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem Categoria"), x.quantidade)
                           if (x.produto.categoria == remover_categoria)
                           else (x), estoque))

        with open(r"projetos\mercearia\arquivos txt\estoque.txt", 'w') as file:
            for i in estoque:
                file.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}\n")
        
    def alterar_categoria(self, categoria_antiga, categoria_nova):
        x = DaoCategoria.ler() # Lê as categorias do arquivo
        # Verifica se a categoria antiga existe ou não existe
        cat = list(filter(lambda x: x.categoria == categoria_antiga, x))
        # Se a categoria antiga existe, verifica se a nova categoria já existe
        if len(cat) > 0:
            # Se a nova categoria não existe, altera a categoria antiga para a nova
            cat1 = list(filter(lambda x: x.categoria == categoria_nova, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoria_nova) if(x.categoria == categoria_antiga) else(x), x))
                print("Alteração feita com sucesso!!")

                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoria_antiga), x.quantidade)
                           if (x.produto.categoria == categoria_nova)
                           else (x), estoque))

                with open(r"projetos\mercearia\arquivos txt\estoque.txt", 'w') as file:
                    for i in estoque:
                        file.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}\n")

            else:
                print(f"Categoria {categoria_nova} já existe!")
                return
        
        else:
            print(f"Categoria {categoria_antiga} não existe!")
            
        # Se a categoria antiga existe e a nova não existe, salva as alterações no arquivo
        with open(r'projetos\mercearia\arquivos txt\categoria.txt', 'w') as file:
            for i in x:
                file.writelines(f"{i.categoria}\n")
            print(f"Categoria {categoria_antiga} alterada para {categoria_nova} com sucesso!")

    def mostrar_categoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print("Não existem categorias cadastradas!")
        else:
            print("Categorias cadastradas são: ")
            for i in categorias:
                print(f"Categoria {i.categoria}")

class ControllerEstoque:
    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y)) # Verifica se a categoria existe ou não
        est = list(filter(lambda x: x.produto.nome == nome, x)) # Verifica se o produto já existe ou não com aquele nome que passei

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f"Produto {nome} cadastrado com sucesso!")
            else:
                print(f"Produto {nome} já existe no Estoque!")
        else:
            print(f"Categoria {categoria} não existe!")

    def remover_produto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)): # Percorre a lista de produtos do estoque
                # Verifica se o nome do produto é igual ao nome que passei
                if x[i].produto.nome == nome:
                    del x[i] # Apaga da memoria um valor da lista, no caso x
                    break
            print(f"Produto {nome} removido com sucesso!")
        else:
            print(f"Produto {nome} não existe no Estoque!")
        
        with open(r'projetos\mercearia\arquivos txt\estoque.txt', 'w') as file:
            for i in x:
                file.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")

    def alterar_produto(self, nome_antigo, nome_novo, preco_novo, categoria_nova, quantidade_nova):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria_nova, y))
        if len(h) > 0:
            # Verifica se o produto existe ou não
            est = list(filter(lambda x: x.produto.nome == nome_antigo, x))
            if len(est) > 0:
                # Verifica se o produto já existe ou não com aquele nome que passei
                est = list(filter(lambda x: x.produto.nome == nome_novo, x))
                if len(est) == 0:
                    # Altera o produto
                    x = list(map(lambda x: Estoque(Produtos(nome_novo, preco_novo, categoria_nova), quantidade_nova) if(x.produto.nome == nome_antigo) else(x), x))
                    print(f"Produto {nome_antigo} alterado para {nome_novo} com sucesso!")
                else:
                    print(f"Produto {nome_novo} já cadastrado!")
            else:
                print(f"Produto {nome_antigo} não existe!")
                # Salva as alterações no arquivo
                with open(r'projetos\mercearia\arquivos txt\estoque.txt', 'w') as file:
                    for i in x:
                        file.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")
        else:
            print("Produto não existe!")

    def mostrar_estoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("Não existem produtos cadastrados no estoque!")
        else:
            print("produtos cadastrados no estoque são: ")
            print(f"========== ESTOQUE ==========\n")
            for i in estoque:
                print(f"\nProduto {i.produto.nome} | Preço: {i.produto.preco} | Categoria: {i.produto.categoria} | Quantidade: {i.quantidade}")
                print("--------------------------------------------------------------------------------")

class ControllerVenda:
    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidade_vendida):
        x = DaoEstoque.ler()  # lê o estoque atual
        temp = []
        existe = False
        quantidade_suficiente = False
        valor_compra = None

        for i in x:
            if i.produto.nome == nome_produto:
                existe = True
                if i.quantidade >= quantidade_vendida:
                    quantidade_suficiente = True
                    i.quantidade -= quantidade_vendida  # atualiza quantidade no estoque

                    vendido = Venda(
                        Produtos(i.produto.nome, i.produto.preco, i.produto.categoria),
                        vendedor,
                        comprador,
                        quantidade_vendida
                    )

                    valor_compra = quantidade_vendida * i.produto.preco
                    DaoVendas.salvar(vendido)
                break  # produto encontrado, pode sair do loop

        if not existe:
            print(f"Produto {nome_produto} não existe!")
            return None

        if not quantidade_suficiente:
            print(f"Quantidade {quantidade_vendida} maior que a quantidade em estoque ou não possui estoque!")
            return None

        # Atualiza o estoque no arquivo com as quantidades corrigidas
        with open(r'projetos\mercearia\arquivos txt\estoque.txt', 'w') as file:
            for i in x:
                file.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")

        print(f"Venda realizada com sucesso!")
        return valor_compra            

    def report_produtos_vendidos(self):
        vendas = DaoVendas.ler()
        produtos = []

        for venda in vendas:
            nome = venda.itensVendido.nome
            quantidade = venda.quantidade_vendida

            # Verifica se o produto já está na lista
            encontrado = False
            for p in produtos:
                if p['produto'] == nome:
                    p['quantidade'] += quantidade
                    encontrado = True
                    break

            # Se não encontrou, adiciona novo produto
            if not encontrado:
                produtos.append({'produto': nome, 'quantidade': quantidade})

        # Ordena os produtos pela quantidade vendida (decrescente)
        ordenar = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print(f"Produtos vendidos: ")

        # Imprime o relatório numerado corretamente
        for idx, item in enumerate(ordenar, start=1):
            print(f"=================== Produto {idx} =====================")
            print(f"Produto: {item['produto']}\nQuantidade vendida: {item['quantidade']}")
        print(f"===================================================")

    def mostrar_vendas(self, data_inicio, data_termino):
        vendas = DaoVendas.ler()  # ✅ Agora sabemos que isso retorna uma lista de objetos Venda
        # Data inicial e final no formato dd/mm/aaaa
        data_inicio_1 = datetime.strptime(data_inicio, '%d/%m/%Y')
        data_termino_1 = datetime.strptime(data_termino, '%d/%m/%Y')
        # Filtrar entre as datas selecionadas
        vendas_selecionadas = list(filter(
            lambda x: data_inicio_1 <= datetime.strptime(x.data.strftime('%d/%m/%Y'), '%d/%m/%Y') <= data_termino_1,
            vendas
        ))

        total = 0
        for idx, venda in enumerate(vendas_selecionadas, start=1):
            print(f"================ Vendas [{idx}] ==================")
            print(f"Nome: {venda.itensVendido.nome}")
            print(f"Categoria: {venda.itensVendido.categoria}")
            print(f"Data: {venda.data.strftime('%d/%m/%Y')}")
            print(f"Quantidade: {venda.quantidade_vendida}")
            print(f"Cliente: {venda.comprador}")
            print(f"Vendedor: {venda.vendedor}")
            print("")

            total += venda.itensVendido.preco * venda.quantidade_vendida

        print(f"Total vendido: R$ {total:.2f}")

class ControllerFornecedor:
    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        # Filtra pelo cnpj e telefone
        list_cnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        list_telefone = list(filter(lambda x: x.telefone == telefone, x))
        # Se existir ou não
        if len(list_cnpj) > 0:
            print(f"O CNPJ {list_cnpj} já existe!")
        elif len(list_telefone) > 0:
            print(f"O Telefone {list_telefone} já existe!!")
        else:
            if len(cnpj) == 14 and len(telefone) == 11:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))  
            else:
                print("Digite um CNPJ ou Telefone válido!!")

    def alterar_fornecedor(self, nome_alterar, novo_nome, novo_cnpj, novo_telefone, nova_categoria):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome_alterar, x))

        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novo_cnpj, x))
            if len(est) == 0:
                x = list(map(Fornecedor(novo_nome, novo_cnpj, novo_telefone, nova_categoria) if(x.nome == nome_alterar) else(x), x))
            else:
                print(f"Esse CNPJ {est} já existe!")
        else:
            print(f"O fornecedor que deseja alterar não existe!")
        
        with open(r"projetos\mercearia\arquivos txt\fornecedor.txt", "w") as file:
            for i in x:
                file.writelines(f"{i.nome}|{i.cnpj}|{i.telefone}|{i.email}|{i.categoria}\n")
            print(f"Fornecedor {i} alterado com sucesso!!")

    def remover_fornecedor(self, nome):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print(f"O Fornecedor {est} que deseja remover NÃO existe.")

        with open(r"projetos\mercearia\arquivos txt\fornecedor.txt", "w") as file:
            for i in x:
                file.writelines(f"{i.nome}|{i.cnpj}|{i.telefone}|{i.categoria}\n")
            print(f"Fornecedor {i} removido com sucesso!")
        
    def mostrar_fornecedores(self):
        fornecedores = DaoFornecedor.ler()

        if len(fornecedores) == 0:
            print("Lista de fornecedores vazia.")
        for i in fornecedores:
            print(f"========== FORNECEDOR {i} ==========")
            print(f"Categoria Fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"CNPJ: {i.cnpj}\n"
                  f"Telefone: {i.telefone}\n")

class ControllerCliente:

    def cadastrar_cliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        lista_cliente = list(filter(lambda x: x.cpf == cpf, x))
        if len(lista_cliente) > 0:
            print(f"O Cliente {lista_cliente} já existe!!")
        else:
            if len(cpf) == 11 and len(telefone) == 11:
                DaoPessoa.salvar(Pessoa(nome, cpf, telefone, email, endereco))
                print(f"Cliente com CPF: {cpf} e Telefone: {telefone} cadastrado com sucesso!")
            else:
                print(f"Esses numeros de CPF: {cpf} e Telefone: {telefone}, não são válidos")
    
    def alterar_cliente(self, nome_alterar, nome_novo, novo_telefone, novo_cpf, novo_email, novo_endereco):
        x = DaoPessoa.ler()
        # Filtrando para achar o nome antigo para retornar
        est = list(filter(lambda x: x.nome == nome_alterar, x))
        
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(nome_novo, novo_cpf, novo_telefone, novo_email, novo_endereco) if (
                x.nome == nome_alterar) else(x), x))
        else:
            print(f"Cliente {nome_alterar} NÃO existe no sistema.")

        with open(r"projetos\mercearia\arquivos txt\clientes.txt", "w") as file:
            for i in x:
                file.writelines(f"{i.nome}|{i.cpf}|{i.telefone}|{i.email}|{i.endereco}\n")
            print("Cliente alterado com sucesso.")

    def remover_cliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print(f"Cliente {i} que deseja remover NÃO existe!")
            return None
        
        with open(r"projetos\mercearia\arquivos txt\clientes.txt", "w") as file:
            for i in x:
                file.writelines(f"{i.nome}|{i.cpf}|{i.telefone}|{i.email}|{i.endereco}\n")
            print("Cliente removido com sucesso!")

    def mostrar_cliente(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print("Lista de clientes vazia.")
        
        for i in clientes:
            print(f"=============== Cliente {i} ===============")
            print(f"Nome: {i.nome}\n"
                  f"CPF: {i.cpf}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}")

class ControllerFuncionario:
    def cadastrar_funcionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        list_cpf = list(filter(lambda x: x.cpf == cpf, x))
        list_clt = list(filter(lambda x: x.clt == clt, x))

        if len(list_cpf) > 0:
            print(f"Funcionario {list_cpf} já existente.")
        elif len(list_clt) > 0:
            print(f"Já existe um funcionario com essa CLT: {list_clt}.")
        else:
            if len(list_cpf == 11) and len(list_clt) == 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print(f"Funcionario {nome} cadastrado!!")
            else:
                print("Digite um CPF ou Telefone válidos.")   

    def alterar_funcionario(self, nome_alterar, novo_clt, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome_alterar, x))

        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novo_clt, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco)
                         if(x.nome == nome_alterar) else(x), x))
        else:
            print(f"Funcionario {nome_alterar} não existe!!")

        with open(r"projetos\mercearia\arquivos txt\funcionarios.txt", "w") as file:
            for i in x:
                file.writelines(f"{i.clt}|{i.nome}|{i.telefone}|{i.cpf}|{i.email}|{i.endereco}\n")
            print(f"Funcionario {nome_alterar} alterado para {novo_nome} com sucesso!")

    def remover_funcionario(self, nome):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("Funcionario que deseja remover NÃO existe!!")
        
        with open(r"projetos\mercearia\arquivos txt\funcionarios.txt", "w") as file:
            for i in x:
                file.writelines(f"{i.clt}|{i.nome}|{i.telefone}|{i.cpf}|{i.email}|{i.endereco}\n")
            print(f"Funcionario removido com sucesso!!")
        
    def mostrar_funcionario(self):
        func = DaoFuncionario.ler()

        if len(func) == 0:
            print("Funcionario NÃO existe no sistema.")
        
        for idx, i in func:
            print(f"=============== Funcionario {idx} ===============")
            print(f"Nome: {i.nome}\n"
                  f"CLT: {i.clt}\n"
                  f"Telefone: {i.telefone}\n"
                  f"CPF: {i.cpf}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}")
