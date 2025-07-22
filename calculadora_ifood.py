def calcular_preco_ifood():
    """
    Calcula o preço de venda de um produto no iFood para manter o mesmo lucro
    que seria obtido na venda presencial, considerando as taxas do iFood.
    """
    print("--- Calculadora de Preço para iFood ---")
    print("Este script irá te ajudar a precificar seus produtos no iFood,")
    print("mantendo o lucro que você teria na venda presencial.\n")

    try:
        # Solicita os dados ao usuário
        preco_presencial = float(input("Digite o preço de venda atual (presencial) do produto (Ex: 30.00): R$ "))
        custo_produto = float(input("Digite o custo direto de produção/aquisição do produto (Ex: 10.00): R$ "))
        comissao_ifood_percentual = float(input("Digite a porcentagem de comissão do iFood sobre o produto (Ex: 12 para 12%): "))

        # Validações básicas para evitar divisões por zero ou valores negativos
        if preco_presencial <= 0 or custo_produto < 0 or comissao_ifood_percentual < 0 or comissao_ifood_percentual >= 100:
            print("\nErro: Por favor, digite valores válidos. O preço presencial deve ser positivo, custos e comissão não negativos e a comissão menor que 100%.")
            return

        # Converte a comissão para formato decimal
        comissao_ifood_decimal = comissao_ifood_percentual / 100

        # 1. Calcular o Lucro Absoluto Presencial
        lucro_absoluto_presencial = preco_presencial - custo_produto

        # Se o lucro presencial for negativo, avisa o usuário
        if lucro_absoluto_presencial < 0:
            print(f"\nAtenção: Seu lucro presencial atual é negativo (Prejuízo de R$ {abs(lucro_absoluto_presencial):.2f}).")
            print("Você já está vendendo abaixo do custo. Considere ajustar seu preço presencial primeiro.")
            # Ainda assim, continua o cálculo para mostrar o preço necessário no iFood
            
        # 2. Calcular o Preço de Venda no iFood
        # PVI = (Custo + Lucro Absoluto) / (1 - Comissão)
        # Que é o mesmo que: PVI = Preço Presencial / (1 - Comissão)
        
        # O denominador (1 - comissao_ifood_decimal) não pode ser zero
        if (1 - comissao_ifood_decimal) == 0:
            print("\nErro: A comissão do iFood não pode ser 100% para este cálculo. Ajuste o valor da comissão.")
            return
            
        preco_venda_ifood = preco_presencial / (1 - comissao_ifood_decimal)

        # 3. Calcular o Lucro Absoluto no iFood (para verificação)
        custo_comissao_ifood = preco_venda_ifood * comissao_ifood_decimal
        lucro_absoluto_ifood = preco_venda_ifood - custo_produto - custo_comissao_ifood
        
        # Exibe os resultados
        print("\n--- Resultados do Cálculo ---")
        print(f"Preço de Venda Presencial: R$ {preco_presencial:,.2f}")
        print(f"Custo do Produto: R$ {custo_produto:,.2f}")
        print(f"Lucro Absoluto Desejado (presencial): R$ {lucro_absoluto_presencial:,.2f}")
        print(f"Comissão do iFood: {comissao_ifood_percentual:.2f}%")
        print(f"\nPara manter o mesmo lucro, o PREÇO DE VENDA NO IFOOD deve ser: R$ {preco_venda_ifood:,.2f}")
        print(f"Custo da Comissão do iFood sobre este preço: R$ {custo_comissao_ifood:,.2f}")
        print(f"Lucro Absoluto Estimado no iFood (para verificação): R$ {lucro_absoluto_ifood:,.2f}")


    except ValueError:
        print("\nErro: Por favor, digite apenas números para os valores.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

# Chama a função para executar o script
if __name__ == "__main__":
    calcular_preco_ifood()