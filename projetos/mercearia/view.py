import Controller
import os.path

def criar_arquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, "w") as file:
                file.write("")

criar_arquivos(r"projetos\mercearia\arquivos txt\categoria.txt", r"projetos\mercearia\arquivos txt\estoque.txt", 
               r"projetos\mercearia\arquivos txt\clientes.txt", r"projetos\mercearia\arquivos txt\fornecedores.txt", 
               r"projetos\mercearia\arquivos txt\funcionarios.txt", r"projetos\mercearia\arquivos txt\venda.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categoria)\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Funcionario )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os Produtos Mais Vendidos\n"
                          "Digite 8 para Sair\n"))
        
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para Cadastrar Categoria\n"
                                    "Digite 2 para Remover Categoria\n"
                                    "Digite 3 para Alterar Categoria\n"
                                    "Digite 4 para Mostrar Categoria\n"
                                    "Digite 5 para Sair\n"))
                
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar.\n")
                    cat.cadastrar_categoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover.\n")
                    cat.remover_categoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a Categoria Atual que deseja alterar.\n")
                    categoria_nova = input("Digite a Nova Categoria.\n")
                    cat.alterar_categoria(categoria, categoria_nova)
                elif decidir == 4:
                    cat.mostrar_categoria()
                else:
                    break

        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para Cadastrar Produto\n"
                                    "Digite 2 para Remover Produto\n"
                                    "Digite 3 para Alterar Produto\n"
                                    "Digite 4 para Mostrar Estoque\n"
                                    "Digite 5 para Sair\n"))
                if decidir == 1:
                    nome = input("Digite o Nome do Produto que deseja Cadastrar.\n")
                    preco = input("Digite o Preço do seu Produto.\n")
                    categoria = input("Digite a Categoria do seu Produto.\n")
                    quantidade = input("Digite a Quantidade que deseja colocar no Estoque.\n")
                    cat.cadastrar_produto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    nome = input("Digite o Nome do Produto que deseja Remover.\n")
                    cat.remover_produto(nome)
                elif decidir == 3:
                    nome_antigo = input("Digite o nome do produto antigo que deseja alterar.\n")
                    nome_novo = input("Digite o nome do produto novo que deseja alterar.\n")
                    preco_novo = input("Digite o preço do produto novo.\n")
                    categoria_nova = input("Digite a categoria nova.\n")
                    quantidade_nova = input("Digite a quantidade.\n")
                    cat.alterar_produto(nome_antigo, nome_novo, preco_novo, categoria_nova, quantidade_nova)
                elif decidir == 4:
                    cat.mostrar_estoque()
                else:
                    break
        
        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para Cadastrar Fornecedor\n"
                                        "Digite 2 para Remover Fornecedor\n"
                                        "Digite 3 para Alterar Fornecedor\n"
                                        "Digite 4 para Mostrar Fornecedor\n"
                                        "Digite 5 para Sair\n"))
                if decidir == 1:
                    nome = input("Digite o nome do Fornecedor.\n")
                    cnpj = input("Digite o CNPJ do Fornecedor.\n")
                    telefone = input("Digite o Telefone do Fornecedor.\n")
                    categoria = input("Digite a Categoria do Fornecedor.\n")
                    cat.cadastrar_fornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome_para_remover = input("Digite o nome do Fornecedor que deseja remover.\n")
                    cat.remover_fornecedor(nome_para_remover)
                elif decidir == 3:
                    nome_antigo_fornecedor = input("Digite o nome do Fornecedor que deseja alterar.\n")
                    nome_novo_fornecedor = input("Digite o nome do novo Fornecedor.\n")
                    cnpj_novo = input("Digite o novo CNPJ do novo Fornecedor.\n")
                    tel_novo = input("Digite o telefone do novo Fornecedor.\n")
                    nova_categoria = input("Digite a Categoria do novo Fornecedor.\n")
                    cat.alterar_fornecedor()
                elif decidir == 4:
                    cat.mostrar_fornecedores()
                else:
                    break

        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para Cadastrar Cliente.\n"
                                        "Digite 2 para Remover Cliente.\n"
                                        "Digite 3 para Alterar Cliente.\n"
                                        "Digite 4 para Mostrar Cliente.\n"
                                        "Digite 5 para Sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o Nome do Cliente.\n")
                    telefone = input("Digite o Telefone do Cliente.\n")
                    cpf = input("Digite o CPF do Cliente.\n")
                    email = input("Digite o Email do Cliente.\n")
                    endereco = input("Digite o Endereço do Cliente.\n")
                    cat.cadastrar_cliente(nome, telefone, cpf, email, email, endereco)
                elif decidir == 2:
                    nome_para_remover = input("Digite o Nome do Cliente que quer remover do sistema.\n")
                    cat.remover_cliente(nome_para_remover)
                elif decidir == 3:
                    nome_antigo = input("Digite o nome do Cliente que deseja alterar.\n")
                    nome_novo = input("Digite o Nome do novo Cliente.\n")
                    novo_telefone = input("Digite o Telefone do novo Cliente.\n")
                    cpf = input("Digite o CPF do novo Cliente.\n")
                    email = input("Digite o Email do novo Cliente.\n")
                    endereco = input("Digite o Novo Endereço do Cliente.\n")
                    cat.alterar_cliente(nome_antigo, nome_novo, novo_telefone, cpf, email, endereco)
                elif decidir == 4:
                    cat.mostrar_cliente()
                else:
                    break
        
        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para Cadastrar Funcionario.\n"
                                    "Digite 2 para Remover Funcionario.\n"
                                    "Digite 3 para Alterar Funcionario.\n"
                                    "Digite 4 para Mostrar Funcionario.\n"
                                    "Digite 5 para Sair\n"))
                if decidir == 1:
                    clt = input("Digite o CLT do Funcionario.")
                    nome = input("Digite o Nome do Funcionario.\n")
                    telefone = input("Digite o Telefone do Funcionario.\n")
                    cpf = input("Digite o CPF do Funcionario.\n")
                    email = input("Digite o Email do Funcionario.\n")
                    endereco = input("Digite o Endereço do Funcionario.\n")
                    cat.cadastrar_funcionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input("Digite o Nome do Funcionario que deseja Remover.\n")
                    cat.remover_funcionario(nome)
                elif decidir == 3:
                    nome_alterar = input("Digite o Nome do Funcionario que deseja Alterar.\n")
                    novo_clt = input("Digite o CLT do Novo Funcionario.\n")
                    novo_nome = input("Digite o Nome do Novo Funcionario.\n")
                    novo_telefone = input("Digite o Telefone do Novo Funcionario.\n")
                    novo_cpf = input("Digite o CPF do Novo Funcionario.\n")
                    novo_email = input("Digite o Email do Novo Funcionario.\n")
                    novo_endereco = input("Digite o Endereço do Novo Funcionario.\n")
                    cat.alterar_funcionario(nome_alterar, novo_clt, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco)
                elif decidir == 4:
                    cat.mostrar_funcionario()
                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            decidir = int(input("Digita 1 para Cadastrar Vendas.\n"
                                "Digite 2 para Mostrar Vendas\n" \
                                "Digite 3 para Sair\n"))
            
            if decidir == 1:
                produto = input("Digite o Nome do Produto.\n")
                vendendor = input("Digite o Nome do Vendedor.\n")
                comprador = input("Digite o Nome do Comprador.\n")
                quantidade = input("Digite a quantidade do produto que quer cadastrar.\n")
                cat.cadastrar_venda(produto, vendendor, comprador, quantidade)
            elif decidir == 2:
                inicio = input("Digite a data de inicio.\n")
                final = input("Digite a data final.\n")
                cat.mostrar_vendas(inicio, final)
            else:
                break
        
        elif local == 7:
            cat = Controller.ControllerVenda()
            cat.report_produtos_vendidos()

        else: 
            break # Finaliza rapidamente