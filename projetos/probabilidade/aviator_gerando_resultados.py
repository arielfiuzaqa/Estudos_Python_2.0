import pandas as pd
import random

# Simula 5000 rodadas baseadas em probabilidades realistas do Aviator
def gerar_multiplicadores(qtd=1000000):
    resultado = []
    for _ in range(qtd):
        r = random.random()
        if r < 0.02:
            mult = round(random.uniform(10, 100), 2)   # raros muito altos
        elif r < 0.10:
            mult = round(random.uniform(5, 10), 2)
        elif r < 0.30:
            mult = round(random.uniform(2, 5), 2)
        elif r < 0.60:
            mult = round(random.uniform(1.5, 2), 2)
        elif r < 0.90:
            mult = round(random.uniform(1.2, 1.5), 2)
        else:
            mult = round(random.uniform(1.01, 1.2), 2)
        resultado.append(mult)
    return resultado

# Gerar e salvar
multiplicadores = gerar_multiplicadores()
df = pd.DataFrame({"Multiplicador": multiplicadores})
df.to_excel(r"projetos\probabilidade\planilha jogos\resultados_aviator.xlsx", index=False)

print("✅ Planilha 'resultados_aviator.xlsx' gerada com sucesso.")
