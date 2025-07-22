# --- Dados de Entrada (Você preenche aqui) ---
percentual_comissao = 0.15  # Ex: 0.09 para 9%
valor_produto = 35.97      # Ex: 100.00 para R$ 100,00
comissao_liquida_desejada_mes = 500.00 # Ex: 10000.00 para R$ 10.000 por mês
percentual_gastos_cpa_alvo = 0.50 # Ex: 0.50 para 50% da CBV destinado ao CPA
mes = 30  # Ex: 30 dias no mês

# --- Cálculos ---

# 1. Comissão Bruta por Venda (CBV)
cbv = valor_produto * percentual_comissao

# 2. Faturamento Bruto Necessário para atingir a meta
faturamento_bruto_necessario = comissao_liquida_desejada_mes / percentual_comissao

# 3. Número de Vendas Necessárias
numero_vendas_necessarias = faturamento_bruto_necessario / valor_produto
qtd_dia = numero_vendas_necessarias / mes

# 4. Custo por Aquisição (CPA) Alvo
cpa_alvo = cbv * percentual_gastos_cpa_alvo

# 5. Investimento em Tráfego (IT) Estimado
it_estimado = numero_vendas_necessarias * cpa_alvo

# --- Apresentação dos Resultados ---
print("--- Projeção de Vendas e Investimento ---")
print(f"")
print(f"Seus Dados de Entrada:")
print(f"- Comissão: {percentual_comissao * 100:.0f}%")
print(f"- Valor do Produto: R$ {valor_produto:,.2f}")
print(f"- Comissão Líquida Desejada por Mês: R$ {comissao_liquida_desejada_mes:,.2f}")
print(f"- Percentual do CPA Alvo sobre a CBV: {percentual_gastos_cpa_alvo * 100:.0f}%")
print(f"")
print("--- Métricas Calculadas ---")
print(f"")
print(f"1. **Comissão Bruta por Venda (CBV):**")
print(f"   É o valor que você recebe de comissão por cada produto vendido.")
print(f"   CBV = R$ {cbv:,.2f}")
print(f"")
print(f"2. **Faturamento Bruto Necessário:**")
print(f"   Valor total que você precisa vender para alcançar sua meta de comissão.")
print(f"   Faturamento Bruto Necessário = R$ {faturamento_bruto_necessario:,.2f}")
print(f"")
print(f"3. **Número de Vendas Necessárias:**")
print(f"   Quantidade de produtos que você precisa vender por mês.")
print(f"   Número de Vendas Necessárias = {numero_vendas_necessarias:,.0f} unidades")
print(f"   Número de Vendas Necessárias por dia = {qtd_dia:,.0f} unidades")
print(f"")
print(f"4. **Custo por Aquisição (CPA) Alvo:**")
print(f"   É o valor máximo que você deve pagar, em média, por cada venda (para que seja lucrativa).")
print(f"   CPA Alvo = R$ {cpa_alvo:,.2f}")
print(f"")
print(f"5. **Investimento em Tráfego (IT) Estimado:**")
print(f"   Valor estimado que você precisaria investir em tráfego pago para alcançar suas vendas, mantendo o CPA Alvo.")
print(f"   IT Estimado = R$ {it_estimado:,.2f}")
print(f"")
print("--- Próximos Passos ---")
print(f"Lembre-se que o marketing digital é dinâmico. Comece com um investimento menor para testar suas campanhas, otimize-as constantemente e escale gradualmente. O monitoramento contínuo do seu CPA real nas plataformas de anúncios é crucial para o sucesso!")