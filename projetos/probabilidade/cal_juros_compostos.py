import pandas as pd
from tabulate import tabulate

# Parâmetros configuráveis
aporte_mensal = 3000              # Valor mensal investido
rendimento_anual = 0.15           # Rentabilidade da carteira por ano
dividendos_anual = 0.06           # Percentual médio anual de dividendos
meta_final = 1_000_000            # Objetivo de R$ 1 milhão

# Cálculo dos rendimentos mensais
rendimento_mensal = (1 + rendimento_anual) ** (1 / 12) - 1
dividendos_mensal = (1 + dividendos_anual) ** (1 / 12) - 1

# Inicialização
saldo = 0
mes = 1
historico = []

# Simulação mês a mês
while saldo < meta_final:
    juros_mes = saldo * rendimento_mensal
    dividendos_mes = saldo * dividendos_mensal
    saldo += juros_mes + aporte_mensal

    historico.append({
        "Mês": mes,
        "Aporte (R$)": round(aporte_mensal, 2),
        "Juros (R$)": round(juros_mes, 2),
        "Dividendos (R$)": round(dividendos_mes, 4),
        "Total acumulado (R$)": round(saldo, 2)
    })

    mes += 1

# Converter para DataFrame
df = pd.DataFrame(historico)

# Mostrar todos os meses no terminal
print("\n📊 Evolução mês a mês até R$ 1 milhão:\n")
print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

# Mostrar o total de meses e anos para atingir a meta
total_meses = df.shape[0]
total_anos = round(total_meses / 12, 2)
print(f"\n📅 Tempo total para atingir R$ 1 milhão: {total_meses} meses ({total_anos} anos)")

# Salvar tudo em Excel
df.to_excel("evolucao_mensal_ate_1_milhao.xlsx", index=False)
print("💾 Planilha salva como 'evolucao_mensal_ate_1_milhao.xlsx'")
