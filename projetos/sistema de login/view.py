from controller import ControllerCadastro, ControllerLogin
import time

while True:
    print("===================== [MENU] =====================")
    descidir = int(input(f"[1] - Cadastrar usuário\n[2] - Logar usuário\n[3] - Sair\nDigite a opção desejada: "))
    print("===================================================")

    if descidir == 1:
        nome = input("Digite o nome do usuario: ")
        email = input("Digite o email do usuario: ")
        senha = input("Digite a senha do usuario: ")
        resultado = ControllerCadastro.cadastrar(nome, email, senha)
        print("Cadastrando usuário...")
        time.sleep(2)

        if resultado == 2:
            print("Tamanho do nome digitado é inválido!")
        elif resultado == 3:
            print("Tamanho do email digitado é maior que 200 caracteres, inválido!")
        elif resultado == 4:
            print("Tamanho da senha digitada inválido!")
        elif resultado == 5:
            print("Email já cadastrado!")
        elif resultado == 6:
            print("Erro ao cadastrar usuário!")
        elif resultado == 1:
            print("Usuário cadastrado com sucesso!")


    elif descidir == 2:
        nome = input("Digite o nome do usuario: ")
        senha = input("Digite a senha do usuario: ")
        resultado = ControllerLogin.login(nome, senha)
        print("Logando usuário...")
        time.sleep(1)
        if not resultado:
            print("Email ou senha inválidos!")
        else:
            print("Usuário logado com sucesso!")
            print(f"ID do usuário: {resultado['id']}")
    else:
        print("Saindo do sistema...")
        time.sleep(1)
        break