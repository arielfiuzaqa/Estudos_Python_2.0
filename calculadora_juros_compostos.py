# Parâmetros principais
meta = 200_000
valor_produto = 10_000
incremento_percentual_produto_mensal = 0.01  # 1% de aumento mensal no valor do produto
quantidade_vendida_mes = 1
percentual_para_investir = 0.35
juros_mensal_percentual = 1  # 1% ao mês (será dividido por 100 na fórmula)
periodo_meses = 360

# --- Cenário com Incremento no Valor do Produto ---
montante_com_incremento = 0
valor_total_investido_com_incremento = 0 # Inicializa o total investido neste cenário
valor_produto_atual = valor_produto # Variável para o valor do produto que será incrementado

for mes in range(1, periodo_meses + 1):
    # Atualiza o valor do produto a cada mês (a partir do segundo mês)
    if mes > 1:
        valor_produto_atual *= (1 + incremento_percentual_produto_mensal)

    # Recalcula o faturamento e o aporte mensal com o novo valor do produto
    faturamento_mensal = valor_produto_atual * quantidade_vendida_mes
    aporte_mensal = faturamento_mensal * percentual_para_investir

    # Acumula o valor total investido (aportado)
    valor_total_investido_com_incremento += aporte_mensal

    # Aplica juros compostos com o aporte do mês
    montante_com_incremento = (montante_com_incremento + aporte_mensal) * (1 + juros_mensal_percentual / 100)

juros_rendidos_com_incremento = montante_com_incremento - valor_total_investido_com_incremento

print(f"--- Cenário com Incremento no Valor do Produto ---")
print(f"Montante final após {periodo_meses} meses: R$ {montante_com_incremento:,.2f}")
print(f"Valor total investido (aportes): R$ {valor_total_investido_com_incremento:,.2f}")
print(f"Juros rendidos sobre o investido: R$ {juros_rendidos_com_incremento:,.2f}")


# --- Cenário sem Incremento no Valor do Produto ---
montante_sem_incremento = 0
valor_total_investido_sem_incremento = 0 # Inicializa o total investido neste cenário

# O faturamento e o aporte mensal são fixos, baseados no valor_produto inicial
faturamento_mensal_fixo = valor_produto * quantidade_vendida_mes
aporte_mensal_fixo = faturamento_mensal_fixo * percentual_para_investir

for mes in range(1, periodo_meses + 1):
    # Acumula o valor total investido (aportado)
    valor_total_investido_sem_incremento += aporte_mensal_fixo

    montante_sem_incremento = (montante_sem_incremento + aporte_mensal_fixo) * (1 + juros_mensal_percentual / 100)

juros_rendidos_sem_incremento = montante_sem_incremento - valor_total_investido_sem_incremento

print(f"\n--- Cenário sem Incremento no Valor do Produto ---")
print(f"Montante final após {periodo_meses} meses: R$ {montante_sem_incremento:,.2f}")
print(f"Valor total investido (aportes): R$ {valor_total_investido_sem_incremento:,.2f}")
print(f"Juros rendidos sobre o investido: R$ {juros_rendidos_sem_incremento:,.2f}")


# --- Comparação entre os Cenários ---
print(f"\n--- Comparação entre os Cenários ---")
diferenca_montantes = montante_com_incremento - montante_sem_incremento
percentual_crescimento_com_incremento = (diferenca_montantes / montante_sem_incremento) * 100 if montante_sem_incremento != 0 else 0

print(f"A diferença entre os montantes finais (com incremento - sem incremento) é: R$ {diferenca_montantes:,.2f}")
print(f"O montante com incremento cresceu {percentual_crescimento_com_incremento:,.2f}% em relação ao montante sem incremento.")