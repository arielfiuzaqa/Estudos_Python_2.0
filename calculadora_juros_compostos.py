# Parâmetros principais
meta = 100000
valor_produto = 350
quantidade_vendida_mes = 30
percentual_para_investir = 0.40  
juros_mensal = 1.1  # 1%
periodo_meses = 120

# Cálculo de investimento mensal vindo das vendas
faturamento_mensal = valor_produto * quantidade_vendida_mes
aporte_mensal = faturamento_mensal * percentual_para_investir

# Juros compostos com aporte mensal
montante = 0
for mes in range(1, periodo_meses + 1):
    montante = (montante + aporte_mensal) * (1 + juros_mensal / 100)

print(f"Montante final após {periodo_meses} meses: R$ {montante:,.2f}")
