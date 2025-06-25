from tqdm import tqdm

def simular_500_meses(capital_inicial, rendimento_mensal, uso_percentual_cenario1, uso_percentual_cenario2, meses_total=500):
    capital1 = capital_inicial
    capital2 = capital_inicial

    print("Mês | Cenário 1: Dividendos (R$) | Cenário 1: Capital (R$) | Cenário 2: Dividendos (R$) | Cenário 2: Capital (R$)")
    print("------------------------------------------------------------------------------------------------------")

    for mes in tqdm(range(1, meses_total + 1), desc="Simulando meses"):
        # Cenário 1 - 30% reinvestido, 70% retirado como dividendos
        rendimento1 = capital1 * rendimento_mensal
        dividendos1 = rendimento1 * (1 - uso_percentual_cenario1)
        reinvestimento1 = rendimento1 * uso_percentual_cenario1
        capital1 += reinvestimento1

        # Cenário 2 - 100% reinvestido, 0% retirado como dividendos
        rendimento2 = capital2 * rendimento_mensal
        dividendos2 = rendimento2 * (1 - uso_percentual_cenario2)
        reinvestimento2 = rendimento2 * uso_percentual_cenario2
        capital2 += reinvestimento2

        print(f"{mes:3d} | R$ {dividendos1:22,.2f} | R$ {capital1:18,.2f} | R$ {dividendos2:22,.2f} | R$ {capital2:18,.2f}")

def main():
    capital_inicial = 200_000
    rendimento_mensal = 0.0139  # 1,39% ao mês
    uso_percentual_cenario1 = 0.25   # 20% reinvestido, 80% retirado como dividendos
    uso_percentual_cenario2 = 0.5   # 50% reinvestido, 50% retirado como dividendos

    simular_500_meses(capital_inicial, rendimento_mensal, uso_percentual_cenario1, uso_percentual_cenario2, meses_total=480)

if __name__ == "__main__":
    main()
